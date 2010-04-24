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
from ConfigException import ConfigException

class AbstractComponent(object):
    '''
    classdocs
    '''
    def __init__(self,logfile,debug):
        self.logfile = logfile
        self.debug = debug

    def checkConfigByKeys(self,config,requiredKeys):
        if config is None:
            raise ConfigException("This site is unconfigured. Please implement method setUp() and fill these keys as dictionary: " + str(requiredKeys))
        for requiredKey in requiredKeys:
            try:
                config[requiredKey]
            except (KeyError, ), e:
                raise ConfigException(requiredKey + " is not configured")

    def setConfig(self,config):
        self.config = config
        
    def setLogger(self,logger):
        self.log = logger