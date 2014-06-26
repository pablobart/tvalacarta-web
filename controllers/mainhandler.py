import jinja2, webapp2
import sys
import json
import logging
from core.item import Item
from google.appengine.ext import ndb

from core import platform_name
platform_name.PLATFORM_NAME="developer"

#Templates environment
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader('views/'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):

    def get(self):
        import channelselector
        channels = channelselector.fav_channels_list()
        template_values = {'channels': channels}
        template = JINJA_ENVIRONMENT.get_template('channels.html')
        self.response.write(template.render(template_values))

class ChannelHandler(webapp2.RequestHandler):

    def get(self, channel):
        # try:
        exec "from tvalacarta.channels import "+channel+" as channelmodule"
        sections = channelmodule.mainlist(None)
        ndb.put_multi(sections)
        template_values = {'items': sections}
        template = JINJA_ENVIRONMENT.get_template('item.html')
        self.response.write(template.render(template_values))
        # except:
            # self.response.write("<h1>Incorrect Channel</h1>")

class ItemHandler(webapp2.RequestHandler):

    def get(self, itemid):
        # try:
        item_key = ndb.Key(urlsafe=itemid)
        item = item_key.get()
        if item is not None:
            exec "from tvalacarta.channels import "+item.channel+" as channelmodule"
            if item.action == "play":
                playitem = channelmodule.play(item)
                template_values = {'item':playitem[0]}
                template = JINJA_ENVIRONMENT.get_template('play.html')
                self.response.write(template.render(template_values))
            else:
                items = []
                method = getattr(channelmodule, item.action)
                items = method(item)

                if len(items) > 0:
                    ndb.put_multi(items)
                    template_values = {'items':items}
                    template = JINJA_ENVIRONMENT.get_template('item.html')
                    self.response.write(template.render(template_values))
                else:
                    self.response.write("<h1>No items</h1>")
        else:
            self.redirect("/")
        # except Exception as e:
            # logging.error(e)
            # self.redirect("/")


