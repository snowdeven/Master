import networkx as nx
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import os
from settings import *
from function import *

# --------------PART_TWO--------------#

# for S in range(1,9):             #we made a loop to compute all the data for each season
#     loc="24"+str(S)              #localisation of the subplot
#     plt.subplot(int(loc))
#     G=Data(S)[6]                 #our function data that retrun the network in position 6
#     plt.title(f"season_S{S}")
#     draw(S,G)                    #We draw the Graph
#     Txt_imp_char(S,5,G)          #We write a file of most important character of the season S
#     Txt_stats(S,G)                               #We write a file of all the stats for the character of the season S


# plt.savefig(os.path.join(os.path.dirname(__file__),f"result/exercise_2/Graph_S1-S8.png"))
# plt.show()


# # --------------PART_THREE--------------#



# for S in range(1,9):
#     Name=Data(S)[0]
#     W_degree=np.zeros(len(Name))

#     mat_adj=Mat_adj(S,Weighted=True)
#     for i in range(len(Name)):
#         W_degree[i]=sum(mat_adj[i,:])

#     sort_index=np.argsort(W_degree)[::-1]
#     if S == 1:
#         file = open(os.path.join(os.path.dirname(__file__),"result/exercise_3/Weighted_most_imp_char_S1-S9.txt"),"w")
#     else:
#         file = open(os.path.join(os.path.dirname(__file__),"result/exercise_3/Weighted_most_imp_char_S1-S9.txt"),"a")
#     Title=f"| Weighted_degree_centrality season {S} |"
#     file.write("-"*len(Title)+"\n"+Title +"\n"+"-"*len(Title)+"\n")
#     file.write("Name,Value\n")
#     for i in sort_index[:5]:
#         file.write(Name[i]+","+str(W_degree[i])+"\n")
    
#     file = open(os.path.join(os.path.dirname(__file__),f"result/exercise_3/Char_weighted_degree_S{S}.txt"),"w")
#     file = open(os.path.join(os.path.dirname(__file__),f"result/exercise_3/Char_weighted_degree_S{S}.txt"),"a")
#     file.write("Name,Value\n")
#     for count, elem in enumerate(W_degree):
#         file.write(Name[count]+ f", {elem}"+"\n")
#     file.close()

# for S in range(1,9):#we made a loop to compute all the data for each season
#     Colors=["royalblue"]
#     loc=f"24{S}"   #localisation of the subplot
#     plt.subplot(int(loc))
#     Hist_Weight(S)


# plt.savefig(os.path.join(os.path.dirname(__file__),f"result/exercise_3/Weight_distribution_S1-S8.png"))

# plt.show()

# --------------PART_FOUR-------------- #

# for S in range(2,3):#we made a loop to compute all the data for each season
#     G=Data(S)[6]
#     C=nx.connected_components(G)
    
#     size=[len(c) for c in sorted(nx.connected_components(G), key=len, reverse=True)]
    
#     if len(list(nx.connected_components(G))) > 1 :
#         sub=[G.subgraph(c).copy() for c in nx.connected_components(G) ][1]
#         Id=list(list(C)[1])
#         draw(S,sub)
#     relative_size=np.array(size)/sum(size)
    
#     file = open(os.path.join(os.path.dirname(__file__),f"result/exercise_4/Connected_compt_table_S{S}.txt"),"w")
#     file = open(os.path.join(os.path.dirname(__file__),f"result/exercise_4/Connected_compt_table_S{S}.txt"),"a")
#     file.write(f"Number of Connected_components : {len(list(nx.connected_components(G)))}\n")
    
#     for island in relative_size:
#         file.write(f"relative size : {island}\n")
#     file.close()


# --------------PART_FOUR.SIX-------------- #

# N=100
# mean=np.zeros(21)
# for i in range(N):
#     mean += np.array(evolution(1,animation=False))
# mean =mean/N    
# print(mean)


# value_f = np.arange(0,1.05,0.05)


# plt.plot(value_f*100,mean)
# plt.title(f"average evolution of c after {N} simulations")
# plt.xlabel("percentage of nodes removed")
# plt.ylabel("average of c")

# plt.show()


# --------------EXERCICE-2-------------- #

Beta=0.5
mu=0.5
Max_step=100

G=Data(1)[6]
A=len(G)

f=np.random.random()

I=attack(G,A,f)

nodes = list(G.nodes())
nodes_state = {}
for n in nodes:
    nodes_state[n] = nodes_state.get(n, 0)

for n in list(I.nodes()):
    nodes_state[n] = 1
nodes_state_counter = nodes_state.copy()
for key, value in nodes_state.items():
        if value == 0:
            nodes_state_counter[key] = list()
        else:
            nodes_state_counter[key] = [1]
l=[]
time_step=0
nb_i=[]
while time_step < Max_step :
    random_node = np.random.choice(nodes)
    nodes.remove(random_node)
    if nodes_state[random_node] == 1:
        for neighbors in G.neighbors(random_node):
            proba_i=np.random.random()
            
            if proba_i <= Beta: 
                nodes_state[neighbors] = 1
                nodes_state_counter[neighbors].append(1)
            proba_s=np.random.random()
            if proba_s <= mu:
                nodes_state[neighbors] = 0
                nodes_state_counter[neighbors].append(0)
    time_step += 1
    #print("state =",nodes_state["TYRION"])
    l.append(nodes_state["TYRION"])
    nb_i.append(list(nodes_state.values()).count(1))


time=np.linspace(0,time_step,100)

#print("counter =",nodes_state_counter["TYRION"])
#print(l)
# it=0
# a=l[0]
# for i in l[1:]:
    
#     if a != i:
#         it +=1
#     a=i

# if it == 1:
#     print(it)
# else:
#     print(it-1)

# #print("function =",(np.diff(l)!=0).sum())

# for v in nodes_state_counter.values():
#     if v != list():
#         print(count(v))
