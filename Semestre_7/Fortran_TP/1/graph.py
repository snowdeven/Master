import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')

DATA=np.loadtxt("result.txt",delimiter=",")

print(DATA)


plt.scatter(DATA[:,2],DATA[:,0],s=35,
            facecolors="None",edgecolors='b',
            label="data")
plt.plot(DATA[:,2],DATA[:,1],label="fit")
plt.plot(DATA[:,2],DATA[:,3],label="fit weighted")



plt.legend()
plt.show()


