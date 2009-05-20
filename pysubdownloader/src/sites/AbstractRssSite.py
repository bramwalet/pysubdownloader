'''
Created on 20 mei 2009

@author: Bram Walet
'''

from classes.ConfigException import ConfigException
from handlers.FileHandler import FileHandler
from handlers.UrlHandler import UrlHandler
from lib.FilenameParser import FilenameParser
from lib.RssFeedParser import RssFeedParser
from sites.AbstractSubtitleSite import AbstractSubtitleSite

class AbstractRssSite(AbstractSubtitleSite):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super(AbstractRssSite,self).__init__()
       
    def setUpHandlers(self):
        self.fh = FileHandler()
        self.uh = UrlHandler()
        self.fparser = FilenameParser()
        self.rssparser = RssFeedParser(self.config["rssFeed"], self.config["baseUrl"])

    def checkConfig(self):
        requiredKeys = ('siteName','baseUrl','rssFeed')
        super(AbstractRssSite,self).checkConfig(requiredKeys)
    
        
    def search(self,episodes):
         print "Search for episodes on: " + self.config["siteName"]
         
         availableSubs = self.rssparser.parse()
         for aSub in availableSubs: 
            for episode in episodes:
                if episode.appropriateSub(aSub):
                    print "Match found for episode: " + episode.printEpisode() + " on site " + self.config["siteName"]
                    self.downloadSubtitle(aSub, episode)
                    
                    
    def downloadSubtitle(self,sub,episode):
        downloadurl = sub.getLink()
        self.uh.installUrlHandler()
        filein = self.uh.executeRequest(downloadurl)
        archive = self.fh.openZipFile(filein) 
        if self.fh.extractZipFile(episode, archive):
            print "Extracted subtitle for: " + episode.printEpisode() + " on site: " + self.config["siteName"]
        