'''
Created on 18 mei 2009

@author: Bram Walet
'''
from sites.AbstractRssSite import AbstractRssSite

class TvSubtitleSite(AbstractRssSite):
    '''
    classdocs
    '''
   
    def setUp(self):
         supportedLanguages = ("en", "es", "fr", "de", "br", "ru", "ua", "it", "gr", "ar","hu", "pl","tr")
         config =  { "siteName" : "TvSubtitles",
                     "rssFeed"  : "http://www.tvsubtitles.net/rss#lang#.xml",
                     "baseUrl"  : "http://www.tvsubtitles.net/" }
         
         return (config,supportedLanguages)
    
  
        
    
    

 