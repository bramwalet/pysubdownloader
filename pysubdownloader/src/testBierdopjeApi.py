'''
Created on 27 apr 2010

@author: b.walet
'''
from springpython.context import ApplicationContext
from springpython.config import XMLConfig
import logging
from sites.components.search.api.bierdopje import BierdopjeAPI
from xml.etree.ElementTree import dump
from Episode import Episode

if __name__ == '__main__':
    loglevel = logging.DEBUG
    log = logging.getLogger("PySubDownloader")
    log.setLevel(loglevel)
    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel(loglevel)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
    consoleHandler.setFormatter(formatter)
    log.addHandler(consoleHandler)
    
    ''' Spring Python logging
    '''
    springlogger = logging.getLogger("springpython")
    loggingLevel = logging.DEBUG
    springlogger.setLevel(loggingLevel)
    springlogger.addHandler(consoleHandler)
    container = ApplicationContext(XMLConfig("app-context.xml"))
    wrapper = container.get_object("bierdopjeWrapper")
    episode = Episode("Fringe", 2008, 2, "19", "Y:\TV\Fringe\Season 2", "Fringe - 2x19 - The Man From The Other Side.mkv")
    wrapper.search(episode,"nl")
    
#    api = container.get_object("bierdopjeApi")
#    dump(api.FindShowByName("24"))
#    dump(api.GetShowByName("24"))
#
#    dump(api.GetShowById("900"))
#    dump(api.GetShowByTVDBID("79567"))
#    dump(api.GetAllEpisodesForShow("13249"))
#    dump(api.GetEpisodeById("387441"))
#    dump(api.GetAllSubsForEpisode("387444", "nl"))
#    
#    dump(api.GetAllSubsFor("900","3","1","nl","false"))