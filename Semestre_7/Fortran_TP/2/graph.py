import matplotlib.pyplot as plt
import numpy as np
import os


a=np.sqrt((2*4159.48-8083.20)/(2*60.8))
b=((8083.20-2*4159.48)/(a*(8083.20-3*4159.48)))**2
Vo=60.8/b

print("a=",a)
print("b=",b)
print("Vo=",Vo)


#------------ Question_1 ------------

l=[-0.95,-0.85,-0.75,-0.65,-0.58,-0.50,-0.40,-0.35,-0.30,-0.25,-0.20]

fig = plt.figure()
for i in range(1,9):
    loc="24"+str(i)
    plt.subplot(int(loc))
    path1=os.path.join(os.path.dirname(__file__),"Result/Q1/mywavefunction"+str(i)+".txt")
    DATA=np.loadtxt(path1,delimiter=",")
    plt.plot(DATA[:,0],DATA[:,1])
    plt.title(f"Psi for e ={l[i]}")


plt.subplots_adjust()
plt.show()


#------------ Question_2 ------------

for v in range(0,2):
    plt.plot([-(1-a*np.sqrt(b)*(v+0.5))**2]*100,np.linspace(0,10,100),label=f"vibrational level {v}")
path2=os.path.join(os.path.dirname(__file__),"Result/Q2/Q2.txt")

DATA=np.loadtxt(path2,delimiter=",")
plt.plot(DATA[:,0],DATA[:,1])
plt.title("Number of iteration in fonction starting energie")
plt.ylabel("NB iteration")
plt.xlabel("Starting energie")
plt.legend()
plt.show()


#------------ Question_3 rn ------------
plt.subplot(121)
path2=os.path.join(os.path.dirname(__file__),"Result/Q3/Q3_rn.txt")
DATA=np.loadtxt(path2,delimiter=",")
plt.plot(DATA[:,0],DATA[:,1])
plt.title("Number of iteration in fonction of rn")
plt.ylabel("NB iteration")
plt.xlabel("rn")



plt.subplot(122)
plt.plot(DATA[:,0],DATA[:,2])
plt.plot(DATA[:,0],[-(1-a*np.sqrt(b)*(10+0.5))**2]*len(DATA[:,0]),label="v10")
plt.title("Energy reached in fonction of rn")
plt.ylabel("energy reached")
plt.xlabel("rn")
plt.legend()
plt.show()

#------------ Question_3 r0 ------------
plt.subplot(121)
path2=os.path.join(os.path.dirname(__file__),"Result/Q3/Q3_r0.txt")
DATA=np.loadtxt(path2,delimiter=",")
plt.plot(DATA[:,0],DATA[:,1])
plt.title("Number of iteration in fonction of r0")
plt.ylabel("NB iteration")
plt.xlabel("r0")





plt.subplot(122)
plt.plot(DATA[:,0],DATA[:,2])
plt.plot(DATA[:,0],[-(1-a*np.sqrt(b)*(0 +0.5))**2]*len(DATA[:,0]),label='v0')
plt.title("Energy reached in fonction of r0")
plt.ylabel("energy reached")
plt.xlabel("r0")
plt.legend()
plt.show()

#------------ Question_3 eps ------------
plt.subplot(121)
path2=os.path.join(os.path.dirname(__file__),"Result/Q3/Q3_eps.txt")
DATA=np.loadtxt(path2,delimiter=",")
plt.plot(DATA[:,0],DATA[:,1])
plt.title("Number of iteration in fonction of eps")
plt.ylabel("NB iteration")
plt.xlabel("eps")





plt.subplot(122)
plt.plot(DATA[:,0],DATA[:,2])
plt.plot(DATA[:,0],[-(1-a*np.sqrt(b)*(10 +0.5))**2]*len(DATA[:,0]),label="v10")
plt.title("Energy reached in fonction of eps")
plt.ylabel("energy reached")
plt.xlabel("eps")
plt.legend()
plt.show()

# ------------ Question_3 tol ------------


plt.subplot(121)
path2=os.path.join(os.path.dirname(__file__),"Result/Q3/Q3_tol.txt")
DATA=np.loadtxt(path2,delimiter=",")
plt.plot(DATA[:,0],DATA[:,1])
plt.title("Number of iteration in fonction of tol")
plt.ylabel("NB iteration")
plt.xlabel("tol")




plt.subplot(122)
plt.plot(DATA[:,0],DATA[:,2])
plt.plot(DATA[:,0],[-(1-a*np.sqrt(b)*(10 +0.5))**2]*len(DATA[:,0]),label="v10")
plt.title("Energy reached in fonction of tol")
plt.ylabel("energy reached")
plt.xlabel("tol")
plt.legend()
plt.show()




#------------ Question_4 ------------

path2=os.path.join(os.path.dirname(__file__),"Result/Q4/Q4.txt")

for v in range(0,11):
    print(-(1-a*np.sqrt(b)*(v+0.5))**2)
    plt.plot([-(1-a*np.sqrt(b)*(v+0.5))**2]*100,np.linspace(-0.02,0.02,100),label=f"v{v}")


DATA=np.loadtxt(path2,delimiter=",")

plt.plot(DATA[:,0],DATA[:,1],color='b',linestyle='--', marker='o')
plt.title("Q4")
plt.ylabel("de")
plt.xlabel("Starting value")
plt.legend()
plt.show()