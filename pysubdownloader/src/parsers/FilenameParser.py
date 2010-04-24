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
import os.path,re,logging
from classes.Episode import Episode
from lib.LoggerFactory import LoggerFactory

class FilenameParser(object):
    '''
    classdocs
    '''
    ''' this class parses a filename based on a Serie (Year) - EpisodeString - Description syntax where Year is optional
    '''
       

    def determineSerieYear(self, serieName):
        pattern = '\([0-9]{4}\)'
        if re.search(pattern, serieName):
            years = re.findall(pattern, serieName)
            year = years[0]
        else:
            year = ""
        return year


    def determineSeasonEpisode(self, list):
        seasonEpisodeString = list[1]
        episode, season = self.parseEpisodeString(seasonEpisodeString)
        return episode, season


    def removeYearFromEpisodeName(self, serieName, year):
        serieName = serieName.replace(year, "")
        serieName = serieName.strip()
        return serieName

    def parseFileName(self,file,path):
        (dirName, fileName) = os.path.split(path)
        (fileBaseName, fileExtension) = os.path.splitext(fileName)
        list = fileBaseName.split(" - ")
        if len(list) < 2:
            return None;
        else: 
            serieName = str(list[0])
            year = self.determineSerieYear(serieName) 
            serieName = self.removeYearFromEpisodeName(serieName, year)
            (episode,season) = self.determineSeasonEpisode(list)
            e = Episode(serieName, year, season, episode, dirName, fileName)
            return e
    
    def parseEpisodeString(self,seasonEpisodeString):
        if re.search("x",seasonEpisodeString):
            (season, episode) = seasonEpisodeString.split("x", 2)
            return episode, season
        if re.search("S[0-9]{2}E[0-9]{2}",seasonEpisodeString):
            matches = re.match("S([0-9]{1,2})E([0-9]{1,2})",seasonEpisodeString)
            season = matches.group(1)
            episode = matches.group(2)
            return episode, season

    def isMovie(self,filename):
        (fileBaseName, fileExtension) = os.path.splitext(filename)
        allowedExt = ('.avi','.mkv', '.wmv')
        if fileExtension in allowedExt:
            return True
        else:
            return False
        
    def hasNoSrt(self,path):
        (fileBaseName, fileExtension) = os.path.splitext(path)
        allowedExt = '.srt'
        srtPath = fileBaseName + allowedExt
        
        if os.path.exists(srtPath): 
            return False
        else:
            return True
        
