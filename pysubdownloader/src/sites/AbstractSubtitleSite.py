'''
Created on 18 mei 2009

@author: Bram Walet
'''

class AbstractSubtitleSite(object):
    def __init__(self): abstract
    def search(self,episodes): abstract
    def downloadSubtitle(self,sub,episode): abstract
        