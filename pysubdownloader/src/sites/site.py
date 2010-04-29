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
import logging

class AbstractSubtitleSite(object):
    
    def __init__(self, siteName):
        self.siteName = siteName
        self.log = logging.getLogger("PySubDownloader." + self.siteName)
    
    def run(self, episodes,language):
        self.log.info("Start search on " + self.siteName)
        downloadList = self.searchComponent.search(episodes,language)
        if (downloadList != None) & (len(downloadList) > 0):
            self.log.info("Found " + str(len(downloadList)) + " subtitles on " + self.siteName)
            for downloadItem in downloadList:
                (sub,episode) = downloadItem
                self.downloadComponent.downloadSubtitle(sub,episode)
            
            self.log.info("Download of subtitles on " + self.siteName + " completed")
        else:
            self.log.info("No subtitles found on " + self.siteName)
    

       
 
    