import networkx as nx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from settings import *
from function import *

# --------------PART_TWO--------------#

for S in range(1,9):                         #we made a loop to compute all the data for each season
    loc="24"+str(S)                          #localisation of the subplot
    plt.subplot(int(loc))
    G=Data(S)[6]                             #our function data that retrun the network in position 6
    plt.title("season_"+str(S))
    nx.draw(G,node_size=15,with_labels=False) #We draw the Graph
    Txt_imp_char(S,5,G)          #We write a file of most important character of the season S
    Txt_stats(S,G)                               #We write a file of all the stats for the character of the season S


plt.savefig(os.path.join(os.path.dirname(__file__),f"result/exercise_2/Graph_S1-S8.png"))
plt.show()


# --------------PART_THREE--------------#



for S in range(1,9):
    Name=Data(S)[0]
    W_degree=np.zeros(len(Name))

    mat_adj=Mat_adj(S,Weighted=True)
    for i in range(len(Name)):
        W_degree[i]=sum(mat_adj[i,:])

    sort_index=np.argsort(W_degree)[::-1]
    if S == 1:
        file = open(os.path.join(os.path.dirname(__file__),"result/exercise_3/Weighted_most_imp_char_S1-S9.txt"),"w")
    else:
        file = open(os.path.join(os.path.dirname(__file__),"result/exercise_3/Weighted_most_imp_char_S1-S9.txt"),"a")
    Title=f"| Weighted_degree_centrality season {S} |"
    file.write("-"*len(Title)+"\n"+Title +"\n"+"-"*len(Title)+"\n")
    file.write("Name,Value\n")
    for i in sort_index[:5]:
        file.write(Name[i]+","+str(W_degree[i])+"\n")
    
    file = open(os.path.join(os.path.dirname(__file__),f"result/exercise_3/Char_weighted_degree_S{S}.txt"),"w")
    file = open(os.path.join(os.path.dirname(__file__),f"result/exercise_3/Char_weighted_degree_S{S}.txt"),"a")
    file.write("Name,Value\n")
    for count, elem in enumerate(W_degree):
        file.write(Name[count]+ f", {elem}"+"\n")
    file.close()

for S in range(1,9):#we made a loop to compute all the data for each season
    Colors=["royalblue"]
    loc=f"24{S}"   #localisation of the subplot
    plt.subplot(int(loc))
    Hist_Weight(S)


plt.savefig(os.path.join(os.path.dirname(__file__),f"result/exercise_3/Weight_distribution_S1-S8.png"))

plt.show()

# --------------PART_FOUR-------------- #

for S in range(1,9):
    G=Data(S)[6]

    C=nx.connected_components(G)


    size=[len(c) for c in sorted(nx.connected_components(G), key=len, reverse=True)]

    relative_size=np.array(size)/sum(size)
    file = open(os.path.join(os.path.dirname(__file__),f"result/exercise_4/Connected_compt_table_S{S}.txt"),"w")
    file = open(os.path.join(os.path.dirname(__file__),f"result/exercise_4/Connected_compt_table_S{S}.txt"),"a")
    file.write(f"Number of Connected_components : {len(list(C))}\n")
    for island in relative_size:
        file.write(f"relative size : {island}\n")
    file.close()


