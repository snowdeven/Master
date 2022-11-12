#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 16:58:46 2022

@author: even
"""

n=5

L=(['2 \n 1'],['1 \n 2'])

def switch(n,remplir=False):
    if n>2 :
        switch(n-2)
        print(n)
        switch(n-2,remplir=True)
        switch(n-1)
    else:
        if n ==2 :
            print(*L[remplir])
        else:
            return 1



switch(n)


