from google.appengine.ext import ndb

class Item(ndb.Model):
    action = ndb.StringProperty(indexed=False, default='')
    category = ndb.StringProperty(indexed=False, default='')
    channel = ndb.StringProperty(indexed=False, default='')
    childcount = ndb.IntegerProperty(indexed=False)
    context = ndb.StringProperty(indexed=False, default='')
    duration = ndb.StringProperty(indexed=False, default='')
    extra = ndb.StringProperty(indexed=False, default='')
    fanart = ndb.StringProperty(indexed=False, default='')
    folder = ndb.BooleanProperty(indexed=False)
    fulltitle = ndb.StringProperty(indexed=False, default='')
    language = ndb.StringProperty(indexed=False, default='')
    overlay = ndb.StringProperty(indexed=False, default='')
    page = ndb.StringProperty(indexed=False, default='')
    password = ndb.StringProperty(indexed=False, default='')
    plot = ndb.StringProperty(indexed=False, default='')
    server =  ndb.StringProperty(indexed=False, default='directo')
    show = ndb.StringProperty(indexed=False, default='')
    subtitle = ndb.StringProperty(indexed=False, default='')
    thumbnail = ndb.StringProperty(indexed=False, default='')
    title = ndb.StringProperty(indexed=False, default='')
    totalItems = ndb.IntegerProperty(indexed=False)
    type = ndb.StringProperty(indexed=False, default='')
    url = ndb.StringProperty(indexed=True, default='')
    viewmode = ndb.StringProperty(indexed=False, default='list')
    view = ndb.StringProperty(indexed=False, default='')

    @property
    def unititle(self):
        return unicode(self.title, "utf8")

    @property
    def thumbnailURL(self):
        if self.thumbnail is '':
            return 'http://ia.media-imdb.com/images/G/01/imdb/images/nopicture/small/no-video-slate-856072904._V379390253_.png'
        else:
            return self.thumbnail

    def tostring(self):
        return "title=["+self.title+"], url=["+self.url+"], thumbnail=["+self.thumbnailURL+"], action=["+self.action+"], show=["+self.show+"], category=["+self.category+"]"

    def serialize(self):
        separator = "|>|<|"
        devuelve = ""
        devuelve = devuelve + self.title + separator
        devuelve = devuelve + self.url + separator
        devuelve = devuelve + self.channel + separator
        devuelve = devuelve + self.action + separator
        devuelve = devuelve + self.server + separator
        devuelve = devuelve + self.extra + separator
        devuelve = devuelve + self.category + separator
        devuelve = devuelve + self.fulltitle + separator
        devuelve = devuelve + self.viewmode + separator
        return devuelve

    def deserialize(self,cadena):
        trozos=cadena.split("|>|<|")
        self.title = trozos[0]
        self.url = trozos[1]
        self.channel = trozos[2]
        self.action = trozos[3]
        self.server = trozos[4]
        self.extra = trozos[5]
        self.category = trozos[6]
        self.fulltitle = trozos[7]
        self.viewmode = trozos[8]
