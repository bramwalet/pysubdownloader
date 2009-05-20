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
        
    def  printSubtitle(self):
        return "Subtitle for serie: " + self.serie +  " Season: " + self.season + " Episode: " + self.episode
        
    def getSerie(self):
        return self.serie
    
    def getSeason(self):
        return self.season
    
    def getEpisode(self):
        return self.episode

    def getLink(self):
        return self.link
       
    def isDoubleEpisode(self):
        # TODO: this should also be implemented at Episode
        return re.match('-', self.episode)
   