import networkx as nx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


i=str(1)


file="TP_network/GOTVID19/data/got-s"+i+"-nodes.csv"



x=pd.read_csv(file)
y=pd.read_csv("TP_network/GOTVID19/data/got-s1-edges.csv")





e=x[['Id']]

z=e.to_dict()
x=x.to_numpy()

y=y.to_numpy()


y=y[:,:2]
m=np.shape(x[:,0])

Name=list(x[:,0])
mat_adj=np.zeros((m[0],m[0]))




for i in range(m[0]):
    a=Name.index(y[i,0])
    b=Name.index(y[i,1])
    
    mat_adj[a,b]=1
    mat_adj[b,a]=1







G=nx.from_numpy_array(mat_adj)
G=nx.relabel_nodes(G,z)
nx.draw_networkx(G)
plt.show()









