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
from sites.components.download import AbstractDownloadComponent
from lxml.html import fromstring
import logging


class HttpDownloadComponent(AbstractDownloadComponent):
    '''
    classdocs
    '''
    def __init__(self):
        self.log = logging.getLogger("PySubDownloader." + self.__class__.__name__)

    def downloadSubtitle(self, sub, episode):
        downloadurl = sub.getLink()
        self.downloadSubtitleInternal(sub, episode, downloadurl)
   
    def downloadSubtitleInternal(self, sub, episode, downloadurl):
        self.log.debug("Trying to download subtitle id: " + sub.getLink() + " for episode: " + episode.printEpisode())
        (content, subtype) = self.getContent(downloadurl)
        if (subtype == "zip") & (self.fileHandler.isZipFile(content)):
            self.handleZipFile(episode, downloadurl, content)
        elif (subtype == "html"):
            self.handleHtmlPage(sub, episode, downloadurl, content)
        elif (subtype == "octet-stream"):
            self.handleSrtFile(episode, content)
        else:
            self.log.error("Unknown file type: " + subtype)

    def getContent(self, downloadurl):
        (filein, subtype) = self.urlHandler.executeRequest(downloadurl)
        content = filein.read()
        return content, subtype

    def handleZipFile(self, episode, downloadurl, content):
        self.log.debug("Content is zip file")
        archive = self.fileHandler.openZipFile(content)
        if archive is None:
            self.log.warn("Download failed for " + downloadurl)
        elif self.fileHandler.extractZipFile(episode, archive, content):
            self.log.info("Extracted subtitle for: " + episode.printEpisode())

    def handleHtmlPage(self, sub, episode, downloadurl, content):
        self.log.debug("Content is HTML page, search for download link")
        doc = fromstring(content)
        doc.make_links_absolute(downloadurl)
        links = doc.iterlinks()
        for element, attribute, link, pos in links:
            if ((link.find(sub.getId()) > 0) & (link.find("download") > 0)):
                self.log.debug("Found link with ID and DOWNLOAD: " + link)
                self.downloadSubtitleInternal(sub, episode, link)

    def handleSrtFile(self, episode, content):
        self.log.debug("Content is srt, download and extract.")
        self.fileHandler.writeSrtFile(episode, content)

