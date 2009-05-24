'''
Created on 18 mei 2009

@author: Bram Walet
'''

import zipfile, StringIO
from classes.Episode import Episode
from lib.LoggerFactory import LoggerFactory

class FileHandler(object):
    
    def __init__(self,logfile,debug):
        self.logfile = logfile
        lf = LoggerFactory("FileHandler",logfile,debug)
        self.log = lf.getLogger()
        
    def extractZipFile(self, episode, archive):
        filesInZip = archive.namelist()
        self.log.debug("Files in zip: " + str(filesInZip))
        # TODO: warn or error if zip file has more than one file, or check which file we need.
        if len(filesInZip) == 1:
            for file in filesInZip:
                srtfile = episode.generateSrtFilename()
                self.log.debug("SRT filename: " + srtfile)
                srt = open(srtfile, 'w')
                srt.write(archive.read(file))
                srt.close()
                return True
        else:
            return False
    def openZipFile(self, filein):
        archive = zipfile.ZipFile(StringIO.StringIO(filein.read()))
        return archive

