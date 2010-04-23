#'''
#Created on 24 mei 2009
#
#Copyright 2009 Bram Walet
#
#This file is part of PySubDownloader.
#
#PySubDownloader is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#PySubDownloader is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with PySubDownloader.  If not, see <http://www.gnu.org/licenses/>.
#
#@author: Bram Walet
#'''
## external imports
#from lxml.html import fromstring
#from lxml import html
#import urllib, re
#
## internal imports
#from handlers.FileHandler import FileHandler
#from handlers.UrlHandler import UrlHandler
#from classes.Subtitle import Subtitle
#from sites.components.search.AbstractSearchComponent import AbstractSearchComponent
#
#class HtmlSearchComponent(AbstractSearchComponent):
#    '''
#    classdocs
#    '''
#
#    def setupHandlers(self):
#        #self.fh = FileHandler(self.logfile,self.debug)
#        self.uh = UrlHandler(self.logfile,self.debug)
#    
#    def search(self, episodes,language):
#        self.language = language
#        self.log.info("Search for each episode.")
#        downloadList = []
#        for episode in episodes:
#            self.log.info("Search for " + episode.printEpisode())
#            searchUrl = self.createSearchQuery(episode)
#            sub = self.searchEpisode(episode,searchUrl)
#            if sub != None:
#                self.log.info("Match found for episode: " + episode.printEpisode())
#                downloadListItem = (sub,episode)
#                downloadList.append(downloadListItem)
#                
#        return downloadList
#     
#    def checkConfig(self,config):
#        requiredKeys = ('findTableString','findDownloadLink','searchUrl')
#        super(AbstractSearchComponent,self).checkConfigByKeys(config,requiredKeys)
#              
#    def createSearchQuery(self,episode): 
#        searchKeys = self.getKeys(episode)
#        searchUrl = self.config["searchUrl"]
#        searchQueryUrl = searchUrl + urllib.urlencode(searchKeys)
#        self.log.debug("Search URL: " + searchQueryUrl)
#        return searchQueryUrl
#
#    
#   
#    def searchEpisode(self,episode,searchUrl):
#        self.uh.installUrlHandler()
#        response = self.uh.executeRequest(searchUrl)
#        html = response.read()
#        #self.log.debug(html)
#        doc = fromstring(html)
#        doc.make_links_absolute(searchUrl,self.config["baseUrl"])
#        list = doc.find_class(self.config["findTableString"])
#      #  self.log.debug(str(list))
#        for listitem in list:
#       #     self.log.debug(listitem.text_content())
#            for (element, attribute, link, pos) in listitem.iterlinks():
#                #self.log.debug("Evaluate URL: + " + str(link) + " in element " + str(element))
#                if re.search(self.config["findDownloadLink"],link):
#                    self.log.debug("Download URL found: + "+link)
#                    return Subtitle(episode.serie, episode.season, episode.episode, link, '1')
#    
#    def getKeys(self,episode):
#        languageKeys = {"en":"2","es":"28","fr":"8","nl":"23","de":"5"}
#        searchKeys = {"tbsl":"3", #tab 3 is tv series
#                "asdp":"1", #advanced search on 
#                "sK": episode.serie, #series name
#                "sJ": languageKeys[self.language], #language searched for 
#                "sO":"desc", #sorting
#                "sS":"time", #sorting
#                "submit":"Search", #button
#                "sTS": str(episode.season), #season
#                "sTE": str(episode.episode), #episode number
#                "sY": str(episode.year),  # series year
#                "sR":"",  # release
#                "sT":"1"} #
#        return searchKeys
#    
