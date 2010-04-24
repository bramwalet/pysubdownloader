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

from lib.LoggerFactory import LoggerFactory
      
class UrlHandler(object):
    
    def __init__(self,logfile,debug):
        self.urllib2 = urllib2
        self.logfile = logfile
        lf = LoggerFactory("UrlHandler",logfile,debug)
        self.log = lf.getLogger()
        self.debug = debug
    def executeRequest(self, downloadurl):
        self.log.debug("Execute Request URL: " + downloadurl)
        request = self.urllib2.Request(downloadurl)
        response = self.urllib2.urlopen(request)
        responseInfo = response.info()
        return response, responseInfo.subtype
    def installUrlHandler(self):
        http_handler = self.urllib2.HTTPHandler(debuglevel=self.debug)
        opener = self.urllib2.build_opener(http_handler)
        self.urllib2.install_opener(opener)

