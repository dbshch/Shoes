#!/usr/bin/python
# __author__ = 'dbshch'

import tornado.ioloop
import tornado.web
import json
import os
import time


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        fp = open("shoes.txt", 'r')
        l = fp.read()
        l = l.split(',')
        fp.close()
        self.render("index.html", l=l)

class takeHandler(tornado.web.RequestHandler):
    def get(self):
        fp = open("shoes.txt", 'r')
        l = fp.read()
        fp.close()
        fp = open("shoes.txt", 'w')
        l = l.split(',')
        id = self.get_arguments("cid")
        l[int(id[0])] = 'n'
        l = ','.join(l)
        fp.write(l)
        fp.close()
        self.write('a')


class putHandler(tornado.web.RequestHandler):
    def get(self):
        fp = open("shoes.txt", 'r')
        l = fp.read()
        fp.close()
        fp = open("shoes.txt", 'w')
        l = l.split(',')
        id = self.get_arguments("cid")
        l[int(id[0])] = 'y'
        l = ','.join(l)
        fp.write(l)
        fp.close()
        self.write('a')

def make_app():
    settings = {"static_path": os.path.join(os.path.dirname(__file__), "static")}
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/get", takeHandler),
        (r"/put", putHandler),
    ], **settings)


if __name__ == "__main__":
    app = make_app()
    app.listen(13000)
    tornado.ioloop.IOLoop.current().start()
