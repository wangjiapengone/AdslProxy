from adslproxy.api import server
from adslproxy.db import RedisClient


if __name__ == '__main__':
    redis = RedisClient()
    server(redis)