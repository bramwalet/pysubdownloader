'''
Created on 21 mei 2009
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
import logging, logging.handlers



class LoggerFactory(object):
    '''
    classdocs
    '''


    def __init__(self,className,logfile,debug):
        '''
        Constructor
        '''
        if debug == True:
            loglevel = logging.DEBUG
        else:
            loglevel = logging.INFO
        self.log = logging.getLogger(className)
        self.log.setLevel(loglevel)
        consoleHandler = logging.StreamHandler()
        
        consoleHandler.setLevel(loglevel)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
        consoleHandler.setFormatter(formatter)
        self.log.addHandler(consoleHandler)
        
        if logfile != None:
            fileHandler = logging.handlers.RotatingFileHandler(logfile, maxBytes=10485760, backupCount=5)
            self.log.addHandler(fileHandler)

        

    def getLogger(self):
        return self.log