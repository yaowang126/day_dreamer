# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 12:41:52 2022

@author: YW
"""

class DuplicateError(Exception):
    pass

class DataABC:
    
    def add_property(self, variable_name:str, variable_series):
        if not isinstance(variable_name,str):
            raise TypeError('String is required for the variable name')
        if self.__dict__.get(variable_name):
            raise DuplicateError('This variable name is already in')
        else:
            self.__dict__[variable_name] = variable_series
            