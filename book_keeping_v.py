# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 20:43:05 2018

@author: Gad
"""

#use these dictionaries as input
#history1 = {'jon':60, 'tami':75, 'george':90, 'mark':75}
#history2 = {'jon':70, 'tami':85, 'george':100, 'mark':85}
#math1 = { 'tom':80, 'jon':85, 'tami':50,'george':65}
#math2 = { 'tom':70, 'jon':75, 'tami':80,'george':85}

#book keeping
def compare_subjects (history1,history2,math1,math2):
    better_at_history={}
    better_at_math={}
    better_at={}
    for key in history1:
        if key in history2:
            if history1[key]>history2[key]:
                better_at_history[key]=history1[key]
                better_at_history[key] = 'History1'
            else:
                better_at_history[key]=history2[key]
                better_at_history[key] = 'History2'
    for key in math1:
        if key in math2:
            if math1[key]>math2[key]:
                better_at_math[key]=math1[key]
                better_at_math[key] = 'Math1'
            else:
                better_at_math[key]=math2[key]
                better_at_math[key] = 'Math2'
                
    for key in better_at_math:
        if key in better_at_history:
            if better_at_math[key]>better_at_history[key]:
                better_at[key]=better_at_math[key]
            else:
                better_at[key]=better_at_history[key]
    return better_at
