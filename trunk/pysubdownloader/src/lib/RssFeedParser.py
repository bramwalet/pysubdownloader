'''
Created on 18 mei 2009

@author: Bram Walet
'''

import feedparser, re

from classes.Subtitle import Subtitle
from lib.FilenameParser import FilenameParser

class RssFeedParser(object):
    '''
    classdocs
    '''


    def __init__(self,url,baseUrl,logfile):
        '''
        Constructor
        '''
        self.url = url
        self.baseUrl = baseUrl
        self.parser = FilenameParser(logfile)
        
        
    def parse(self):
        items = []
        feed = feedparser.parse(self.url)
        for feeditem in feed["items"]:
            sub = self.parseRssFeedItem(feeditem)
            items.append(sub)
           
        return items
    
    
    def parseRssFeedItem(self, feeditem):
        
        # TODO: implement better
        link = feeditem["link"]
        serietitle = ""
        title = feeditem["title"]
        words = title.split()
        seasonEpisodeStringFound = False
        for word in words:
            ''' try to search for season - episode string in format #x# until it is found, the title is displayed
            ''' 
            if re.match('[0]*([0-9]+)x[0]*([0-9]+)[^\\/]*', word):
                seasonEpisodeString = word
                seasonEpisodeStringFound = True
            
            if seasonEpisodeStringFound == False:
                if len(serietitle.strip()) == 0:
                    serietitle = word
                else:
                    serietitle = serietitle + " " + word

        (episode, season) = self.parser.parseEpisodeString(seasonEpisodeString)
        link = self.baseUrl + "download-" + self.getId(link) + ".html"
        sub = Subtitle(serietitle, season, episode, link)
        return sub
   
    def getId(self,displayLink):
        # TODO: this should be in a parser, and should be fixed better
        rightIdx = displayLink.rfind('.')
        leftIdx = displayLink.find('-')
        id = displayLink[leftIdx+1:rightIdx]
        return id