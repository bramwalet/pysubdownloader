'''
Created on 18 mei 2009

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
