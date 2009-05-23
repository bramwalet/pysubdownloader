'''
Created on 18 mei 2009

@author: Bram Walet
'''
from sites.AbstractHtmlSite import AbstractHtmlSite


class PodnapisiSite(AbstractHtmlSite):
    '''
    classdocs
    '''
        
    def setUp(self):
        supportedLanguages = ("en", "es", "fr", "de", "br", "ru", "ua", "it", "gr", "ar","hu", "pl","tr")
        config = { "siteName" : "Podnapisi",
                   "findTableString" : 'list',
                   "findDownloadLink" : 'download',
                   "baseUrl" : "http://simple.podnapisi.net/ppodnapisi/",
                   "searchUrl" : "http://simple.podnapisi.net/ppodnapisi/search?" }
        return (config,supportedLanguages)
    
    def getKeys(self,episode):
        languageKeys = {"en":"2","es":"28","fr":"8","nl":"23","de":"5"}
        searchKeys = {"tbsl":"3", #tab 3 is tv series
                "asdp":"1", #advanced search on 
                "sK": episode.serie, #series name
                "sJ": languageKeys[self.language], #language searched for 
                "sO":"desc", #sorting
                "sS":"time", #sorting
                "submit":"Search", #button
                "sTS": str(episode.season), #season
                "sTE": str(episode.episode), #episode number
                "sY": str(episode.year),  # series year
                "sR":"",  # release
                "sT":"1"} #
        return searchKeys
    
      
      


       