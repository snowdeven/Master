from ast import get_docstring
import networkx as nx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import os
from settings import *



def Data(S):
    """This function read the csv file for a season S 
    using panda to compute the graph and to put the data in list.

    Args:
        s (int): the number of a season

    Returns: 
        Id (list): list of  type string of the season Id
        Label (list): list of  type string of the season Label
        HouseId (list): list of  type string of the season HouseId
        Source (list): list of  type string of the season Source
        Target (list): list of  type string of the season Target
        Weight (list): list of integer off the season Weight
        G (networkx.graph): Graph on a file with nodes, edges and labels
    """    
    path1=os.path.join(os.path.dirname(__file__), f'data/got-s{S}-nodes.csv') #we use os library to get the path of our file 
    path2=os.path.join(os.path.dirname(__file__), f'data/got-s{S}-edges.csv')
    
    x=pd.read_csv(path1) #we use panda to read csv file 
    y=pd.read_csv(path2)
    
    G=nx.from_pandas_edgelist(y,"Source","Target") #we create a graph using networkx from panda dataframe 
    
    x=x.to_numpy()#turn  panda dataframe to an array 
    y=y.to_numpy()
    
    Id=list(x[:,0])
    Label=list(x[:,1])
    HouseId=list(x[:,2])
    
    Source=list(y[:,0])
    Target=list(y[:,1])
    Weight=list(y[:,2])
    
    return Id, Label, HouseId, Source, Target, Weight, G


def Important_char(func,n,G):
    """Find the most (n=5) important characters in terms of degree, closesnees or betweeness 
    using a function 'func 'to represent each one of them
    we compute the function of G and we get a dictonary
    after we sorted it in decrasing order and take the n-first keys = characters


    Args:
        func (function): represent func that can be compute our graph in our case it is degree, closesnees or betweeness
        n (int): variable to choose how many we want for the most important character
        G (networkx.granx.coph): Graph on a file with nodes, edges and labels

    Returns:
        Name (list) :list of  type string of (n=5) most important characters name
        Value (list) :list of  type string of (n=5) most important characters value of the function "func"
    """    
    Name=["Name"]
    Value=["Value"]
    dic=func(G)
    sorted_dic=sorted(dic.items(), key=lambda x:x[1],reverse=True)
    for i in sorted_dic[:n]:
        Name.append(i[0])
        Value.append(i[1])

    return Name,Value


def Txt_imp_char(S,n,G):
    """Create a txt file of (n=5) most important characters in terms of degree, closesnees or betweeness for the season s
    Args:
        s (int): the number of a season
        n (int): variable to choose how many we want for the most important character
        G (networkx.graph): Graph on a file with nodes, edges and labels

    """    
    a=Important_char(nx.degree_centrality,n,G)

    b=Important_char(nx.closeness_centrality,n,G)

    c=Important_char(nx.betweenness_centrality,n,G)
    file = open(os.path.join(os.path.dirname(__file__),f"result/exercise_2/GOT_Most_important_S{S}.txt"),"w") #"w" to open a file and erase the previous data if he is already exsit
    file = open(os.path.join(os.path.dirname(__file__),f"result/exercise_2/GOT_Most_important_S{S}.txt"),"a") #"a" to open a file and add the data after the previous one

    Title="| degree_centrality |"
    file.write("-"*len(Title)+"\n"+Title +"\n"+"-"*len(Title)+"\n")
    for i in range(len(a[0])):
        file.write(a[0][i]+","+str(a[1][i])+"\n") 

    Title="| closeness_centrality |"
    file.write("-"*len(Title)+"\n"+Title +"\n"+"-"*len(Title)+"\n")
    for i in range(len(a[0])):
        file.write(b[0][i]+","+str(b[1][i])+"\n")

    Title="| betweeness_centrality |"
    file.write("-"*len(Title)+"\n"+Title +"\n"+"-"*len(Title)+"\n")
    for i in range(len(a[0])):
        file.write(c[0][i]+","+str(c[1][i])+"\n")


    file.close()

def Txt_stats(S,G):
    """Create a txt file for all the character with their values in terms of degree, closesnees or betweeness for the season s
    Args:
        S (int): the number of a season
        n (int): variable to choose how many we want for the most important character
        G (networkx.graph): Graph on a file with nodes, edges and labels
    """    
    dic1=nx.degree_centrality(G)
    dic2=nx.closeness_centrality(G)
    dic3=nx.betweenness_centrality(G)
    

    Name=Data(S)[0]
    Value_d=[]
    Value_c=[]
    Value_b=[]
    
    file = open(os.path.join(os.path.dirname(__file__),f"result/exercise_2/GOT_stats_S{S}.txt"),"w")#"w" to open a file and erase the previous data if he is already exsit
    file = open(os.path.join(os.path.dirname(__file__),f"result/exercise_2/GOT_stats_S{S}.txt"),"a")#"a" to open a file and add the data after the previous one
    file.write("Name,Degree,Closeness,Betweenness"+"\n")
    
    for i in range(len(Name)): 
        Value_d.append(dic1.get(Name[i])) #dic(1/2/3).get to obtains values of the key name[i]
        Value_c.append(dic2.get(Name[i]))
        Value_b.append(dic3.get(Name[i]))
    

        file.write(str(Name[i])+","+str(Value_d[i])+","+str(Value_c[i])+","+str(Value_b[i])+"\n")
        
    file.close()


