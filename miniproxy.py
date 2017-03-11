import tornado.ioloop
import tornado.web
import requests
from subprocess import call
import os


class MainHandler(tornado.web.RequestHandler):
    
    
    def get(self):
        self.write('<html><body><form action="/" method="POST">'
                   '<input type="text" name="siteAcessado">'
                   '<input type="submit" value="Submit">'
                   '</form></body></html>')


    def post(self):
        self.set_header("Content-Type", "html")
        site = requests.get("http://"+self.get_body_argument("siteAcessado"))
        

        self.urlSite = self.get_body_argument("siteAcessado")
        self.siteHTML = site.content
        call (['C://GnuWin32/bin/wget.exe', '--recursive', '--no-clobber', '--page-requisites', '--html-extension', '--convert-links', '--restrict-file-names=windows', '--domains', self.urlSite, '--no-parent', '-nH', '--directory-prefix=static', 'http://'+self.urlSite+''])
        call (['C://GnuWin32/bin/wget.exe', '--recursive', '--no-clobber', '--page-requisites', '--html-extension', '--convert-links', '--restrict-file-names=windows', '--domains', self.urlSite, '--no-parent', '-nH', '--directory-prefix=static', 'http://'+self.urlSite+''])

        
        self.write(self.siteHTML)

    def write_error(self, status_code, **kwargs):
        if status_code in [403, 500, 503]:
            self.write('Error %s' % status_code)
        elif status_code == 404:
            print '\n\n\nque nada \n\n\n'
            print os.path.abspath('static')

        else:
            self.write('BOOM!')
    

class PagePreProcessor(MainHandler):


    def __init__(self):

        self.urlSite = url
        self.siteHTML = html






class ErrorHandler(tornado.web.ErrorHandler, MainHandler):
    """
    Default handler gonna to be used in case of 404 error
    """
    pass





def make_app():

    settings = {
    'default_handler_class': ErrorHandler,
    'default_handler_args': dict(status_code=404),
    'static_path': os.path.abspath('static'),
    'static_url_prefix': '/static/',
    }
    
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/(.*)", tornado.web.StaticFileHandler, dict(path=settings['static_path'])),
        ], **settings)


if __name__ == "__main__":
    
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
