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
from lxml.html import fromstring


class HttpDownloadComponent(AbstractDownloadComponent):
    '''
    classdocs
    '''
    def setupHandlers(self):
        self.fh = FileHandler(self.logfile,self.debug)
        self.uh = UrlHandler(self.logfile,self.debug)
    

    def getContent(self, downloadurl):
        (filein,subtype) = self.uh.executeRequest(downloadurl)
        content = filein.read()
        return content, subtype


    def downloadSubtitleInternal(self, sub, episode, downloadurl):
        self.log.info("Trying to download subtitle id: " + sub.getId() + " for episode: " + episode.printEpisode())
        (content,subtype) = self.getContent(downloadurl)
        if (subtype == "zip") & (self.fh.isZipFile(content)):
            self.log.info("Content is zip file")
            archive = self.fh.openZipFile(content)
            if archive is None:
                self.log.warn("Download failed for " + downloadurl)
            elif self.fh.extractZipFile(episode, archive):
                self.log.info("Extracted subtitle")
        if (subtype == "html"):
            self.log.info("Content is HTML page, search for download link")
            doc = fromstring(content)
            doc.make_links_absolute(downloadurl)
            links = doc.iterlinks()
            for element, attribute, link, pos in links:
                if ((link.find(sub.getId()) > 0) & (link.find("download") > 0)):
                    self.log.info("Found link with ID and DOWNLOAD: " + link)
                    self.downloadSubtitleInternal(sub,episode,link)

    def downloadSubtitle(self,sub,episode):
        downloadurl = sub.getLink()
        self.uh.installUrlHandler()
        self.downloadSubtitleInternal(sub, episode, downloadurl)
                    
            
    def checkConfig(self,config):
        requiredKeys = ('siteName')
        super(self).checkConfig(config,requiredKeys)