import numpy as np
import matplotlib.pyplot as plt
from function import *
import networkx as nx


# --------------PART_TWO--------------#

fig = plt.figure(dpi=300)

for S in range(1,9):             #we made a loop to compute all the data for each season
    loc="24"+str(S)              #localisation of the subplot
    plt.subplot(int(loc))
    G=Data(S)[6]                 #our function data that retrun the network in position 6
    plt.title(f"Season {S}", size=4)
    d=nx.degree_centrality(G)
    pos = nx.spring_layout(G,k=2,iterations=100)
    nx.draw_networkx(G,pos,with_labels=True
                    ,node_color=houses_colors(G,S)
                    ,node_size=[d[k]*100 for k in d]
                    ,width=[d[k]*3 for k in d]
                    ,edge_color='gray'
                    ,font_size=1.5)                #We draw the Graph
    Txt_imp_char(S,5,G)          #We write a file of most important character of the season S
    Txt_stats(S,G)                               #We write a file of all the stats for the character of the season S

plt.suptitle("GOT-NET for each season", size=8)

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
        file = open(os.path.join(os.path.dirname(__file__),"result/exercise_3/Weighted_most_imp_char_S1-S8.txt"),"w")
    else:
        file = open(os.path.join(os.path.dirname(__file__),"result/exercise_3/Weighted_most_imp_char_S1-S8.txt"),"a")
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

# Create a figure with a specific size and dpi

fig, ax = plt.subplots(2, 4, sharex='col', sharey='row')

for S in range(1,9):#we made a loop to compute all the data for each season
    Colors=["royalblue"]
    loc=f"24{S}"   #localisation of the subplot
    plt.subplot(int(loc))
    Hist_Weight(S)

plt.suptitle("Distribution of the links weight for each season")

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
        plt.title(f"Season {S} Smallest Connected Components")

        plt.show()
    relative_size=np.array(size)/sum(size)
    
    file = open(os.path.join(os.path.dirname(__file__),f"result/exercise_4/Connected_compt_table_S{S}.txt"),"w")
    file = open(os.path.join(os.path.dirname(__file__),f"result/exercise_4/Connected_compt_table_S{S}.txt"),"a")
    file.write(f"Number of Connected_components : {len(list(nx.connected_components(G)))}\n")
    
    for island in relative_size:
        file.write(f"relative size : {island}\n")
    file.close()


# # --------------PART_FOUR.FOUR-------------- #
G=Data(S=1)[6]



# N=1 ex4.4 & N=100 ex4.6
for N in (1, 100):
    value_f = np.arange(0, 1.05, 0.05)
    average_c = average_of_c_for_f(G, N)
    fig, ax = plt.subplots()
    ax.plot(value_f, average_c, '-*')

    plt.xlabel("percentage of nodes removed")
    plt.ylabel("Average of c")
    if N == 1:
        plt.title("Evolution of |c| with the fraction of attacked nodes f")

    else:
        plt.title("Evolution of |c| with the fraction of attacked nodes f after 100 samples")


    plt.show()

#--------------EXERCICE-2-------------- #
time=np.linspace(0,100,100)
mean=np.zeros(100)
parameters=((0.5,0.5),(0.3,0.7),(0.7,0.3))
Nb=1000

w_matrix=Mat_adj(1,True)

G = Data(1)[6]
Id = Data(1)[0]
S=1

# create the initail infected list, and a final list whith how much each character got infected
for beta,mu in parameters:
    f = np.random.random()
    file = open(os.path.join(os.path.dirname(__file__), f"result/Part_2/Covid_stats-end-S{S}-{beta, mu}.txt"),
                "w")  # "w" to open a file and erase the previous data if he is already exsit
    file = open(os.path.join(os.path.dirname(__file__), f"result/Part_2/Covid_stats-end-S{S}-{beta, mu}.txt"),
                "a")  # "a" to open a file and add the data after the previous one
    file.write(f"Name,number of time being infected\n")
    for item, val in covided(beta, mu, f, w_matrix, Id, G,  1, False)[1]:
        file.write(f"{item},{val}\n")

# create the initial infected list, and a final list whith how much each character got infected (Weighted)
for beta,mu in parameters:
    f = np.random.random()
    file = open(os.path.join(os.path.dirname(__file__), f"result/Part_2/Covid_stats-end-S{S}-{beta, mu}_weighted.txt"),
                "w")  # "w" to open a file and erase the previous data if he is already exsit
    file = open(os.path.join(os.path.dirname(__file__), f"result/Part_2/Covid_stats-end-S{S}-{beta, mu}_weighted.txt"),
                "a")  # "a" to open a file and add the data after the previous one
    file.write(f"Name,number of time being infected\n")
    for item, val in covided(beta, mu, f, w_matrix, Id, G,  1, True)[1]:
        file.write(f"{item},{val}\n")

covid_plot(False)
covid_plot(True)




