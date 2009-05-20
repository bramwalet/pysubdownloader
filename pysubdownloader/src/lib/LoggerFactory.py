'''
Created on 21 mei 2009

@author: Bram Walet
'''
import logging

class LoggerFactory(object):
    '''
    classdocs
    '''


    def __init__(self,className):
        '''
        Constructor
        '''
        self.log = logging.getLogger(className)
        self.log.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        ch.setFormatter(formatter)
        self.log.addHandler(ch)

    def getLogger(self):
        return self.log