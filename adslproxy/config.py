# Redis数据库配置参数
REDIS_HOST = '47.93.19.178'
REDIS_PORT = 6379
REDIS_PASSWD = 'wangjiapeng'

# 代理池键名
PROXY_KEY = 'adsl'

# API 端口
API_PORT = 8000

# 代理运行端口
PROXY_PORT = 8888

# ADSL拨号命令
ADSL_BASH = 'adsl-stop;adsl-start'

# 拨号网卡的名称
ADSL_IFNAME = 'ppp0'

# 测试URL地址
TEST_URL = 'http://www.pss-system.gov.cn/sipopublicsearch/portal/uiIndex.shtml'
# 测试超时时间
TEST_TIMEOUT = 10

# 客户端（拨号服务器）名称
CLIENT_NAME = 'adsl2'

# 拨号间隔
ASDL_CYCLE = 100
# 拨号出错重试间隔
ASDL_ERROR_CYCLE = 5