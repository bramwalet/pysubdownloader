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
import urllib2
import logging

      
class UrlHandler(object):
    
    def __init__(self):
        self.log = logging.getLogger("PySubDownloader." + self.__class__.__name__)
        self.installUrlHandler()
          
    def executeRequest(self, downloadurl):
        self.log.debug("Execute Request URL: " + downloadurl)
        request = urllib2.Request(downloadurl)
        response = urllib2.urlopen(request)
        responseInfo = response.info()
        return response, responseInfo.subtype

    def determineLoggingLevel(self):
        level = self.log.getEffectiveLevel()
        if level == logging.DEBUG:
            debuglevel = True
        else:
            debuglevel = False
        return debuglevel

    def installUrlHandler(self):
        debuglevel = self.determineLoggingLevel()
        http_handler = urllib2.HTTPHandler(debuglevel)
        opener = urllib2.build_opener(http_handler)
        urllib2.install_opener(opener)

