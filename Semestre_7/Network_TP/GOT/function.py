from ast import get_docstring
import networkx as nx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from settings import *


def data(s):
    
    i=str(s)

    path1=os.path.join(os.path.dirname(__file__), 'data/got-s'+i+'-nodes.csv')
    path2=os.path.join(os.path.dirname(__file__), 'data/got-s'+i+'-edges.csv')

    x=pd.read_csv(path1)
    y=pd.read_csv(path2)
    G=nx.from_pandas_edgelist(y,"Source","Target")
    
    x=x.to_numpy()
    y=y.to_numpy()
    y=y[:,:3]
    
    
    
    Id=list(x[:,0])
    Label=list(x[:,1])
    HouseId=list(x[:,2])
    
    Source=list(y[:,0])
    Target=list(y[:,1])
    Weight=list(y[:,2])
    
    return Id, Label, HouseId, Source, Target, Weight, G




def Create_graph(s,Weighted=False):
    Id=data(s)[0]
    Source=data(s)[3]
    Target=data(s)[4]
    
    L_S=len(Source)
    L_I=len(Id)
    
    mat_adj=np.zeros((L_I,L_I))
    for i in range(L_S):
        a=Id.index(Source[i])
        b=Id.index(Target[i])
        # print(Source[i],Target[i],i)
        # print(a+2,b+2)
        # print(i)
        if Weighted == True :
            
            mat_adj[a,b]=data(s)[5][i]
            mat_adj[b,a]=data(s)[5][i]
        else:
            mat_adj[a,b]=1
            mat_adj[b,a]=1
    
    G=nx.from_numpy_array(mat_adj) 
    return mat_adj,G


def Draw_graph(s,G):
    
    nx.draw_networkx(G)
    plt.show()
    

def Max_count(func,n,G,s):
    Name=["Name"]
    Value=["Value"]
    func=func(G)
    it=len(func)
    while len(func) != it-n :
        x=max(func, key=func.get)
        Name.append(x)
        Value.append(round(func[x],3))
        func.pop(x)
    return Name, Value

def stats(s,G):
    a=Max_count(nx.degree_centrality,5,G,s)

    b=Max_count(nx.closeness_centrality,5,G,s)

    c=Max_count(nx.betweenness_centrality,5,G,s)
    fichier = open(os.path.join(os.path.dirname(__file__),"GOT_Most_important"+str(s)+".txt"),"w")
    fichier = open(os.path.join(os.path.dirname(__file__),"GOT_Most_important"+str(s)+".txt"),"a")

    fichier.write("---------------------\n"+"| degree_centrality |\n"+"---------------------\n")
    for i in range(len(a[0])):
        fichier.write(a[0][i]+","+str(a[1][i])+"\n")


    fichier.write("------------------------\n"+"| closeness_centrality |\n"+"------------------------\n")
    for i in range(len(a[0])):
        fichier.write(b[0][i]+","+str(b[1][i])+"\n")


    fichier.write("--------------------------\n"+"| betweenness_centrality |\n"+"--------------------------\n")
    for i in range(len(a[0])):
        fichier.write(c[0][i]+","+str(c[1][i])+"\n")


    fichier.close()