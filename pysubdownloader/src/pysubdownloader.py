'''
Created on 17 mei 2009

@author: Bram Walet
'''

import sys
from lib.Inspector import Inspector
from sites.TvSubtitleSite import TvSubtitleSite

''' main function 
''' 
if __name__ == '__main__':
    # TODO: help, proper handling
    print("start subdownloader")
    path = sys.argv[1]
    inspector = Inspector()
    episodes = inspector.scan(path)
    try:
        tvsub = TvSubtitleSite()    
        tvsub.search(episodes)
    except (RuntimeError, ), e:
        raise
   
        