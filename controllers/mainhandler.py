import jinja2
import sys
import logging
import webapp2

from core import platform_name
platform_name.PLATFORM_NAME="developer"

#Templates environment
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader('views/'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):

    def get(self):

        try:
            from tvalacarta.channels import antena3 as channelmodule
            resultado = channelmodule.test()
            self.response.write(resultado)
        except:
            import traceback

            exc_type, exc_value, exc_tb = sys.exc_info()
            lines = traceback.format_exception(exc_type, exc_value, exc_tb)
            for line in lines:
                line_splits = line.split("\n")
                for line_split in line_splits:
                    print line_split

        template_values = {'loggedInUserName': "test"}
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))


    def post(self):
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write("POST")

