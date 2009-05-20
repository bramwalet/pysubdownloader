'''
Created on 18 mei 2009

@author: Bram Walet
'''
from classes.ConfigException import ConfigException
from lib.LoggerFactory import LoggerFactory
class AbstractSubtitleSite(object):
    def __init__(self):
        self.config = self.setUp()
        try:    
            self.checkConfig()
        except (ConfigException, ), e:
            raise     
        self.setUpHandlers()
        lf = LoggerFactory(self.config['siteName'])
        self.log = lf.getLogger()
        
    
        

    def search(self,episodes): abstract
    
    def setUp(self): abstract
    
    def setUpHandlers(self): abstract
    
    def checkConfig(self,requiredKeys):
        if self.config is None:
            raise ConfigException("This site is unconfigured. Please implement method setUp() and fill these keys as dictionary: " + str(requiredKeys))
     
        for requiredKey in requiredKeys:
            try:
                self.config[requiredKey]
            except (KeyError, ), e:
                raise ConfigException(requiredKey + " is not configured")

    def downloadSubtitle(self,sub,episode,site):
        downloadurl = sub.getLink()
        self.uh.installUrlHandler()
        filein = self.uh.executeRequest(downloadurl)
        archive = self.fh.openZipFile(filein) 
        if self.fh.extractZipFile(episode, archive):
            self.log.debug("Extracted subtitle")
        