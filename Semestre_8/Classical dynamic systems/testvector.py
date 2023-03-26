import numpy as np

v=200
n=v**2
x = np.random.rand(v, v)+1j*np.random.rand(v, v)
y = np.random.rand(v, v)+1j*np.random.rand(v, v)
print(np.shape(x)[0])
# E=np.dot(x,y)
x=x.ravel()
y=y.ravel()
z=np.zeros(n,dtype='complex_')
m=0
it=0
for i in range(v):
    for k in range(v):
        z[it]=sum([x[j+m]*y[k+v*j] for j in range(v)])
        it +=1
    m+= v

# print(E.ravel()== z)
# print(E.ravel())
# print(z)
# print(E.ravel() - z)




