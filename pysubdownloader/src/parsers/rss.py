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
from parsers.file import FilenameParser

class RssFeedParser(object):
    '''
    classdocs
    '''

    def __init__(self, filenameParser):
        self.filenameParser = filenameParser

        
    def parse(self,url, baseUrl):
        items = []
        feed = feedparser.parse(url)
        for feeditem in feed["items"]:
            sub = self.parseRssFeedItem(feeditem)
            if sub is not None:
                items.append(sub)
           
        return items
    
    

    def parseItemTitle(self, serietitle, words):
        seasonEpisodeStringFound = False
        seasonEpisodeString = None
        for word in words:
            ''' try to search for season - episode string in format #x# until it is found, the title is displayed
            '''
            SEASON_X_EPISODE_REGEXP = '[0]*([0-9]+)x[0]*([0-9]+)[^\\/]*'
            if re.match(SEASON_X_EPISODE_REGEXP, word):
                seasonEpisodeString = word
                seasonEpisodeStringFound = True
            ''' try to search for season - episode string in format S##E## until it is found, the title is displayed
            '''
            S_SEASON_E_EPISODE_REGEXP = '[sS][0]*([0-9]+)[eE][0]*([0-9]+)[^\\/]*'
            if re.match(S_SEASON_E_EPISODE_REGEXP, word):
                seasonEpisodeString = word
                seasonEpisodeStringFound = True
            if seasonEpisodeStringFound == False:
                if len(serietitle.strip()) == 0:
                    serietitle = word
                else:
                    serietitle = serietitle + " " + word
        
        return seasonEpisodeString, serietitle

    def parseRssFeedItem(self, feeditem):
        
        # TODO: implement better
        link = feeditem["link"]
        serietitle = ""
        title = feeditem["title"]
        # split using whitespace
        words = title.split()
        if len(words) == 1:
            # split using dots
            words = title.split(".")
        
        (seasonEpisodeString, serietitle) = self.parseItemTitle(serietitle, words)
                    
        if seasonEpisodeString is not None:
            (episode, season) = self.filenameParser.parseEpisodeString(seasonEpisodeString)
            id = self.getId(link)
            sub = Subtitle(serietitle, season, episode, link, id)
            return sub
        else:
            print "WARNING "
            return None;
   
    def getId(self, displayLink):
        # TODO: this should be in a parser, and should be fixed better
        rightIdx = displayLink.rfind('.')
        leftIdx = displayLink.find('-')
        id = displayLink[leftIdx + 1:rightIdx]
        return id
