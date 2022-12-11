
import numpy as np
import matplotlib.pyplot as plt
from function import *


# --------------PART_TWO--------------#

for S in range(1,9):             #we made a loop to compute all the data for each season
    loc="24"+str(S)              #localisation of the subplot
    plt.subplot(int(loc))
    G=Data(S)[6]                 #our function data that retrun the network in position 6
    plt.title(f"season_S{S}")
    d=nx.degree_centrality(G)
    pos = nx.spring_layout(G,k=2,iterations=100)
    nx.draw_networkx(G,pos,with_labels=True
                    ,node_color=houses_colors(G,S)
                    ,node_size=[d[k]*500 for k in d]
                    ,width=[d[k]*3 for k in d]
                    ,edge_color='gray'
                    ,font_size=4)                #We draw the Graph
    Txt_imp_char(S,5,G)          #We write a file of most important character of the season S
    Txt_stats(S,G)                               #We write a file of all the stats for the character of the season S
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


plt.show()

#--------------PART_FOUR-------------- #

for S in range(1,9):#we made a loop to compute all the data for each season
    G=Data(S)[6]
    C=nx.connected_components(G)
    
    size=[len(c) for c in sorted(nx.connected_components(G), key=len, reverse=True)]
    
    if len(list(nx.connected_components(G))) > 1 :
        sub=[G.subgraph(c).copy() for c in nx.connected_components(G) ][1]
        Id=list(list(C)[1])
        d=nx.degree_centrality(sub)
        nx.draw_networkx(sub,with_labels=True
                        ,node_color=houses_colors(sub,S)
                        ,node_size=[d[k]*500 for k in d]
                        ,width=[d[k]*3 for k in d]
                        ,edge_color='gray'
                        ,font_size=7)
        plt.show()
    relative_size=np.array(size)/sum(size)
    
    file = open(os.path.join(os.path.dirname(__file__),f"result/exercise_4/Connected_compt_table_S{S}.txt"),"w")
    file = open(os.path.join(os.path.dirname(__file__),f"result/exercise_4/Connected_compt_table_S{S}.txt"),"a")
    file.write(f"Number of Connected_components : {len(list(nx.connected_components(G)))}\n")
    
    for island in relative_size:
        file.write(f"relative size : {island}\n")
    file.close()


# # --------------PART_FOUR.SIX-------------- #
S=1
G=Data(S)[6]
N=100
pos = nx.spring_layout(G,k=1.5,iterations=100)
mean=np.zeros(21)
for i in range(N):
    mean += np.array(evolution(G,S,pos,N))
mean =mean/N    



value_f = np.arange(0,1.05,0.05)

plt.plot(value_f*100,mean)
plt.title(f"average evolution of c after {N} simulations")
plt.xlabel("percentage of nodes removed")
plt.ylabel("average of c")

plt.show()

#--------------EXERCICE-2-------------- #
time=np.linspace(0,100,100)
mean=np.zeros(100)
parameters=((0.5,0.5),(0.3,0.7),(0.7,0.3))
Nb=1000

w_matrix=Mat_adj(1,True)
nb_i=np.zeros(100)
G = Data(1)[6]
Id = Data(1)[0]
S=1
for beta,mu in parameters:
    mean=np.zeros(100)
    for i in range(Nb):
        f=np.random.random()
        mean += covided(beta,mu,f,w_matrix,Id,G,nb_i,1,False)[2]
    print(f"computation for {beta,mu} finish")
    plt.plot(time,mean/Nb,label=f'{beta,mu}')
    file = open(os.path.join(os.path.dirname(__file__),f"result/Part_2/Covid_stats-end-S{S}-{beta,mu}.txt"),"w")#"w" to open a file and erase the previous data if he is already exsit
    file = open(os.path.join(os.path.dirname(__file__),f"result/Part_2/Covid_stats-end-S{S}-{beta,mu}.txt"),"a")#"a" to open a file and add the data after the previous one
    file.write(f"Name,number of time being infected\n")
    for item, val in covided(beta,mu,f,w_matrix,Id,G,nb_i,1,False)[1]:
        file.write(f"{item},{val}\n")


plt.legend()
plt.show()





