'''
Created on 21 mei 2009

@author: Bram Walet
'''
from sites.AbstractHtmlSite import AbstractHtmlSite

class TvSubsSite(AbstractHtmlSite):
    '''
    classdocs
    '''
# &setlang1=en
    def setUp(self):
        supportedLanguages = ("en", "es", "fr", "de", "br", "ru", "ua", "it", "gr", "ar","hu", "pl","tr")
        config = { "siteName" : "TvSubs",
                   "findTableString" : 'cont',
                   "findDownloadLink" : 'subtitle',
                   "baseUrl" : "http://www.tvsubs.net/",
                   "searchUrl" : "http://www.tvsubs.net/new.html" }
        return (config,supportedLanguages)
    
    def getKeys(self,episode):
        languageKeys = {"en":"en"}
        searchKeys = ['setlang1=' + languageKeys[self.language]]
        sep = '&'
        return (searchKeys,sep)
    
      