'''
Created on 20 mei 2009

@author: Bram Walet
'''

from lxml.html import fromstring

from classes.Subtitle import Subtitle
from classes.ConfigException import ConfigException
from handlers.FileHandler import FileHandler
from handlers.UrlHandler import UrlHandler
from sites.AbstractSubtitleSite import AbstractSubtitleSite


class AbstractHtmlSite(AbstractSubtitleSite):
    '''
    classdocs
    '''

       
    def setUpHandlers(self):
        self.fh = FileHandler()
        self.uh = UrlHandler()
    
    def checkConfig(self):
        requiredKeys = ('siteName','findTableString','findDownloadLink','baseUrl','searchUrl')
        super(AbstractHtmlSite,self).checkConfig(requiredKeys)
    
        
    def createSearchQuery(self,episode): 
        (searchKeys,sep) = self.getKeys(episode)
        searchUrl = self.config["searchUrl"]
        searchQueryUrl = searchUrl + sep.join(searchKeys)
        return searchQueryUrl

    
    def search(self, episodes):
        self.log.debug("Search for each episode.")
        
        for episode in episodes:
            self.log.debug("Search for " + episode.printEpisode())
            searchUrl = self.createSearchQuery(episode)
            sub = self.searchEpisode(episode,searchUrl)
            if sub != None:
                self.log.debug("Match found for episode: " + episode.printEpisode + " on site " + self.siteName)
                self.downloadSubtitle(sub,episode,self.siteName)
                
    def searchEpisode(self,episode,searchUrl):
        self.uh.installUrlHandler()
        response = self.uh.executeRequest(searchUrl)
        doc = fromstring(response.read())
        doc.make_links_absolute(searchUrl,self.config["baseUrl"])
        list = doc.find_class(self.config["findTableString"])
        for listitem in list:
            for (element, attribute, link, pos) in listitem.iterlinks():
                if re.search(self.config["findDownloadLink"],link):
                    return Subtitle(episode.getSerie(), episode.getSeason(), episode.getEpisode(), link)
                    
