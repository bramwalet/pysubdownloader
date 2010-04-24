'''
Created on 30 mei 2009

@author: Bram Walet
'''

from xml.etree.ElementTree import fromstring, dump
import urllib

# internal imports
from handlers.UrlHandler import UrlHandler
from classes.Subtitle import Subtitle
from sites.components.search.AbstractSearchComponent import AbstractSearchComponent


class XmlSearchComponent(AbstractSearchComponent):
    '''
    classdocs
    '''

    def setupHandlers(self):
        self.uh = UrlHandler(self.logfile,self.debug)
    

    def searchEpisode(self, episode):
        self.log.debug("Search for " + episode.printEpisode())
        searchUrl = self.createSearchQuery(episode)
        sub = self.searchEpisodeSub(episode, searchUrl)
        if sub != None:
            self.log.info("Match found for episode: " + episode.printEpisode())
            downloadListItem = sub, episode
            return downloadListItem
        return None

    def search(self, episodes,language):
        self.language = language
        self.log.info("Search for each episode.")
        downloadList = []
        for episode in episodes:
            downloadListItem = self.searchEpisode(episode)
            if downloadListItem is not None:
                downloadList.append(downloadListItem)
        self.log.info("Found " + str(len(downloadList)) + " sub(s) to download")       
        return downloadList
     
#    def checkConfig(self,config):
#        requiredKeys = ('findTableString','findDownloadLink','searchUrl')
#        super(AbstractSearchComponent,self).checkConfigByKeys(config,requiredKeys)
#              
    def createSearchQuery(self,episode): 
        searchKeys = self.getKeys(episode)
        searchUrl = self.config["searchUrl"]
        searchQueryUrl = searchUrl + urllib.urlencode(searchKeys)
        self.log.debug("Search URL: " + searchQueryUrl)
        return searchQueryUrl

    
   

    def handleChildElement(self, child, searchTag):
        value = None
        if child.tag == searchTag:
            value = child.text
            self.log.debug(searchTag + " element: " + value)
        return value

    def searchEpisodeSub(self,episode,searchUrl):
        self.uh.installUrlHandler()
        (response,subtype) = self.uh.executeRequest(searchUrl)
        xml = fromstring(response.read())
        self.log.debug("Response: " + str(xml))
        subtitle = xml.find("subtitle")
        if subtitle is not None:
            self.log.debug("Subtitle element: " + str(subtitle))
            children = subtitle.getchildren()
            for child in children: 
                foundTitle = self.handleChildElement(child, "title")
                if foundTitle is not None:
                    title = foundTitle    
                foundSeason = self.handleChildElement(child, "tvSeason")
                if foundSeason is not None:
                    season = foundSeason    
                foundEpisode = self.handleChildElement(child, "tvEpisode")
                if foundEpisode is not None:
                    episode = foundEpisode    
                foundLink = self.handleChildElement(child, "url")
                if foundLink is not None:
                    link = foundLink    
                foundId = self.handleChildElement(child, "id")
                if foundId is not None:
                    id = foundId    
                
            return Subtitle(title,season, episode, link, id)
#       
#        
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
    