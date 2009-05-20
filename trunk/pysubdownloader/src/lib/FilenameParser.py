'''
Created on 18 mei 2009

@author: Bram Walet
'''
import os.path,re,logging
from classes.Episode import Episode
from lib.LoggerFactory import LoggerFactory

class FilenameParser(object):
    '''
    classdocs
    '''
    ''' this method parses a filename based on a Serie - EpisodeString - Description syntax
    '''
    def __init__(self):
        lf = LoggerFactory("FilenameParser")
        self.log = lf.getLogger()
       
    def parseFileName(self,file,path):
        (dirName, fileName) = os.path.split(path)
        (fileBaseName, fileExtension) = os.path.splitext(fileName)
        list = fileBaseName.split(" - ")
        serieName = str(list[0])
        pattern = '\([0-9]{4}\)'
        if re.search(pattern,serieName):
            self.log.debug("This serie has a year") 
            years = re.findall(pattern, serieName)
            year = years[0]
            serieName = serieName.replace(year, "")
            serieName =  serieName.strip()
        else:
            year = "" 
        #print fileBaseName
        seasonEpisodeString = list[1]
        (episode, season) = self.parseEpisodeString(seasonEpisodeString)
        e = Episode(serieName, year, season, episode, dirName, fileName)
        return e
    
    def parseEpisodeString(self,seasonEpisodeString):
        (season, episode) = seasonEpisodeString.split("x", 2)
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
        
