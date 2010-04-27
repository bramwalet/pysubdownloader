'''
Created on 24 apr 2010

@author: b.walet
'''
from sites.components.search.AbstractSearchComponent import AbstractSearchComponent

class ApiSearchComponent(AbstractSearchComponent):
    '''
    classdocs
    '''


    def __init__(self,params):
        '''
        Constructor
        '''

    def search(self, episodes, language):
        return AbstractSearchComponent.search(self, episodes, language)


    def checkConfig(self, config):
        return AbstractSearchComponent.checkConfig(self, config)


    def setupHandlers(self):
        return AbstractSearchComponent.setupHandlers(self)

        