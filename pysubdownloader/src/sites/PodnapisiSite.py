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
        config = { "siteName" : "Podnapisi",
                   "findTableString" : 'a',
                   "findDownloadLink" : 'download',
                   "baseUrl" : "http://simple.podnapisi.net/ppodnapisi/",
                   "searchUrl" : "http://simple.podnapisi.net/ppodnapisi/search?" }
        return config
    
    def getKeys(self,episode):
        searchKeys = ['tbsl=3',
                'asdp=1', 
                'sK='+ episode.getSerie(),
                'sJ=' + '2', 
                'sO=desc',
                'sS=time',
                'submit=Search', 
                'sTS=' + episode.getSeason(),
                'sTE=' + str(episode.getEpisode()),
                'sY=' + episode.getYear(), 
                'sR', 
                'sT=1']
        sep = '&'
        return (searchKeys,sep)
       
    
      


       
