import matplotlib.pyplot as plt
import numpy as np



DATA=np.loadtxt("result.txt",delimiter=",")

print(DATA)


plt.scatter(DATA[:,2],DATA[:,0],marker=".")
plt.plot(DATA[:,2],DATA[:,1])



plt.show()


