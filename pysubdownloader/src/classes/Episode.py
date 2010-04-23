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
import os.path, logging
from lib.LoggerFactory import LoggerFactory

class Episode(object):
    '''
    classdocs
    '''

    def __init__(self, serie, year, season, episode, path, fileName):
        '''
        Constructor
        '''
        self.serie = serie
        self.year = year
        self.season = int(season)
        episodes = episode.split('-')
        self.episode =  int(episodes[0])
        self.path = path
        self.fileName = fileName

    def getSerie(self):
        return self.__serie


    def getYear(self):
        return self.__year


    def getSeason(self):
        return self.__season


    def getEpisode(self):
        return self.__episode


    def getPath(self):
        return self.__path


    def getFileName(self):
        return self.__fileName


    def setSerie(self, value):
        self.__serie = value


    def setYear(self, value):
        self.__year = value


    def setSeason(self, value):
        self.__season = value


    def setEpisode(self, value):
        self.__episode = value


    def setPath(self, value):
        self.__path = value


    def setFileName(self, value):
        self.__fileName = value


    def delSerie(self):
        del self.__serie


    def delYear(self):
        del self.__year


    def delSeason(self):
        del self.__season


    def delEpisode(self):
        del self.__episode


    def delPath(self):
        del self.__path


    def delFileName(self):
        del self.__fileName



    def printEpisode(self):
        return "serie: " + self.serie + " Season: " + str(self.season) + " Episode: " + str(self.episode)
        
    def appropriateSub(self,sub):
  
        if self.serie != sub.getSerie():
            return False
        if self.season != int(sub.getSeason()):
            return False
        if self.episode != int(sub.getEpisode()):
            return False   
        if sub.isDoubleEpisode():
            #self.log.error("Double episodes not supported")
            return False         
        
        return True
    
    def generateSrtFilename(self):
        (fileBaseName,fileExt) = os.path.splitext(self.fileName)
        return os.path.join(self.path , fileBaseName + ".srt")
    
    def isDoubleEpisode(self):
        # TODO: Implement
        return True

    _serie = property(getSerie, setSerie, delSerie, "Serie's Docstring")

    _year = property(getYear, setYear, delYear, "Year's Docstring")

    _season = property(getSeason, setSeason, delSeason, "Season's Docstring")

    _episode = property(getEpisode, setEpisode, delEpisode, "Episode's Docstring")

    _path = property(getPath, setPath, delPath, "Path's Docstring")

    _fileName = property(getFileName, setFileName, delFileName, "FileName's Docstring")
