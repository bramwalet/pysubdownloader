'''
Created on 30 mei 2009

@author: Bram Walet
'''

import xml.sax
import urllib, re

# internal imports
from handlers.FileHandler import FileHandler
from handlers.UrlHandler import UrlHandler
from classes.Subtitle import Subtitle
from sites.components.search.AbstractSearchComponent import AbstractSearchComponent
from parsers.XmlSubtitleListParser import XmlSubtitleListParser

class XmlSearchComponent(AbstractSearchComponent):
    '''
    classdocs
    '''

    def setupHandlers(self):
        #self.fh = FileHandler(self.logfile,self.debug)
        self.uh = UrlHandler(self.logfile,self.debug)
    
    def search(self, episodes,language):
        self.language = language
        self.log.info("Search for each episode.")
        downloadList = []
        for episode in episodes:
            self.log.info("Search for " + episode.printEpisode())
            searchUrl = self.createSearchQuery(episode)
            sub = self.searchEpisode(episode,searchUrl)
            if sub != None:
                self.log.info("Match found for episode: " + episode.printEpisode())
                downloadListItem = (sub,episode)
                downloadList.append(downloadListItem)
                
        return downloadList
     
    def checkConfig(self,config):
        requiredKeys = ('findTableString','findDownloadLink','searchUrl')
        super(AbstractSearchComponent,self).checkConfigByKeys(config,requiredKeys)
              
    def createSearchQuery(self,episode): 
        searchKeys = self.getKeys(episode)
        searchUrl = self.config["searchUrl"]
        searchQueryUrl = searchUrl + urllib.urlencode(searchKeys)
        self.log.debug("Search URL: " + searchQueryUrl)
        return searchQueryUrl

    
   
    def searchEpisode(self,episode,searchUrl):
        self.uh.installUrlHandler()
        response = self.uh.executeRequest(searchUrl)
        parser = xml.sax.make_parser() 
        subhandler = XmlSubtitleListParser("subtitle")
        parser.setContentHandler(subhandler)
        list = parser.parse(response)
        
#        html = response.read()
#        #self.log.debug(html)
#        doc = fromstring(html)
#        doc.make_links_absolute(searchUrl,self.config["baseUrl"])
#        list = doc.find_class(self.config["findTableString"])
#        
#        
      #  self.log.debug(str(list))
        if list is not None:
            for listitem in list:
           #     self.log.debug(listitem.text_content())
                for (element, attribute, link, pos) in listitem.iterlinks():
                    #self.log.debug("Evaluate URL: + " + str(link) + " in element " + str(element))
                    if re.search(self.config["findDownloadLink"],link):
                        self.log.debug("Download URL found: + "+link)
                        return Subtitle(episode.serie, episode.season, episode.episode, link)
        
    def getKeys(self,episode):
        languageKeys = {"en":"2","es":"28","fr":"8","nl":"23","de":"5"}
        searchKeys = {"tbsl":"3", #tab 3 is tv series
                "asdp":"1", #advanced search on 
                "sK": episode.serie, #series name
                "sJ": languageKeys[self.language], #language searched for 
                "sO":"desc", #sorting
                "sS":"time", #sorting
                "submit":"Search", #button
                "sTS": str(episode.season), #season
                "sTE": str(episode.episode), #episode number
                "sY": str(episode.year),  # series year
                "sR":"",  # release
                "sT":"1",
                "sXML":"1"} #
        return searchKeys
    