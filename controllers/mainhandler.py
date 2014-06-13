import jinja2, webapp2
import sys
import json

from core import platform_name
platform_name.PLATFORM_NAME="developer"

#Templates environment
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader('views/'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):

    def get(self):
        from tvalacarta.channels import a3media as channelmodule
        resultado = channelmodule.mainlist(None)
        for item in resultado:
            jsonOut = json.dumps(item, default=lambda o: o.__dict__)
            self.response.write(jsonOut)
            self.response.write("<br><br><br>")

        #template_values = {'loggedInUserName': resultado}
        #template = JINJA_ENVIRONMENT.get_template('index.html')
        #self.response.write(template.render(template_values))


    def post(self):
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write("POST")

