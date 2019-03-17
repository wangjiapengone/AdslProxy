import platform
import re
import redis
import time
import requests
from requests.exceptions import RequestException, ConnectionError
from adslproxy.db import RedisClient
from adslproxy.config import *


if platform.python_version().startswith('3.'):
    import subprocess
elif platform.python_version().startswith('2.'):
    import commands as subprocess
else:
    raise('python version must be 2 or 3')


class Sender:
    def get_ip(self, ifname=ADSL_IFNAME):
        '''
        获取本机的IP

        :param ifname: 网卡名称
        :return:
        '''
        status, output = subprocess.getstatusoutput('ifconfig')
        if status == 0:  # 代表 cmd 命令执行成功了
            pattern = re.compile(ifname + '.*?inet (\d+\.\d+\.\d+\.\d+).*?netmask', re.S)
            result = pattern.search(output)
            if result:
                return result.group(1)

    def test_proxy(self, proxy):
        '''
        测试代理

        :param proxy: 代理
        :return:
        '''
        try:
            response = requests.get(TEST_URL, proxies={
                'http': 'http://{}'.format(proxy),
                'https': 'https://{}'.format(proxy),
            }, timeout=TEST_TIMEOUT)
        except RequestException:
            return False
        else:
            return True if response.status_code == 200 else False

    def remove_proxy(self):
        '''
        移除代理

        :return:
        '''
        self.redis = RedisClient()
        try:
            self.redis.remove(CLIENT_NAME)
        except redis.exceptions.ConnectionError:
            return False
        else:
            print('Successfully Removed Proxy')
            return True

    def set_proxy(self, proxy):
        '''
        设置代理

        :param proxy: 代理
        :return:
        '''
        self.redis = RedisClient()
        if self.redis.set(CLIENT_NAME, proxy):
            print('Successfully Set Proxy:', proxy)

    def adsl(self):
        '''
        拨号主进程
        :return:
        '''
        while True:
            print('ADSL Start, Remove Proxy, Please wait')
            if self.remove_proxy():
                status = -1
                while status != 0:
                    status, output = subprocess.getstatusoutput(ADSL_BASH)
                if status == 0:
                    print('ASDL Successfully')
                    time.sleep(ASDL_ERROR_CYCLE)
                    ip = self.get_ip()
                    if ip:
                        print('IP:', ip)
                        proxy = '{}:{}'.format(ip, PROXY_PORT)
                        if self.test_proxy(proxy):
                            print('Valid proxy')
                            self.set_proxy(proxy)
                            print('Sleeping')
                            time.sleep(ASDL_CYCLE)
                        else:
                            print('Invalid Proxy')
                    else:
                        print('Get IP failed, Re Dailing...')
                        time.sleep(ASDL_ERROR_CYCLE)
                else:
                    print('ASDL Failed, Please Check')
                    time.sleep(ASDL_ERROR_CYCLE)
            else:
                print('Redis Connection Failed, Try Again...')
                time.sleep(ASDL_ERROR_CYCLE)


def run():
    sender = Sender()
    sender.adsl()


if __name__ == '__main__':
    run()