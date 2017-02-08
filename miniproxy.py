import tornado.ioloop
import tornado.web
import requests


class MainHandler(tornado.web.RequestHandler):
    

    def get(self):
        self.write('<html><body><form method="POST">'
                   '<input type="text" name="siteAcessado">'
                   '<input type="submit" value="Submit">'
                   '</form></body></html>')

    def post(self):
        self.set_header("Content-Type", "html")
        site = requests.get(self.get_body_argument("siteAcessado"))
        try:
            self.write(site.content)
        except Exception as e:
            print "erro: ",e



def make_app():

    settings = {
    "static_path": '/',
    }
    
    return tornado.web.Application([
        (r"/", MainHandler)
        ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()