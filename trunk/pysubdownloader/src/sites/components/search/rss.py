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
import logging

class RssSearchComponent(AbstractSearchComponent):
    '''
    classdocs
    '''

    def __init__(self):
        self.log = logging.getLogger("PySubDownloader." + self.__class__.__name__)
  
    def search(self, episodes, language):
        downloadList = []
        self.log.info("Search for new episodes on RSS feed.")
        rssFeedUrl = self.getRssFeedUrl(language)
        availableSubs = self.rssFeedParser.parse(rssFeedUrl)
        for aSub in availableSubs: 
            for episode in episodes:
                if episode.appropriateSub(aSub):
                    self.log.info("Match found for episode: " + episode.printEpisode())
                    downloadListItem = (aSub, episode)
                    downloadList.append(downloadListItem)
                    
        self.log.info("Found " + str(len(downloadList)) + " sub(s) to download")       
        return downloadList
                    
    def getRssFeedUrl(self, language):     
        rssFeedUrl = self.rssFeedUrlByLanguage[language]
        return rssFeedUrl       
     

         
