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
from lib.LoggerFactory import LoggerFactory

class AbstractSubtitleSite(object):
    
    def __init__(self,language,logfile,debug):
        self.language = language
         
        # assign class variables
        self.logfile = logfile
        self.debug = debug 
        self.language = language
        
        (search,download) = self.setUp(logfile,debug)
        
        languages = self.setupLanguages()
        #self.config = configGlobal
        
        configSearch = self.setupSearch()
        #search.checkConfig(config)
        self.sc = search
        self.dc = download        
        self.startLogger(self.getSiteName(),logfile,debug)
       
        self.sc.setConfig(configSearch)
        self.sc.setupHandlers()
        self.dc.setupHandlers()
    
    def run(self,episodes,language):
        downloadList = self.sc.search(episodes,language)
        if downloadList != None:
            for downloadItem in downloadList:
                (sub,episode) = downloadItem
                self.dc.downloadSubtitle(sub,episode)

    def startLogger(self,siteName,logfile,debug):
        
        lf = LoggerFactory(siteName,logfile,debug)
        self.logfile = logfile
        self.log = lf.getLogger()
        self.debug = debug
        self.sc.setLogger(self.log)
        self.dc.setLogger(self.log)
 
    def setUp(self,logfile,debug): abstract