def draw(S,G):
    """Function to plot the graph with better parameter

    Args:
        S (int): the number of a season
        G (networkx.graph): Graph on a file with nodes, edges and labels
    """    
    pos = nx.spring_layout(G,k=1.5,iterations=100)
    d=nx.degree_centrality(G)
    w=Data(S)[5]
    nx.draw_networkx(G,pos,with_labels=False
                    ,node_color=houses_colors(G,S)[0]
                    ,node_size=[d[k]*300 for k in d]
                    ,width=1
                    # ,width=[w[k]/20 for k in w]
                    ,edge_color='gray'
                    ,style='--')
    for node, (x, y) in pos.items():
        plt.text(x, y, node, fontsize=(3*np.log(d[node]+1)+0.5), ha='center', va='center')






def Mat_adj(S,Weighted=False):
    """Define the adjacency matrix for a graph of a season s. 
    the number of rows and column is the number of nodes,
    each element (m[i,j]) of our matrix has to be equal to one if i and j are linked,
    or equal to the weight of the link between the node i and j for the Weighted adjacency matrix.

    Args:
        s (int): the number of a season
        Weighted (bool, optional): boolean to precise the tpe of matrix, weighted or not. Defaults to False.

    Returns:
        mat_adj (array) : matrix of adjacency
    """    
    Id=Data(S)[0]
    Source=Data(S)[3]
    Target=Data(S)[4]
    
    L_S=len(Source)
    L_I=len(Id)
    
    mat_adj=np.zeros((L_I,L_I))
    for i in range(L_S):
        a=Id.index(Source[i])
        b=Id.index(Target[i])
        
        if Weighted == True :
            
            mat_adj[a,b]=Data(S)[5][i]
            mat_adj[b,a]=Data(S)[5][i]
        else:
            mat_adj[a,b]=1
            mat_adj[b,a]=1
            
    return mat_adj


def Hist_Weight(S):
    """Create a histogram of of the links weight for the season S.
    Args:
        S (int): the number of a season
    """    
    plt.title(f"season_{S}")
    w=Data(S)[5]
    bindwith=1
    bin = range(min(w), max(w)+ bindwith, bindwith)
    plt.hist(w,bins=bin,color="c",edgecolor="black")
    plt.xlabel("Weight")
    plt.ylabel("Frequency")


def houses_colors(G,S):

    colors ={"WESTEROS":"red","BARATHEON":"yellow","ARRYN":"orange","TULLY":"darkgoldenrod","MARTELL" : "lime"
            ,"BOLTON":"forestgreen","LANNISTER":"turquoise","TARGARYEN":"royalblue","TYRELL":"lightsalmon"
            ,"STARK":"blueviolet","WALL":"blue","GREYJOY":"olive","ESSOS":"peru","FREY" : "darkseagreen"}
    houses_colors = []
    label_colors=[]
    nodes=G.nodes()
    for i in nodes:
        x=Data(S)[2][Data(S)[0].index(i)]
        houses_colors.append(colors.get(x))
        label_colors.append(x)
    return houses_colors, label_colors




def attack(G,A,f):
    G_copy = G.copy()
    for i in range(int(f*A)):
        removed_node=np.random.choice(list(G_copy.nodes()))
        G_copy.remove_node(removed_node)

    return G_copy



def evolution(S,animation=False):
    A=len(Data(S)[6])
    mean=[]
    value_f=[]
    for f in np.arange(0,1.05,0.05):
        G=Data(S)[6]
        G_reduced=attack(G,A,f)
        
        size=[len(c) for c in sorted(nx.connected_components(G_reduced), key=len, reverse=True)]
        
        if len(G_reduced) == 0:
            mean.append(0)
            break
        else:
            mean.append(np.mean(size))
            value_f.append(f*100)
            if animation == True:
                pos = nx.spring_layout(G_reduced,k=1.5,iterations=100)
                d=nx.degree_centrality(G_reduced)
                plt.subplot(121)
                nx.draw_networkx(G_reduced,pos,with_labels=False
                                ,node_color=houses_colors(G_reduced,S)[0]
                                ,node_size=[d[k]*500 for k in d]
                                ,width=[d[k]*3 for k in d]
                                ,edge_color='gray')
                for node, (x, y) in pos.items():
                    plt.text(x, y, node, fontsize=(15*np.log(d[node]+1)+10), ha='center', va='center')
                plt.subplot(122)
                plt.plot(value_f,mean)
                plt.pause(0.01)
                plt.clf()
    plt.show()
    return mean


# def count(l):
#     return (np.diff(l)!=0).sum()

