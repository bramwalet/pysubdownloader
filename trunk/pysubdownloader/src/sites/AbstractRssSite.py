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

    
    def setUpHandlers(self):
        self.fh = FileHandler(self.logfile)
        self.uh = UrlHandler(self.logfile)
        self.fparser = FilenameParser(self.logfile)
        rssFeedUrl = self.getRssFeedUrl(self.language)
        self.rssparser = RssFeedParser(rssFeedUrl, self.config["baseUrl"],self.logfile)

    def checkConfig(self,config):
        requiredKeys = ('siteName','baseUrl','rssFeed')
        super(AbstractRssSite,self).checkConfig(config,requiredKeys)
    
        
    def search(self,episodes):
         self.log.info("Search for new episodes on RSS feed.")
         
         availableSubs = self.rssparser.parse()
         for aSub in availableSubs: 
            for episode in episodes:
                if episode.appropriateSub(aSub):
                    self.log.info("Match found for episode: " + episode.printEpisode())
                    self.downloadSubtitle(aSub, episode)
                    
                    
#    def downloadSubtitle(self,sub,episode):
#        downloadurl = sub.getLink()
#        filein = self.uh.executeRequest(downloadurl)
#        archive = self.fh.openZipFile(filein) 
#        if self.fh.extractZipFile(episode, archive):
#            self.log.info("Extracted subtitle for: " + episode.printEpisode())
    
    def getRssFeedUrl(self,language):
         rssFeedUrl = self.config["rssFeed"]
         rssFeedUrl.replace("#lang#",language)
         return rssFeedUrl     