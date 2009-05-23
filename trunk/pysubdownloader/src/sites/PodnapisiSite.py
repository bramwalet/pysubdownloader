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
        searchKeys = ['tbsl=3',
                'asdp=0', 
                'sK='+ episode.serie,
                'sJ=' + languageKeys[self.language], 
                'sO=desc',
                'sS=time',
                'submit=Search', 
                'sTS=' + episode.season,
                'sTE=' + str(episode.episode),
                'sY=' + episode.year, 
                'sR', 
                'sT=1']
        sep = '&'
        return (searchKeys,sep)
    
      
      


       
