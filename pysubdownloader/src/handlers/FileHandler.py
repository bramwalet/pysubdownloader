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

import zipfile, StringIO
from lib.LoggerFactory import LoggerFactory

class FileHandler(object):
    
    def __init__(self, logfile, debug):
        self.logfile = logfile
        lf = LoggerFactory("FileHandler", logfile, debug)
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
    def openZipFile(self, content):
        try:
            fileContent = StringIO.StringIO(content)
            archive = zipfile.ZipFile(fileContent)
        except:
            return None
        return archive

    def isZipFile(self, content):
        try:
            fileContent = StringIO.StringIO(content)
            zipfile.ZipFile(fileContent)
        except:
            return False
        return True
    
