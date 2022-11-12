#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 11:29:23 2022

@author: even
"""

circle= np.linspace(0,2*np.pi,nb)

for i in range(1,nb):

    plt.plot(np.cos(circle),np.sin(circle),linewidth=0.5)
    plt.plot(np.cos(A[0,i]),np.sin(A[0,i]),marker='o')
    plt.plot(np.cos(A[1,i]),np.sin(A[1,i]),marker='o')
    plt.plot(np.cos(A[2,i]),np.sin(A[2,i]),marker='o')
    plt.plot(np.cos(A[3,i]),np.sin(A[3,i]),marker='o')
    plt.plot(np.cos(A[4,i]),np.sin(A[4,i]),marker='o')

    
    plt.pause(0.0001)
    plt.clf()
    


plt.xlim(-1,1)
plt.ylim(-1,1)
plt.show()