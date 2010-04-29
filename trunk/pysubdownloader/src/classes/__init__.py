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
import os.path
import re

class Episode(object):
    '''
    classdocs
    '''

    def __init__(self, serie, year, season, episode, path, fileName):
        '''
        Constructor
        '''
        self.__serie = serie
        self.__year = year
        self.__season = int(season)
        episodes = episode.split('-')
        self.__episode = int(episodes[0])
        self.__path = path
        self.__fileName = fileName

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
        return "serie: " + self.getSerie() + " Season: " + str(self.getSeason()) + " Episode: " + str(self.getEpisode())
        
    def appropriateSub(self, sub):
  
        if self.__serie != sub.getSerie():
            return False
        if self.__season != int(sub.getSeason()):
            return False
        if self.__episode != int(sub.getEpisode()):
            return False   
        if sub.isDoubleEpisode():
            #self.log.error("Double episodes not supported")
            return False         
        
        return True
    

    def generateFilename(self, ext):
        fileBaseName, fileExt = os.path.splitext(self.getFileName())
        filename = os.path.join(self.getPath(), fileBaseName + ext)
        return filename

    def generateSrtFilename(self):
        return self.generateFilename(".srt")
    
    def generateZipFilename(self):
        return self.generateFilename(".zip")
       
    
    def isDoubleEpisode(self):
        # TODO: Implement
        return True

    _serie = property(getSerie, setSerie, delSerie, "Serie's Docstring")

    _year = property(getYear, setYear, delYear, "Year's Docstring")

    _season = property(getSeason, setSeason, delSeason, "Season's Docstring")

    _episode = property(getEpisode, setEpisode, delEpisode, "Episode's Docstring")

    _path = property(getPath, setPath, delPath, "Path's Docstring")

    _fileName = property(getFileName, setFileName, delFileName, "FileName's Docstring")


class Subtitle(object):
    
    def __init__(self, serie, season, episode, link, id):
    
        self.serie = serie
        self.season = season
        self.episode = episode
        self.link = link
        self.id = id
        

    def getSerie(self):
        return self._serie


    def getSeason(self):
        return self._season


    def getEpisode(self):
        return self._episode


    def getLink(self):
        return self._link

    def getId(self):
        return self._id
    
    def setSerie(self, value):
        self._serie = value


    def setSeason(self, value):
        self._season = value


    def setEpisode(self, value):
        self._episode = value


    def setLink(self, value):
        self._link = value

    def setId(self, value):
        self._id = value
        
    def delSerie(self):
        del self._serie


    def delSeason(self):
        del self._season


    def delEpisode(self):
        del self._episode


    def delLink(self):
        del self._link

    def delId(self):
        del self._id

    def printSubtitle(self):
        return "Subtitle for serie: " + self.serie +  " Season: " + self.season + " Episode: " + self.episode + " Id: " + id
   
    def isDoubleEpisode(self):
        # TODO: this should also be implemented at Episode
        return re.match('-', self.episode)

    serie = property(getSerie, setSerie, delSerie, "Serie's Docstring")

    season = property(getSeason, setSeason, delSeason, "Season's Docstring")

    episode = property(getEpisode, setEpisode, delEpisode, "Episode's Docstring")

    link = property(getLink, setLink, delLink, "Link's Docstring")
    
    id = property(getId, setId, delId, "Id's Docstring")
    
