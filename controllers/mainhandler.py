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
        #from tvalacarta.channels import a3media as channelmodule
        #channels = channelmodule.mainlist(None)
        import channelselector
        channels = channelselector.fav_channels_list()
#         for item in channels:
#             jsonOut = json.dumps(item, default=lambda o: o.__dict__)
#             self.response.write(jsonOut)
#             self.response.write("<br><br><br>")

        template_values = {'channels': channels}
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))


    def post(self):
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write("POST")

#{"category": "", "language": "", "title": "Documentales", "totalItems": 0, "password": "", "viewmode": "list", "action": "secciones", "channel": "a3media", "overlay": null, "folder": true, "extra": "", "url": "http://servicios.atresplayer.com/api/categorySections/80000011", "server": "directo", "type": "", "fanart": "", "context": "", "subtitle": "", "thumbnail": "", "plot": "", "show": "", "fulltitle": "", "duration": "", "page": "http://servicios.atresplayer.com/api/categorySections/80000011", "childcount": 0}
#{"channel": "a3media", "viewmode": "list", "action": "", "totalItems": 0, "overlay": null, "context": "", "category": "N", "thumbnail": "", "subtitle": "", "folder": true, "title": "AtresPlayer", "fanart": "", "language": "ES", "extra": "", "show": "", "type": "generic", "fulltitle": "", "plot": "", "url": "", "duration": "", "page": "", "password": "", "server": "directo", "childcount": 0}