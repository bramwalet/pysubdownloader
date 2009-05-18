'''
Created on 18 mei 2009

@author: Bram Walet
'''
from handlers.FileHandler import FileHandler
from handlers.UrlHandler import UrlHandler
from lib.FilenameParser import FilenameParser
from lib.RssFeedParser import RssFeedParser
from classes.Subtitle import Subtitle
from sites.AbstractSubtitleSite import AbstractSubtitleSite

class TvSubtitleSite(AbstractSubtitleSite):
    '''
    classdocs
    '''
    def __init__(self):
        self.uh = UrlHandler()
        self.fh = FileHandler()
        self.fparser = FilenameParser()
        self.rssFeed = "http://www.tvsubtitles.net/rssen.xml"
        
        self.rssparser = RssFeedParser(self.rssFeed)
        self.baseUrl = "http://www.tvsubtitles.net/"
        
    def search(self,episodes):
         print "[search] parseRss"
         
         availableSubs = self.rssparser.parse()
         for aSub in availableSubs: 
            #print "[search] iterate aSub"
            #aSub.printSubtitle()
            for episode in episodes:
                #print "[search] iterate episode"
                #episode.printEpisode()
                if episode.appropriateSub(aSub):
                    print "[search] match found"
                    self.downloadSubtitle(aSub, episode)
              
 

        
    
    

    def downloadSubtitle(self,sub,episode):
        fh = FileHandler()
        uh = UrlHandler()
        downloadurl = self.baseUrl + "download-" + sub.getId() + ".html"
        uh.installUrlHandler()
        filein = uh.executeRequest(downloadurl)
        archive = fh.openZipFile(filein) 
        if fh.extractZipFile(episode, archive):
            print "extracted subtitle"
        