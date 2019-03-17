from adslproxy.db import RedisClient


if __name__ == '__main__':
    client = RedisClient()

    print('Random:', client.random())
    print('All:', client.all())
    print('Names:', client.names())
    print('Proxies:', client.proxies())
    print('Count:', client.count())