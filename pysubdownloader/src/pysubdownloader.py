'''
Created on 17 mei 2009

@author: Bram Walet

'''
import sys
from optparse import OptionParser
from lib.Inspector import Inspector
from sites.TvSubtitleSite import TvSubtitleSite
from sites.PodnapisiSite import PodnapisiSite
from sites.TvSubsSite import TvSubsSite

    
def parseOptions():
   
    parser = OptionParser()
    parser.add_option("-f", dest="folder", help="scan this folder and subfolders", metavar="FOLDER")
   # parser.add_option("-d", "--debug", action="store_true", dest="debug", default=False)
   # parser.add_option("-v", "--verbose", action="store_true", dest="verbose", default=False)
   # parser.add_option("--log", dest="logfile", help="logfile", metavar="LOGFILE")
    parser.add_option("-l", dest="language", help="language to search subtitles for", type="choice", choices=("en","nl"))
    (options, args) = parser.parse_args()
    if options.folder is None:
        #usage()
        parser.error("-f is a required option")
        
    else: 
        path = options.folder 
    if options.language is None:
        parser.error("-l is a required option")
    else: 
        language = options.language   
    return (path,language)


def startSubtitleDownloader(path,language):
    inspector = Inspector()
    episodes = inspector.scan(path)
    try:
        tvsub = TvSubtitleSite(language)
        tvsub.search(episodes)
    except (RuntimeError, ), e:
        raise
    
    try:
    	
        podnapisi = PodnapisiSite(language)
        podnapisi.search(episodes)
    except (RuntimeError, ), e:
        raise

#    try:
#        
#        tvsubs = TvSubsSite(language)
#        tvsubs.search(episodes)
#    except (RuntimeError, ), e:
#        raise


    


def main():
    (path,language) = parseOptions()
    startSubtitleDownloader(path,language)
    

if __name__ == '__main__':
    main()  
    
        