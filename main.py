import webapp2
from controllers.mainhandler import *

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)