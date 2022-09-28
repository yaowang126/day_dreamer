# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 12:09:47 2022

@author: YW
"""
from day_dreamer_abc import DataABC

class DataLoader(DataABC):
    ...
    def __init__(self):
         self.name = 'n'
        
dl = DataLoader()
dl.add_property('sexual', [1,0])
dl.add_property('sexual', [1,0])
    