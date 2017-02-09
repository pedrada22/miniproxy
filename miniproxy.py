import tornado.ioloop
import tornado.web
import requests


class MainHandler(tornado.web.RequestHandler):
    
    def vars(self,url='',html=''):
        self.urlSite = url
        self.siteHTML = html

    def mudaLocal(self):
        
        return self.siteHTML.replace(self.request.uri, self.urlSite+self.request.uri)

    def get(self):
        self.write('<html><body><form action="/" method="POST">'
                   '<input type="text" name="siteAcessado">'
                   '<input type="submit" value="Submit">'
                   '</form></body></html>')


    def post(self):
        self.set_header("Content-Type", "html")
        site = requests.get(self.get_body_argument("siteAcessado"))
        
        self.vars()

        self.urlSite = self.get_body_argument("siteAcessado")
        self.siteHTML = site.content

        self.write(self.siteHTML)


    def write_error(self, status_code, **kwargs):
        if status_code in [403, 500, 503]:
            self.write('Error %s' % status_code)
        elif status_code == 404:
            import pdb;pdb.set_trace()
            
            self.write(self.mudaLocal())

        else:
            self.write('BOOM!')


class ErrorHandler(tornado.web.ErrorHandler, MainHandler):
    """
    Default handler gonna to be used in case of 404 error
    """
    pass


def make_app():

    settings = {
    'default_handler_class': ErrorHandler,
    'default_handler_args': dict(status_code=404)
    }
    
    return tornado.web.Application([
        (r"/", MainHandler),
        ], **settings)


if __name__ == "__main__":
    
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()