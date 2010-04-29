'''
Created on 30 mei 2009

@author: Bram Walet
'''

from classes.Subtitle import Subtitle
from sites.components.search.AbstractSearchComponent import \
    AbstractSearchComponent
from lxml.etree import fromstring
import urllib
import logging

# internal imports


class XmlSearchComponent(AbstractSearchComponent):
    '''
    classdocs
    '''
    def __init__(self):
        self.log = logging.getLogger("PySubDownloader." + self.__class__.__name__)

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
        
    def searchEpisode(self, episode):
        self.log.debug("Search for " + episode.printEpisode())
        searchUrl = self.createSearchQuery( episode)
        sub = self.searchEpisodeSub(episode, searchUrl)
        if sub != None:
            self.log.info("Match found for episode: " + episode.printEpisode())
            downloadListItem = sub, episode
            return downloadListItem
        return None
            
    def createSearchQuery(self, episode): 
        searchKeys = self.getKeys(episode)
        searchUrl = self.searchUrl
        searchQueryUrl = searchUrl + urllib.urlencode(searchKeys)
        self.log.debug("Search URL: " + searchQueryUrl)
        return searchQueryUrl


    #@TODO this MUST be outside this class.
    def getKeys(self,episode):
        searchKeys = {"tbsl":"3", #tab 3 is tv series
                "asdp":"1", #advanced search on 
                "sK": episode.getSerie(), #series name
                "sJ": self.languageKeys[self.language], #language searched for 
                "sO":"desc", #sorting
                "sS":"time", #sorting
                "submit":"Search", #button
                "sTS": str(episode.getSeason()), #season
                "sTE": str(episode.getEpisode()), #episode number
                "sY": str(episode.getYear()),  # series year
                "sR":"",  # release
                "sT":"1",
                "sXML":"1"} #
        return searchKeys

    def searchEpisodeSub(self,episode,searchUrl):
        (response,subtype) = self.urlHandler.executeRequest(searchUrl)
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
    
    def handleChildElement(self, child, searchTag):
        value = None
        if child.tag == searchTag:
            value = child.text
            self.log.debug(searchTag + " element: " + value)
        return value

  
      

    