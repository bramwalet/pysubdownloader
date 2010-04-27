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
from sites.components.AbstractSubtitleSite import AbstractSubtitleSite

class TvSubtitleSite(AbstractSubtitleSite):
    
    def getSiteName(self):
        return "TvSubtitles"
    
    def setupSearch(self):
        config =  {  "rssFeed"  : "http://www.tvsubtitles.net/rssen.xml",
                     "baseUrl"  : "http://www.tvsubtitles.net/" }
       
        return (config)
  
    def setupLanguages(self):
        supportedLanguages = ("en", "es", "fr", "de", "br", "ru", "ua", "it", "gr", "ar","hu", "pl","tr")
#         config = { "siteName" : "Podnapisi",
#                   "baseUrl" : "http://simple.podnapisi.net/ppodnapisi/"}
#                  
        return supportedLanguages
