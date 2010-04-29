'''
Created on 24 apr 2010

@author: b.walet
'''
from sites.components.search.AbstractSearchComponent import AbstractSearchComponent
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


        