#'''
#Created on 30 mei 2009
#
#@author: Bram Walet
#'''
#import xml.sax
#from classes.Subtitle import Subtitle
#
#from xml.sax.handler import ContentHandler 
#
#class XmlSubtitleListParser(ContentHandler):
#    '''
#    classdocs
#    '''
#    value_names = (u"title",
#            u"tvSeason",
#            u"tvEpisode",
#            u"id", )
#
#    def __init__(self,tagname):
#        '''
#        Constructor
#        '''
#        self.tagname = tagname
#        self.foundSubs = []
#        self._isTitleElement = False
#        self._isTvSeasonElement = False
#        self._isTvEpisodeElement = False
#        self._isIdElement = False
#        self.episode = None
#        self.season = None
#        self.title = None
#        self.id = None
#        
#    def startElement(self, name, attrs):
#        self._get_characters = False
#
#
#        if name == "subtitle": #new item
#            #reset some shit
#            self.title = ""
#            self.season = ""
#            self.episode = ""
#            self.id = ""
#            
#        elif name in XmlSubtitleListParser.value_names:
#            if name == "title":
#                self._isTitleElement = True
#                self._get_characters = True
#            if name == "tvSeason":
#                self._isTvSeasonElement = True
#                self._get_characters = True
#            if name == "tvEpisode":
#                self._isTvEpisodeElement = True
#                self._get_characters = True
#            if name == "id":
#                self._isIdElement = True
#                self._get_characters = True
#
#
#    def characters (self, content):    
#        if self._get_characters is True:
#            if self._isTitleElement is True:
#                self.title = content
#                self._isTitleElement = False
#            if self._isTvSeasonElement is True:
#                self.season = content
#                self._isTvSeasonElement = False
#            if self._isTvEpisodeElement is True:
#                self.episode = content
#                self._isTvEpisodeElement = False
#            if self._isIdElement is True:
#                self.id = content
#                self._isIdElement = False
#
#        
#    def endElement(self,name):
#        if name == "subtitle":
#            newSub = Subtitle(self.title, self.season, self.episode, self.id)
#            #print " found something" 
#            #print newSub.printSubtitle()
#            self.foundSubs.append(newSub)
#        
#    def endDocument(self):
#        return self.foundSubs
#    