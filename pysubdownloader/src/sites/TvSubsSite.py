#'''
#Created on 21 mei 2009
#Copyright 2009 Bram Walet
#
#This file is part of PySubDownloader.
#
#PySubDownloader is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#PySubDownloader is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with PySubDownloader.  If not, see <http://www.gnu.org/licenses/>.
#
#@author: Bram Walet
#'''
#from sites.AbstractHtmlSite import AbstractHtmlSite
#
#class TvSubsSite(AbstractHtmlSite):
#    '''
#    classdocs
#    '''
## &setlang1=en
#    def setUp(self):
#        supportedLanguages = ("en", "es", "fr", "de", "br", "ru", "ua", "it", "gr", "ar","hu", "pl","tr")
#        config = { "siteName" : "TvSubs",
#                   "findTableString" : 'cont',
#                   "findDownloadLink" : 'subtitle',
#                   "baseUrl" : "http://www.tvsubs.net/",
#                   "searchUrl" : "http://www.tvsubs.net/new.html" }
#        return (config,supportedLanguages)
#    
#    def getKeys(self,episode):
#        languageKeys = {"en":"en"}
#        searchKeys = ['setlang1=' + languageKeys[self.language]]
#        sep = '&'
#        return (searchKeys,sep)
#    
#      