'''
Created on 24 apr 2010

@author: b.walet
'''
from handlers.UrlHandler import UrlHandler
import urllib
from xml.etree.ElementTree import ElementTree

class BierdopjeAPI(object):
    '''
    classdocs
    '''


    def __init__(self, urlhandler, apikey):
        '''
        Constructor
        '''
        self.uh = UrlHandler(self.logfile, self.debug)
        self.apiurl = "http://api.bierdopje.com/"
        self.apikey = apikey
        
    def call_api(self, command, params=None):
        url = self.apiurl + self.apikey + "/" + command 
        if params is not None:
            for param in params:
                url = url + "/" + urllib.quote_plus(param)
        
        response = self.uh.executeRequest(url)
        try:
            xml = ElementTree.parse(response)
            status = self.gettextelements(xml, "response/status")
        except:
            return None
        
        if status == "false":
            return None
        else:
            return xml    


        
    def GetShowById(self, bierdopjeSerieId): pass
    
    def GetShowByTVDBID(self, tvdbId): pass
    
    def FindShowByName(self, name): 
        response = self.call_api("FindShowByName",name)

    
    def GetAllEpisodesForShow(self, bierdopjeSerieId): pass
    
    def GetEpisodeById(self, episodeId): pass
    
    def GetAllSubsForEpisode(self, episodeId, language): pass
        
    def gettextelements(self,xml, path):
        textelements = []
        try:
            elements = xml.findall(path)
        except:
            return
        for element in elements:
            textelements.append(element.text)
        return textelements

