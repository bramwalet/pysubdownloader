'''
Created on 18 mei 2009

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
        return response
    def installUrlHandler(self):
        http_handler = self.urllib2.HTTPHandler(debuglevel=self.debug)
        opener = self.urllib2.build_opener(http_handler)
        self.urllib2.install_opener(opener)

