'''
Created on 17 mei 2009
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
from optparse import OptionParser
from springpython.config import YamlConfig
from springpython.context import ApplicationContext
import logging


    
def main():
    (path, language, logfilepath, debug) = parseOptions()
    setupLogging(debug,logfilepath)
    startSubtitleDownloader(path, language)

def parseOptions():
    parser = OptionParser()
    parser.add_option("-f", dest="folder", help="scan this folder and subfolders", metavar="FOLDER")
    parser.add_option("-d", "--debug", action="store_true", dest="debug", default=False)
    parser.add_option("--log", dest="logfile", help="log to this file", metavar="LOGFILE")
    parser.add_option("-l", dest="language", help="language to search subtitles for", type="choice", choices=("en", "nl"), default="en")
    (options, args) = parser.parse_args()
    if options.folder is None:
        parser.error("-f is a required option")
        
    else: 
        path = options.folder 

    return (path, options.language, options.logfile, options.debug)
 
def startSubtitleDownloader(path, language):
#    container = ApplicationContext(XMLConfig("app-context.xml"))
    container = ApplicationContext(YamlConfig("app-context.yml"))
    inspector = container.get_object("inspector")
    sites = container.get_object("enabledsites")
    maxdays = container.get_object("maxdays")
    
    episodes = inspector.scan(path, maxdays)
    if len(episodes) > 0:
        for site in sites.__iter__():
            currentsite = container.get_object(site + "site")
            currentsite.run(episodes, language)
    
def setupLogging(debug, logfilepath):
    if debug:
        loglevel = logging.DEBUG
    else:
        loglevel = logging.INFO
        
    ''' Application logging
    '''
    log = logging.getLogger("PySubDownloader")
    log.setLevel(loglevel)
    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel(loglevel)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
    consoleHandler.setFormatter(formatter)
    log.addHandler(consoleHandler)
    
    if(logfilepath is not None):
        handler = logging.handlers.RotatingFileHandler(
                  logfilepath, maxBytes=20, backupCount=5)
        log.addHandler(handler)

    
    ''' Spring Python logging
    '''
    springlogger = logging.getLogger("springpython")
    loggingLevel = logging.DEBUG
    springlogger.setLevel(loggingLevel)
    springlogger.addHandler(consoleHandler)
       
    return log

if __name__ == '__main__':
    main()