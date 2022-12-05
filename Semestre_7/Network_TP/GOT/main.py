import networkx as nx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from settings import *
from function import *


s=8




G=data(s)[6]

# Draw_graph(s,G)










for i in range(1,9):
    loc="24"+str(i)
    plt.subplot(int(loc))
    G=data(i)[6]
    plt.title("season_"+str(i))
    nx.draw(G,node_size=15)
    stats(i,G)

plt.show()

