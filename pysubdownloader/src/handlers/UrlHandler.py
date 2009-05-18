'''
Created on 18 mei 2009

@author: Bram Walet
'''
import urllib2

            
class UrlHandler(object):
    
    def __init__(self):
        self.urllib2 = urllib2
    def executeRequest(self, downloadurl):
        return self.urllib2.urlopen(urllib2.Request(downloadurl))
    def installUrlHandler(self):
        http_handler = self.urllib2.HTTPHandler(debuglevel=False)
        opener = self.urllib2.build_opener(http_handler)
        self.urllib2.install_opener(opener)

