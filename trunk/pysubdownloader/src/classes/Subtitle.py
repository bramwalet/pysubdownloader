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
import re

class Subtitle(object):
    
    def __init__(self, serie, season, episode, link):
    
        self.serie = serie
        self.season = season
        self.episode = episode
        self.link = link

    def getSerie(self):
        return self._serie


    def getSeason(self):
        return self._season


    def getEpisode(self):
        return self._episode


    def getLink(self):
        return self._link


    def setSerie(self, value):
        self._serie = value


    def setSeason(self, value):
        self._season = value


    def setEpisode(self, value):
        self._episode = value


    def setLink(self, value):
        self._link = value


    def delSerie(self):
        del self._serie


    def delSeason(self):
        del self._season


    def delEpisode(self):
        del self._episode


    def delLink(self):
        del self._link


    def printSubtitle(self):
        return "Subtitle for serie: " + self.serie +  " Season: " + self.season + " Episode: " + self.episode
   
    def isDoubleEpisode(self):
        # TODO: this should also be implemented at Episode
        return re.match('-', self.episode)

    serie = property(getSerie, setSerie, delSerie, "Serie's Docstring")

    season = property(getSeason, setSeason, delSeason, "Season's Docstring")

    episode = property(getEpisode, setEpisode, delEpisode, "Episode's Docstring")

    link = property(getLink, setLink, delLink, "Link's Docstring")
