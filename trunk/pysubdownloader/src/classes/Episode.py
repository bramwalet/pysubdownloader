'''
Created on 18 mei 2009

@author: Bram Walet
'''
import os.path

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
        self.season = season
        self.episode = episode
        self.path = path
        self.fileName = fileName

    def getSerie(self):
        return self.serie


    def getSeason(self):
        return self.season


    def getEpisode(self):
        return int(self.episode)


    def getPath(self):
        return self.path


    def getFileName(self):
        return self.fileName
    
    def getYear(self):
        return self.year

                
    def __iter__(self):
        return self;
    
        
    def printEpisode(self):
        print "Serie: " + self.serie + " Season: " + self.season + " Episode: " + self.episode
        
    def appropriateSub(self,sub):
  
        if self.serie != sub.getSerie():
            return False
        if self.season != sub.getSeason():
            return False
        if self.episode != sub.getEpisode():
            return False   
        if sub.isDoubleEpisode():
            print "double episodes not supported"
            return False         
        
        return True
    
    def generateSrtFilename(self):
        (fileBaseName,fileExt) = os.path.splitext(self.fileName)
        return os.path.join(self.path , fileBaseName + ".srt")
    
    def isDoubleEpisode(self):
        # TODO: Implement
        return True
    
   