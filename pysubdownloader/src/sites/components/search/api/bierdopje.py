'''
Created on 24 apr 2010

Copyright 2010 Bram Walet

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

@author: b.walet
'''
import urllib
import logging
from xml.etree import ElementTree
from classes.exceptions import ConfigException
from classes import Subtitle


class BierdopjeAPI(object):
    '''
    classdocs
    '''


    def __init__(self, apiurl, apikey):
        '''
        Constructor
        '''
        self.log = logging.getLogger("PySubDownloader.BierdopjeAPI")
        self.apiurl = apiurl
        self.apikey = apikey
        
    def __call_api__(self, command, params=None):
        if(self.apikey == "None"):
            raise ConfigException("API Key is unconfigured")
        
        self.log.debug("Calling API with command: " + command + " and parameters: " + str(params))
        url = self.apiurl + self.apikey + "/" + command 
        if params is not None:
            for param in params:
                url = url + "/" + urllib.quote_plus(param)
        
        (response, type) = self.urlHandler.executeRequest(url)
        try:
            xml = ElementTree.fromstring(response.read())
            status = self.gettextelements(xml, "response/status")
            self.log.debug("Status: " + str(status))
        except:
            return None
        
        if status == "false":
            return None
        else:
            self.log.debug("Response: " + str(xml))
            return xml    


        
    def GetShowByName(self, name):
        return self.__call_api__("GetShowByName", params=[name])
    
    def GetShowById(self, bierdopjeSerieId):
        return self.__call_api__("GetShowById", params=[str(bierdopjeSerieId)])
    
    def GetShowByTVDBID(self, tvdbId): 
        return self.__call_api__("GetShowByTVDBID", params=[str(tvdbId)])
 
    def FindShowByName(self, name): 
        return self.__call_api__("FindShowByName", params=[name])
    
    def GetAllEpisodesForShow(self, bierdopjeSerieId): 
        return self.__call_api__("GetAllEpisodesForShow", params=[str(bierdopjeSerieId)])

    def GetEpisodeById(self, episodeId): 
        return self.__call_api__("GetEpisodeById", params=[str(episodeId)])

    def GetAllSubsForEpisode(self, episodeId, language): 
        return self.__call_api__("GetAllSubsForEpisode", params=[str(episodeId), language])
        
    def GetAllSubsFor(self, showid, season, episode, language, istvdbid):    
        return self.__call_api__("GetAllSubsFor", params=[str(showid), str(season), str(episode), language, str(istvdbid)])

    def GetEpisodesForSeason(self, showid, season):      
        return self.__call_api__("GetEpisodesForSeason", params=[str(showid), str(season)])

    def GetSubsForSeason(self, showid, season, language):
        return self.__call_api__("GetSubsForSeason", params=[str(showid), str(season), language])
        
    def gettextelements(self, xml, path):
        textelements = []
        try:
            elements = xml.findall(path)
        except:
            return
        for element in elements:
            textelements.append(element.text)
        return textelements


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
            downloadlinks = self.api.gettextelements(responseSubs,"response/results/result/downloadlink")
            if len(downloadlinks)>0:
                sub = Subtitle(name, season, episode.getEpisode() , downloadlinks[0], None)
                return sub,episode # @TODO 
        else:
            self.log.warn("unable to determine show")
       