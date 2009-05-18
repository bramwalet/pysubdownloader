'''
Created on 18 mei 2009

@author: Bram Walet
'''
import os
from lib.Parser import Parser

class Inspector(object):
    
    def __init__(self):
        self.parser = Parser()
        
    def scan(self,path):
        return self.findEpisodes(path)
        
    def findEpisodes(self, path):
        episodes = []
        for root, dirs, files in os.walk(path):
            for file in files:
                episodePath = os.path.join(root,file)
                if self.parser.isMovie(file) & self.parser.hasNoSrt(episodePath):
                    episodes.append(self.parser.parseFileName(file,episodePath))
        return episodes
    
    def getEpisodes(self):
        return self.episodes
    

        