import redis
import random
from adslproxy.config import *


class RedisClient:
    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, passwd=REDIS_PASSWD, proxy_key=PROXY_KEY):
        '''
        初始化 redis 连接

        :param host: 地址
        :param port: 端口
        :param proxy_key: 哈希表名
        '''
        self.db = redis.StrictRedis(host=host, port=port, password=passwd, decode_responses=True)
        self.proxy_key = proxy_key

    def set(self, name, proxy):
        '''
        存入数据库

        :param name: ADSL服务器名称
        :param proxy: 代理
        :return: 设置结果
        '''
        return self.db.hset(self.proxy_key, name, proxy)

    def get(self, name):
        '''
        获取代理

        :param name: ADSL服务器名称
        :return: 代理
        '''
        return self.db.hget(self.proxy_key, name)

    def count(self):
        '''
        代理总数

        :return: 总数
        '''
        return self.db.hlen(self.proxy_key)

    def remove(self, name):
        '''
        删除代理

        :param name: ADSL服务器名称
        :return: 删除结果
        '''
        return self.db.hdel(self.proxy_key, name)

    def names(self):
        '''
        获取服务器名称列表

        :return: 名称列表
        '''
        return self.db.hkeys(self.proxy_key)

    def proxies(self):
        '''
        获取代理列表

        :return: 代理列表
        '''
        return self.db.hvals(self.proxy_key)

    def random(self):
        '''
        获取随机代理

        :return: 随机代理
        '''
        return random.choice(self.proxies())

    def all(self):
        '''
        获取字典

        :return: 字典
        '''
        return self.db.hgetall(self.proxy_key)


