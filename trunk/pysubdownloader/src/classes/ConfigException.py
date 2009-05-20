'''
Created on 20 mei 2009

@author: Bram Walet
'''

class ConfigException(Exception):
    '''
    classdocs
    '''


    def __init__(self,value):
        '''
        Constructor
        '''
        self.value = value

    def __str__(self):
        return repr(self.value)

        