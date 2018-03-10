# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 12:46:45 2018

@author: Gad
"""
#this function is meant to check if a given number fits the needed 4 conditions
def con_fit (number):
    con_one=str(number)
    if con_one[2:6]==con_one[-1:-5]:
        number+=1
        con_two=str(number)
        if con_two[1:6]==con_one[-1:-6]:
            number+=1
        con_three=str(number)
        if con_three[1:5]==con_one[-2:-6]:
            number+=1
        con_four=str(number)
        if con_four[0:6]==con_one[-1:-7]:
            return(number)
#this function is needed to itterate on 6 digit numbers
def num_it():
    for i in range(100000,999999):
        truth=con_fit(i)
        if truth:
            print (i)
        
        

        