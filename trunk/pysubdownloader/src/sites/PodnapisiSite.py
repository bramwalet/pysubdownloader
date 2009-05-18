'''
Created on 18 mei 2009

@author: Bram Walet
'''
from sites.AbstractSubtitleSite import AbstractSubtitleSite

class PodnapisiSite(AbstractSubtitleSite):
    '''
    classdocs
    '''
    def __init__(selfparams):
      
        self.uh = UrlHandler()

    def search(self, episodes):
        return AbstractSubtitleSite.search(self, episodes)


    def downloadSubtitle(self, sub, episode):
        return AbstractSubtitleSite.downloadSubtitle(self, sub, episode)

        