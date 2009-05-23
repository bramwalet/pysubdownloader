'''
Created on 20 mei 2009

@author: Bram Walet
'''

from lxml.html import fromstring
from lxml import html
import urllib, re

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
        self.fh = FileHandler(self.logfile)
        self.uh = UrlHandler(self.logfile)
    
    def checkConfig(self,config):
        requiredKeys = ('siteName','findTableString','findDownloadLink','baseUrl','searchUrl')
        super(AbstractHtmlSite,self).checkConfig(config,requiredKeys)
        
    def createSearchQuery(self,episode): 
        searchKeys = self.getKeys(episode)
        searchUrl = self.config["searchUrl"]
        searchQueryUrl = searchUrl + urllib.urlencode(searchKeys)
        self.log.debug("Search URL: " + searchQueryUrl)
        return searchQueryUrl

    
    def search(self, episodes):
        self.log.info("Search for each episode.")
        
        for episode in episodes:
            self.log.info("Search for " + episode.printEpisode())
            searchUrl = self.createSearchQuery(episode)
            sub = self.searchEpisode(episode,searchUrl)
            if sub != None:
                self.log.info("Match found for episode: " + episode.printEpisode())
                self.downloadSubtitle(sub,episode)
                
    def searchEpisode(self,episode,searchUrl):
        self.uh.installUrlHandler()
        response = self.uh.executeRequest(searchUrl)
        html = response.read()
        #self.log.debug(html)
        doc = fromstring(html)
        doc.make_links_absolute(searchUrl,self.config["baseUrl"])
        list = doc.find_class(self.config["findTableString"])
      #  self.log.debug(str(list))
        for listitem in list:
       #     self.log.debug(listitem.text_content())
            for (element, attribute, link, pos) in listitem.iterlinks():
                #self.log.debug("Evaluate URL: + " + str(link) + " in element " + str(element))
                if re.search(self.config["findDownloadLink"],link):
                    self.log.debug("Download URL found: + "+link)
                    return Subtitle(episode.serie, episode.season, episode.episode, link)
    
#    def getLanguage(self,language,languageKeys):
#        return languageKeys[language]
#                      