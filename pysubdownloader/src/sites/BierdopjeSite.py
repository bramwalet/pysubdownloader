'''
Created on 24 apr 2010

Copyright 2009-2010 Bram Walet

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
from sites.components.AbstractSubtitleSite import AbstractSubtitleSite
from sites.components.search.RssSearchComponent import RssSearchComponent
from sites.components.download.HttpDownloadComponent import HttpDownloadComponent

class BierdopjeSite(AbstractSubtitleSite):
    
    def setUp(self,logfile,debug):
        search = RssSearchComponent(logfile,debug)
        download = HttpDownloadComponent(logfile,debug)
        return (search,download)
    
    def getSiteName(self):
        return "BierdopjeSite"
    
    def setupSearch(self):
        config =  {  "rssFeed"  : "http://feeds.bierdopje.com/bierdopje/subs/dutch",
                     "baseUrl"  : "http://feeds.bierdopje.com/bierdopje/subs/" }
       
        return (config)
  
    def setupLanguages(self):
        supportedLanguages = ("en", "nl")         
        return supportedLanguages
