from google.appengine.ext import ndb

class Item(ndb.Model):
    channel = ndb.StringProperty(indexed=False)
    title = ndb.StringProperty(indexed=False)
    url = ndb.StringProperty(indexed=True)
    page = ndb.StringProperty(indexed=False)
    thumbnail = ndb.StringProperty(indexed=False)
    plot = ndb.StringProperty(indexed=False)
    duration = ndb.StringProperty(indexed=False)
    fanart = ndb.StringProperty(indexed=False)
    folder = ndb.BooleanProperty(indexed=False)
    action = ndb.StringProperty(indexed=False)
    server =  ndb.StringProperty(indexed=False, default='directo')
    extra = ndb.StringProperty(indexed=False, default='')
    show = ndb.StringProperty(indexed=False)
    category = ndb.StringProperty(indexed=False)
    childcount = ndb.IntegerProperty(indexed=False)
    language = ndb.StringProperty(indexed=False)
    type = ndb.StringProperty(indexed=False)
    context = ndb.StringProperty(indexed=False)
    subtitle = ndb.StringProperty(indexed=False)
    totalItems = ndb.IntegerProperty(indexed=False)
    overlay = ndb.StringProperty(indexed=False)
    password = ndb.StringProperty(indexed=False)
    fulltitle = ndb.StringProperty(indexed=False)
    viewmode = ndb.StringProperty(indexed=False, default='list')

    @property
    def unititle(self):
        return unicode(self.title, "utf8")

    @property
    def thumbnailURL(self):
        if self.thumbnail is None or self.thumbnail is "":
            return 'http://ia.media-imdb.com/images/G/01/imdb/images/nopicture/small/no-video-slate-856072904._V379390253_.png'
        else:
            return self.thumbnail

    def tostring(self):
        return "title=["+self.title+"], url=["+self.url+"], thumbnail=["+self.thumbnail+"], action=["+self.action+"], show=["+self.show+"], category=["+self.category+"]"

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
