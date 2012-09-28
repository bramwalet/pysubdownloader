'''
Created on 29 april 2010

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

from sites.components.search import AbstractSearchComponent
import logging

class ApiSearchComponent(AbstractSearchComponent):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.log = logging.getLogger("PySubDownloader." + self.__class__.__name__)

    def search(self, episodes, language): 
        downloadList = []
        for episode in episodes:
            downloadListItem = self.wrapper.search(episode,language)
            if downloadListItem is not None:
                downloadList.append(downloadListItem)
        self.log.info("Found " + str(len(downloadList)) + " sub(s) to download")       
        return downloadList
