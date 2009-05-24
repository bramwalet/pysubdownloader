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
from classes.ConfigException import ConfigException
from lib.LoggerFactory import LoggerFactory
import sites.components
import sites.components.download
import sites.components.search

class AbstractSubtitleSite(object):
    
    def __init__(self,language,logfile,debug):
#        (config,supportedLanguages) = self.setUp()
#        try:    
#            self.checkConfig(config)
#            self.config = config
#        except (ConfigException, ), e:
#            raise    
#        try:    
#            self.checkLanguage(supportedLanguages,language)
#            #self.supportedLanguages = supportedLanguages
        self.language = language
#        except (ConfigException, ), e:
#            raise    
        
         
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

#    def search(self,episodes): abstract
#    
    def setUp(self,logfile,debug): abstract
#    
#    def setUpHandlers(self): abstract
#    
#   
#    def checkLanguage(self,supportedLanguages,inputLanguage):
#        if supportedLanguages is None:
#            raise ConfigException("This site must support at least one language. Please return a list of supportedLanguages in method setUp()")
#        languageFound = False
#        for language in supportedLanguages:
#            if language == inputLanguage:
#               languageFound = True
#                    
#        if languageFound == False:
#            raise ConfigException("This site does not support this language.")
#       
#                
     
       
