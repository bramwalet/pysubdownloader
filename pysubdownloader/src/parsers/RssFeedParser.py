'''
Created on 18 mei 2009
Copyright 2009 Bram Walet

This file is part of PySubDownloader.

PySubDownloader is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

PySubDownloader is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with PySubDownloader.  If not, see <http://www.gnu.org/licenses/>.

@author: Bram Walet
'''

import feedparser, re

from classes.Subtitle import Subtitle
from parsers.FilenameParser import FilenameParser

class RssFeedParser(object):
    '''
    classdocs
    '''


    def __init__(self,url,baseUrl,logfile,debug):
        '''
        Constructor
        '''
        self.url = url
        self.baseUrl = baseUrl
        self.logfile = logfile
        self.debug = debug
        self.parser = FilenameParser()
        
        
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
        id = self.getId(link)
        link = self.baseUrl + "download-" + id + ".html"
        sub = Subtitle(serietitle, season, episode, link, id)
        return sub
   
    def getId(self,displayLink):
        # TODO: this should be in a parser, and should be fixed better
        rightIdx = displayLink.rfind('.')
        leftIdx = displayLink.find('-')
        id = displayLink[leftIdx+1:rightIdx]
        return id