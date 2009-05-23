'''
Created on 18 mei 2009

@author: Bram Walet
'''
import os.path, logging
from lib.LoggerFactory import LoggerFactory

class Episode(object):
    '''
    classdocs
    '''

    def __init__(self, serie, year, season, episode, path, fileName,logfile):
        '''
        Constructor
        '''
        self.serie = serie
        self.year = year
        self.season = season
        episodes = episode.split('-')
        self.episode =  int(episodes[0])
        self.path = path
        self.fileName = fileName
        lf = LoggerFactory("Episode",logfile)
        self.log = lf.getLogger()

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



    def getEpisode(self):
        return self.__episode
        
    def printEpisode(self):
        return "serie: " + self.serie + " Season: " + self.season + " Episode: " + str(self.episode)
        
    def appropriateSub(self,sub):
  
        if self.serie != sub.getSerie():
            return False
        if self.season != sub.getSeason():
            return False
        if self.episode != sub.getEpisode():
            return False   
        if sub.isDoubleEpisode():
            self.log.error("Double episodes not supported")
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


  