'''
Created on 24 mei 2009

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
from sites.components.search.AbstractSearchComponent import \
    AbstractSearchComponent
from lib.LoggerFactory import LoggerFactory

class RssSearchComponent(AbstractSearchComponent):
    '''
    classdocs
    '''

    def __init__(self,filenameParser, rssFeedParser):
        self.fparser = filenameParser
        self.rssparser = rssFeedParser
        self.log = LoggerFactory.getLogger("RssSearchComponent")

        
    def checkConfig(self, config):
        requiredKeys = ('siteName', 'baseUrl', 'rssFeed')
        super(AbstractSearchComponent, self).checkConfig(config, requiredKeys)
    
    def search(self, episodes, language):
        self.language = language
        downloadList = []
        self.log.info("Search for new episodes on RSS feed.")
        rssFeedUrl = self.getRssFeedUrl(self.language)
        
        availableSubs = self.rssparser.parse(rssFeedUrl, self.config["baseUrl"])
        for aSub in availableSubs: 
            for episode in episodes:
                if episode.appropriateSub(aSub):
                    self.log.info("Match found for episode: " + episode.printEpisode())
                    downloadListItem = (aSub, episode)
                    downloadList.append(downloadListItem)
                    
        self.log.info("Found " + str(len(downloadList)) + " sub(s) to download")       
        return downloadList
                    
    def getRssFeedUrl(self, language):
        rssFeedUrl = self.config["rssFeed"]
        return rssFeedUrl       
     

         
