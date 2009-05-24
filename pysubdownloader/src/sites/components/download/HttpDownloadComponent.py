'''
Created on 24 mei 2009

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
# local imports
from handlers.FileHandler import FileHandler
from handlers.UrlHandler import UrlHandler
from sites.components.download.AbstractDownloadComponent import AbstractDownloadComponent

class HttpDownloadComponent(AbstractDownloadComponent):
    '''
    classdocs
    '''
    def setupHandlers(self):
        self.fh = FileHandler(self.logfile,self.debug)
        self.uh = UrlHandler(self.logfile,self.debug)
    
    def downloadSubtitle(self,sub,episode):
        downloadurl = sub.getLink()
        self.uh.installUrlHandler()
        filein = self.uh.executeRequest(downloadurl)
        archive = self.fh.openZipFile(filein) 
        if self.fh.extractZipFile(episode, archive):
            self.log.info("Extracted subtitle")
            
    def checkConfig(self,config):
        requiredKeys = ('siteName')
        super(AbstractHtmlSite,self).checkConfig(config,requiredKeys)
     
     
     