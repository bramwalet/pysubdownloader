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
         config =  { "siteName" : "TvSubtitles",
                     "rssFeed"  : "http://www.tvsubtitles.net/rssen.xml",
                     "baseUrl"  : "http://www.tvsubtitles.net/" }
         
         return config
 

        
    
    

 