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
class AbstractSubtitleSite(object):
    def __init__(self,language,logfile,debug):
        (config,supportedLanguages) = self.setUp()
        try:    
            self.checkConfig(config)
            self.config = config
        except (ConfigException, ), e:
            raise    
        try:    
            self.checkLanguage(supportedLanguages,language)
            #self.supportedLanguages = supportedLanguages
            self.language = language
        except (ConfigException, ), e:
            raise     
        self.logfile = logfile
        self.debug = debug 
        lf = LoggerFactory(self.config['siteName'],logfile,debug)
        self.log = lf.getLogger()
        self.setUpHandlers()
        
       
        self.language = language
        
    
        

    def search(self,episodes): abstract
    
    def setUp(self): abstract
    
    def setUpHandlers(self): abstract
    
    def checkConfig(self,config,requiredKeys):
        if config is None:
            raise ConfigException("This site is unconfigured. Please implement method setUp() and fill these keys as dictionary: " + str(requiredKeys))
        for requiredKey in requiredKeys:
            try:
                config[requiredKey]
            except (KeyError, ), e:
                raise ConfigException(requiredKey + " is not configured")

    def checkLanguage(self,supportedLanguages,inputLanguage):
        if supportedLanguages is None:
            raise ConfigException("This site must support at least one language. Please return a list of supportedLanguages in method setUp()")
        languageFound = False
        for language in supportedLanguages:
            if language == inputLanguage:
               languageFound = True
                    
        if languageFound == False:
            raise ConfigException("This site does not support this language.")
       
                
     
       
    def downloadSubtitle(self,sub,episode):
        downloadurl = sub.getLink()
        self.uh.installUrlHandler()
        filein = self.uh.executeRequest(downloadurl)
        archive = self.fh.openZipFile(filein) 
        if self.fh.extractZipFile(episode, archive):
            self.log.info("Extracted subtitle")
        