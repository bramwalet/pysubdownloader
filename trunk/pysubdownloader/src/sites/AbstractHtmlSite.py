'''
Created on 20 mei 2009
Copyright 2009 Bram Walet

This file is part of PySubDownloader.

PySubDownloader is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

PySubDownloader is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with PySubDownloader.  If not, see <http://www.gnu.org/licenses/>.

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
        self.fh = FileHandler(self.logfile,self.debug)
        self.uh = UrlHandler(self.logfile,self.debug)
    
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
