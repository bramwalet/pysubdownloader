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
from lib.Inspector import Inspector
#from sites.TvSubtitleSite import TvSubtitleSite
from sites.PodnapisiSite import PodnapisiSite
from sites.TvSubtitleSite import TvSubtitleSite
from lib.LoggerFactory import LoggerFactory
from sites.BierdopjeSite import BierdopjeSite
from springpython.context import ApplicationContext
from springpython.config import XMLConfig
import logging
#from sites.TvSubsSite import TvSubsSite

    
def parseOptions():
    
    parser = OptionParser()
    parser.add_option("-f", dest="folder", help="scan this folder and subfolders", metavar="FOLDER")
    parser.add_option("-d", "--debug", action="store_true", dest="debug", default=False)
    parser.add_option("--log", dest="logfile", help="log to this file", metavar="LOGFILE")
    parser.add_option("-l", dest="language", help="language to search subtitles for", type="choice", choices=("en", "nl"), default="en")
    (options, args) = parser.parse_args()
    if options.folder is None:
        #usage()
        parser.error("-f is a required option")
        
    else: 
        path = options.folder 
#    if options.language is None:
#        parser.error("-l is a required option")
#    else: 
#        language = options.language   
    return (path, options.language, options.logfile, options.debug)


def startSubtitleDownloader(path, language, logfile, debug, logger):
    logger = logging.getLogger("springpython")
    loggingLevel = logging.DEBUG
    logger.setLevel(loggingLevel)
    ch = logging.StreamHandler()
    ch.setLevel(loggingLevel)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    container = ApplicationContext(XMLConfig("app-context.xml"))
    inspector = container.get_object("inspector")
    
    episodes = inspector.scan(path)
    
    tvsub = container.get_object("tvsubtitlesite")
    tvsub.run(episodes, language)
    
    podnapisi = container.get_object("podnapisisite")
    podnapisi.run(episodes, language)

    
#    try:
#        logger.info("Starting Bierdopje")
#        bierdopje = BierdopjeSite(language,logfile,debug)
#        bierdopje.run(episodes,language)
#    except (RuntimeError, ), e:
#        raise
    
   


def main():
    (path, language, logfilepath, debug) = parseOptions()
    logger = setupLogging()
    startSubtitleDownloader(path, language, logfilepath, debug, logger)
    
def setupLogging():
    return LoggerFactory.getLogger("PySubDownloader")
        
if __name__ == '__main__':
    main()  
    
        
