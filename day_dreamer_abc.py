# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 12:41:52 2022

@author: YW
"""

class DuplicateError(Exception):
    pass

class DataABC:
    
    def add_property(self, property_name:str, property_value):
        if self.__dict__.get(property_name):
            raise DuplicateError('This variable name is already in')
        else:
            self.__dict__[property_name] = property_value
            