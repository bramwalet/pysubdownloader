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
import os
from parsers.FilenameParser import FilenameParser
from lib.LoggerFactory import LoggerFactory

class Inspector(object):
    
    def __init__(self,  logfile, debug):
        self.parser = FilenameParser()
        self.setupLogging(logfile, debug)
       
        
    def scan(self,path):
        return self.findEpisodes(path)
        
    def findEpisodes(self, path):
        episodes = []
        for root, dirs, files in os.walk(path):
            for file in files:
                episodePath = os.path.join(root,file)
                if self.parser.isMovie(file) & self.parser.hasNoSrt(episodePath):
                    self.log.info("Found movie file: " + file)
                    episode = self.parser.parseFileName(file, episodePath)
                    if episode is not None:
                        self.log.info("Determined episode: " + episode.printEpisode())
                        episodes.append(episode)
        return episodes
    
    def getEpisodes(self):
        return self.episodes
    
    def setupLogging(self, logfile, debug):
        lf = LoggerFactory("Inspector",logfile,debug)
        self.logfile = logfile
        self.log = lf.getLogger()

        