import json
import tornado.ioloop
from tornado.web import RequestHandler, Application
from adslproxy.config import API_PORT


class MainHandler(RequestHandler):
    def initialize(self, redis):
        self.redis = redis

    def get(self, api=''):
        if not api:  # 如果没给请求参数
            links = ['random', 'proxies', 'all', 'names', 'count']
            self.write('<h3>Welcome to ADSL Proxy API<h3>')
            for link in links:
                self.write('<a href={link}>{link}</a><br>'.format(link=link))

        if api == 'random':
            result = self.redis.random()
            if result:
                self.write(result)

        if api == 'names':
            result = self.redis.names()
            if result:
                self.write(json.dumps(result))

        if api == 'proxies':
            result = self.redis.proxies()
            if result:
                self.write(json.dumps(result))

        if api == 'all':
            result = self.redis.all()
            if result:
                self.write(json.dumps(result))

        if api == 'count':
            self.write(str(self.redis.count()))


def server(redis, port=API_PORT, address=''):
    application = Application([
        (r'/', MainHandler, dict(redis=redis)),
        (r'/(.*)', MainHandler, dict(redis=redis)),
    ])
    application.listen(port, address=address)
    print('ADSL API listening on', port)
    tornado.ioloop.IOLoop.instance().start()
