# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 09:36:14 2026

@author: piercetf
"""

import cProfile
    

def profile_func(profile_filename):
    
    def wrapping(func):
        
        def wrapped(*args, **kwargs):
            
            profile = cProfile.Profile()
            profile.enable()
            
            try:
                res = func(*args, **kwargs)
            
            except Exception as e:
                profile.disable()
                raise e
            
            finally:
                profile.disable()
                profile.dump_stats(profile_filename)
            
            return res
        
        return wrapped
    
    return wrapping