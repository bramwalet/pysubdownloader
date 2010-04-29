'''
Created on 28 apr 2010

@author: b.walet
'''
import ConfigParser

class ConfigurationParser(object):
    '''
    classdocs
    '''


    def __init__(self, filename):
        '''
        Constructor
        '''
        self.config = ConfigParser.RawConfigParser()
        self.filename = filename
        
    def getConfigSites(self, sites):
        self.config.read()
        enabled = {}
        for site in sites:
            enabled[site] = self.getConfigValue(self.config, site, "enabled")
        return enabled
    
    
    def getConfigValue(self, section, option):
        if self.config.has_option(section, option):
            return self.config.get(section, option)
    
