import jinja2, webapp2
from google.appengine.ext import ndb
from google.appengine.api import users

#Templates environment
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader('views/'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class FavouriteHandler(webapp2.RequestHandler):

    def get(self, action):
        #Protect the GET only for logged users
        user = users.get_current_user()
        if user:
            template_values = {'items': []}
            template = JINJA_ENVIRONMENT.get_template('item.html')
            self.response.write(template.render(template_values))
        else:
            self.redirect(users.create_login_url(self.request.uri))