import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from time import sleep
from tqdm import tqdm
from mayavi import mlab
import os

plt.style.use("ggplot")
path1=os.path.join(os.path.dirname(__file__),'msd.dat') 


data1=np.loadtxt(path1)

plt.plot(data1[:,0],data1[:,1])
plt.show()