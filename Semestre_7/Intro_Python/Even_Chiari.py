#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 13:42:55 2022

@author: even
"""

#%%    1.1 is odd ##



def is_odd(n):
    if n%2 == 0:
        return"False"
    else:
        return "True"
        
   
print(is_odd(int(input("give me a number : " ))))
     
#%% 1.2 odd_ints ##      

## defintion of function that i made before:


def is_odd(n):
    if n%2 == 0:
        return"False"
    else:
        return "True"

##definition of the function for the program:


def odd_ints(n):
    l=[]
    for i in n:
        if isinstance(i,bool) == True:
            pass
        elif isinstance(i,int) == True :
            if is_odd(i) == "True":
                l.append(i)
        else:
            pass
    return l
        
print(odd_ints([1, True, "hello", 5, 0, 10]))



#%% 1.3. filter_odd_ints ##

## defintion of function that i made before:


def is_odd(n):
    if n%2 == 0:
        return"False"
    else:
        return "True"
    
    
def odd_ints(n):
    l=[]
    for i in n:
        if isinstance(i,bool) == True:
            pass
        elif isinstance(i,int) == True :
            if is_odd(i) == "True":
                l.append(i)
        else:
            pass
    return l

##definition of the function for the program:       
        
def  filter_odd_ints(n):
     n = list(filter(None,n))
     l=[]
     print(n)
     for i in n:
         if i%2 == 0:
             l.append(i)
         else:
             pass
        
     return l
     

    
print(filter_odd_ints([1, True, "hello", 5, 0, 10]))
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
