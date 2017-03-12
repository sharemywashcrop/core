# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 21:17:42 2017

@author: Thomas
"""

import pymysql

class db:
    
    def __init__(self):
        self.connection = pymysql.connect (host = "198.100.148.10", user = "sharemywash",passwd = "epitaepita",db = "sharemywash") 
                              
                              
    def ex(self,query):
        cur = self.connection.cursor()
        ret = cur.execute(query)
        self.connection.commit()
        return ret
        
    def query(self,query):
        cur = self.connection.cursor()
        cur.execute(query)
        res = cur.fetchall()
        return res
        
        
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              