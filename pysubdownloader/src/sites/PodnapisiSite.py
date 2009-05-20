'''
Created on 18 mei 2009

@author: Bram Walet
'''
from sites.AbstractSubtitleSite import AbstractSubtitleSite
from handlers.UrlHandler import UrlHandler
from lxml.html import parse
import StringIO


class PodnapisiSite(AbstractSubtitleSite):
    '''
    classdocs
    '''
    def __init__(self):
      
       self.uh = UrlHandler()

    def search(self, episodes):
        print "Search for each episode"
        for episode in episodes:
            episode.printEpisode()
            self.searchEpisode(episode)
        
        #return AbstractSubtitleSite.search(self, episodes)


    def downloadSubtitle(self, sub, episode):
        return AbstractSubtitleSite.downloadSubtitle(self, sub, episode)

    
    def searchEpisode(self,episode):
        baseUrl = "http://simple.podnapisi.net/ppodnapisi/search?"
        keys = ['tbsl=3',
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
        searchUrl = baseUrl + sep.join(keys)
        print searchUrl
        self.uh.installUrlHandler()
        response = self.uh.executeRequest(searchUrl)
        print response.read()
      
        result = parse(searchUrl)
        print(result)


       
