'''
Created on 21 mei 2009

@author: Bram Walet
'''
import logging, logging.handlers



class LoggerFactory(object):
    '''
    classdocs
    '''


    def __init__(self,className,logfile,debug):
        '''
        Constructor
        '''
        if debug == True:
            loglevel = logging.DEBUG
        else:
            loglevel = logging.INFO
        self.log = logging.getLogger(className)
        self.log.setLevel(loglevel)
        consoleHandler = logging.StreamHandler()
        
        consoleHandler.setLevel(loglevel)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
        consoleHandler.setFormatter(formatter)
        self.log.addHandler(consoleHandler)
        
        if logfile != None:
            fileHandler = logging.handlers.RotatingFileHandler(logfile, maxBytes=10485760, backupCount=5)
            self.log.addHandler(fileHandler)

        

    def getLogger(self):
        return self.log