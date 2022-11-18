### LIBRARY  ###
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import warnings
warnings.filterwarnings("ignore")

### DATA ###


with open("Links.dat", "r") as f:
    SOURCE = list()
    TARGET = list()
    for line in f:
        if "#" in line:
            # on saute la ligne
            continue
        data = line.split()
        SOURCE.append(data[0])
        TARGET.append(data[1])

with open("Nodes.dat", "r") as f:
    ID = list()
    LABEL = list()
    for line in f:
        if "#" in line:
            # on saute la ligne
            continue
        data = line.split()
        ID.append(data[0])
        LABEL.append(data[1])


e=zip(SOURCE[1:],TARGET[1:])

### GRAPH ###

G=nx.MultiDiGraph() #création d'un graphe orienté

G.add_nodes_from((ID[1:]))
G.add_edges_from(e)


pos=nx.spring_layout(G)
# nx.draw_networkx(G,pos=pos)
# plt.show()

### ADJ_MATRIX ###

Mat_adj_ex=np.zeros((6,6))

for i in range(1,len(SOURCE)):
    a=int(SOURCE[i])
    b=int(TARGET[i])
    Mat_adj_ex[a-1,b-1]=1
    Mat_adj_ex[b-1,a-1]=1
    
    
G=nx.from_numpy_array(Mat_adj_ex)
nx.draw_networkx(G)
plt.show()

Mat_adj_th=nx.adjacency_matrix(G)



print("adjacency matrix is ",np.all(Mat_adj_ex == Mat_adj_th))

### DEGREE ###

IN_DEGRE=np.zeros(6)
OUT_DEGRE=np.zeros(6)


for i in range(6):
    IN_DEGRE[i]=sum(Mat_adj_ex[i,:])
    OUT_DEGRE[i]=sum(Mat_adj_ex[:,i])


T_DEGREE_th=nx.degree(G)

print(IN_DEGRE,T_DEGREE_th)


### SH_PATH ###


M_sh_path_ex=np.zeros((6,6))


for i in range(6):
    for j in range(6):
        V=np.zeros((6,1))
        V[i]=1
        it=0
        if i == j :
            M_sh_path_ex[i,j]=0
            break
        else:
            while V[j] == 0:
                
                V =np.dot(Mat_adj_ex,V)
                
                it += 1
                if it > nx.diameter(G) :
                    break
        M_sh_path_ex[i,j]=it
        M_sh_path_ex[j,i]=it

print(M_sh_path_ex)

M_sh_path_th=dict(nx.shortest_path_length(G))
print(M_sh_path_th)


### CLOSENESS ###

Clo_ex=np.zeros(6)

for i in range(6):
    
    Clo_ex[i]=5 *sum(M_sh_path_ex[i])**-1


print(sum(M_sh_path_ex[1]))

print(*Clo_ex)

Clo_th=nx.closeness_centrality(G)


print(Clo_th)


### BETWEENESS ###

Bet=nx.betweenness_centrality(G,normalized=False)

print(Bet)