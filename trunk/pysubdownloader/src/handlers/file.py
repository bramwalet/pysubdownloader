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
import os
import logging

class FileHandler(object):
    
    def __init__(self):
        self.log = logging.getLogger("PySubDownloader." + self.__class__.__name__)
         

    def determineSrtFilesInZip(self, filesInZip):
        srtFilesInZip = []
        for file in filesInZip:
            fileBaseName, fileExt = os.path.splitext(file)
            if fileExt == ".srt":
                srtFilesInZip.append(file)
        
        return srtFilesInZip


    def writeZipFile(self, episode, archive):
        zipFile = episode.generateZipFilename()
        self.log.debug("Zip filename: " + zipFile)
        zip = open(zipFile, 'w')
        zip.write(archive)
        zip.close()


    def writeSrtFile(self, episode, fileContent):
        srtfile = episode.generateSrtFilename()
        self.log.debug("SRT filename: " + srtfile)
        srt = open(srtfile, 'w')
        srt.write(fileContent)
        srt.close()

    def extractZipFile(self, episode, archive):
        filesInZip = archive.namelist()
        self.log.debug("Files in zip: " + str(filesInZip))
        srtFilesInZip = self.determineSrtFilesInZip(filesInZip)
        self.log.debug("SRT Files in zip: " + str(srtFilesInZip))
        
        if len(srtFilesInZip) == 1:
            for file in srtFilesInZip:
                srtFile = archive.read(file)
                self.writeSrtFile(episode, srtFile)
                return True
        if len(srtFilesInZip) < 1:
            self.log.warn("Found more than one file in zip. Extract aborted. Placing zip file instead")
            self.writeZipFile(episode, archive)
            return True
        else:
            self.log.warn("Expected at least 1 SRT file in zip, none found.")
            return False
        

    def readZipFile(self, content):
        fileContent = StringIO.StringIO(content)
        archive = zipfile.ZipFile(fileContent)
        return archive

    def openZipFile(self, content):
        try:
            archive = self.readZipFile(content)
        except:
            return None
        return archive

    def isZipFile(self, content):
        try:
            self.readZipFile(content)
        except:
            return False
        return True
    
