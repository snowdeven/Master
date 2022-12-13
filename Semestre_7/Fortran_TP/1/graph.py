import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes

plt.style.use('ggplot')


# for i in range(1,6):
#     ax1 = plt.subplot(2, 3, i)
#     file="result_"+str(i)+".txt"
#     DATA=np.loadtxt(file,delimiter=",")
    
#     plt.scatter(DATA[:,2],DATA[:,0],s=35,
#                 facecolors="None",edgecolors='b',
#                 label="data")
#     plt.plot(DATA[:,2],DATA[:,1],label="fit")
#     plt.plot(DATA[:,2],DATA[:,3],label="fit weighted")

#     plt.legend()

# plt.show()



DATA=np.loadtxt("regr_gamma.txt",delimiter=",")

plt.scatter(DATA[:,0],DATA[:,1])
x=np.linspace(-1,16,100)
plt.plot(x,DATA[1,2]*x +DATA[1,3])
plt.show()

DATA=np.loadtxt("regr_omega.txt",delimiter=",")

plt.scatter(DATA[:,0],DATA[:,1])
x=np.linspace(-1,16,100)
plt.plot(x,DATA[1,2]*x +DATA[1,3])
plt.show()
