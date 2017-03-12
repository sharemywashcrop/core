# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 19:23:10 2017

@author: Thomas
"""

import base64

class user:
    
    def __init__(self,n,e,l,p,t=""):
        self.name = n
        self.email = e
        self.token = t
        self.location ="" # evol("(233,234)")
        self.pseudo = p