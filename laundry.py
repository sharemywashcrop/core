# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 19:24:25 2017

@author: Thomas
"""

import base64

class laundry:
    
    def __init__(self,l,m=[],d=[]):
        self.location = l
        self.machines = m
        self.dryers = d