import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import webapp2
from controllers.mainhandler import *

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/item/(.*)', ItemHandler),
    ('/channel/(.*)', ChannelHandler),
], debug=True)