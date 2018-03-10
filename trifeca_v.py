# -*- coding: utf-8 -*-
"""
Created on Fri Mar 09 17:33:56 2018

@author: Gad
"""

def trifeca(word):
    pairs=0 #counts letter pairs
    for i in range(len(word)-1):
       if word[i]==word[i+1]:
           pairs+=1
           i+=1 #skips one letter if we found a double
           
    if pairs>=3:
        truth=True
        print(truth)
    else:
        print(False)
       
                    
    