'''
Created on 24 apr 2010

@author: b.walet
'''
from sites.components.search.api.bierdopje import BierdopjeAPI
import logging
from xml.etree.ElementTree import dump
from Subtitle import Subtitle

class BierdopjeWrapper(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.log = logging.getLogger("PySubDownloader.BierdopjeWrapper")

        
    def search(self,episode,language): 
        season = episode.getSeason()
        name = episode.getSerie()
        responseShows = self.api.GetShowByName(name)
        showids = self.api.gettextelements(responseShows,"response/showid")
        if len(showids) == 1:
            showid = showids[0]
            responseSubs = self.api.GetAllSubsFor(showid, season, episode.getEpisode(), language, False)
            dump(responseSubs)
            downloadlinks = self.api.gettextelements(responseSubs,"response/results/result/downloadlink")
            if len(downloadlinks)>0:
                sub = Subtitle(name, season, episode.getEpisode() , downloadlinks[0], None)
                return sub,episode # @TODO 
        else:
            self.log.warn("unable to determine show")
        ## extract show id
       
        ## filter relevant episode
      
        
        