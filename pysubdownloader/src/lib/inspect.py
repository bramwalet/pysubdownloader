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
import logging
import time

class Inspector(object):
    
    def __init__(self):
        self.log = logging.getLogger("PySubDownloader." + self.__class__.__name__)
       
        
    def scan(self, path, maxdays):
        return self.findEpisodes(path, maxdays)
        
    def findEpisodes(self, path, maxdays):
        self.log.info("Scanning path: " + path)
        episodes = []
        unknownFiles = []
        for root, dirs, files in os.walk(path):
            self.log.debug("Walking path: %s",  root)
            for file in files:
                episodePath = os.path.join(root, file)
                if self.filenameParser.isMovie(file) & \
                    self.filenameParser.hasNoSrt(episodePath):
                    if self.recentlyAdded(episodePath, maxdays):

                        self.log.debug("Found movie file: " + file)
                        episode = self.filenameParser.parseFileName(file, episodePath)
                        if episode is not None:
                            self.log.debug("Determined episode: " + episode.printEpisode())
                            episodes.append(episode)
                        else:
                            self.log.warn("Cannot determine episode from file: " + file)
                            unknownFiles.append(file)
        self.log.info("Found %i episode(s) without subtitles.", len(episodes))
        self.log.info("Found %i unknown movie file(s).", len(unknownFiles))

        return episodes

    def recentlyAdded(self,episodePath, maxdays):
        modifDate = os.stat(episodePath).st_mtime
        self.log.debug("File %s modified on %d ", episodePath, modifDate)
        if modifDate < time.time() - int(maxdays) * 86400:
            return False
        else:
            self.log.debug("File %s is considered recent.", episodePath)
            return True

        
