import numpy as np
import matplotlib.pyplot as plt




################  declarating variables ################


N=100#numbers of oscillators 
tf=30#time of the simulation 
t0=0 #time of the beginning of the simultaion
t=0 
nb=500# number of steps
kappa=3 #coefficient of coupling
M = 25 # the nearest neighbour
Open=False
################ compute usefull variables ################

h=(tf-t0)/nb #steps of the simulation
A=np.zeros((N,nb)) #declaring the matrix of theta
t_n= np.linspace(t0,tf,nb) #declaring axe of time

A[:,0]=2 *np.pi *np.random.rand(N)# add the initial condition to matrix theta

W=np.random.normal(0.5,0.5,N)#declaring the initial pulsation

#declaring the matrix of coupling

K=np.zeros((N,N)) #matrix of zeros
for i in range(N):
    l=np.arange(i-M,i+M+1) # list of all the link with the parameter M
    
    for j in l:
        if Open == False: #parameter define closed or open case
            K[i,j%N] = kappa # % to keep the good index at border on your chain 
           
            if i == j: # set up all the diagonal at zero because an oscillator can't be coupled with himself 
                K[i,j]=0
        else:
            if j >= 0 and j <= N-1 and i!=j: # condition to set the diagonal at zero and
               K[i,j] = kappa                # to set j at  or N-1 when he is out of range
           
################ definition of integrate methode for differential equations ################



def F(x,Y,i,time):
    #this is te definition of the differential equation
    #we do a matrix product to save time  
    return (W[i] + (1/N)*(K[i,:] @ np.sin(Y[:,time]-x)))


def RK4_t(Y,time,i,h) :#Y is the Theta matrix , i is le rows of theta matrix and h is the step of simulation
    #definition of runge-kutta order 4 to solve the differential equation
    K1=F(Y[i][time],A,i,time)
    K2=F(Y[i][time]+K1*(h/2),A,i,time)
    K3=F(Y[i][time]+K2*(h/2),A,i,time)
    K4=F(Y[i][time]+K3*h,A,i,time) 
    return (Y[i][time] +( K1 + 2*K2 + 2*K3 +K4 )*(h/6))

################ computing value theta  for each oscilator at each time steps ################
    

for T in range(1,nb): # list of time
    for i in range(N): #list of oscillators
        A[i,T] = (RK4_t(A,T-1,i,h)) % (2*np.pi) # % 2 np.pi to module value


################ plot the value of theta in time ################

for i in range(0,N):
    plt.plot(t_n,A[i,:])


plt.title("phase for each oascillators along time")
plt.xlabel('time in second')
plt.ylabel('phase of each oscillators')
plt.grid()
plt.show()

# # # ################ plot the value oh phi ################
            
            
            
psi=[] #empty list
for i in range(0,nb): #list of time
      psi.append(np.mean(A[:,i])) # we did the average on theta for one time
     
     
     
plt.figure(dpi=200)

plt.plot(t_n,psi)
plt.title("phi along time")
plt.ylabel("average phase ")
plt.xlabel('time in second')
plt.grid()
plt.show()
 
 
# ################ plot R in time ################
    

plt.figure(dpi=200)
    
R=np.abs([ 1/N *sum(np.exp((A[:,i]*1j))) for i in range(0,nb)]) #np.abs() do the modulus and 1j is the i-complexe in python

plt.plot(t_n,R)
    
    
plt.ylim(0,2)
plt.title("R along time")
plt.xlabel('time in second')
plt.ylabel('value of R')
plt.grid()
plt.show()


################ plot entropy of i-th oscillator ################


def entropy_1D(i, n, t): # define function to compute S for i_th oscillaotrs at time t
    s = 0

    q = 100
    for a in range(q):  # we browse a list betxeen a until q

        nb_theta = 0# set nb of theta k at 0
        for k in range(i-n, i+n): # we browse the list of k label

            if k < 0:  # when k is smaller than 0 we set it at 0

                k = 0
            if k > N-1: # when k is greater than N-1  we set it at N-1

                k = N-1

            if A[k, t] >= (2*np.pi*a)/q and A[k, t] < (2*np.pi*(a+1))/q: #we count how many theta K are in the interval

                nb_theta += 1 # iteration on number of theta in the interval

        if nb_theta == 0: # condition to not have an error with ln when theta is equal to zero
            s += 0
        else:
            s += -1*((nb_theta)/(2*n+1)) * np.log(nb_theta/(2*n+1)) #the equation of entropy

    return s


plt.figure(dpi=200)

Stot = np.zeros((N, nb)) #define a matrix of entropy

for i in range(N): # we browse our list of oscillators
    S = [] #list of entropy for one oscillator along time
    for t in range(nb): # we browse our list of time
      x = entropy_1D(i, M, t) #call the entropy function
      S.append(x) #put the value of entropy in our list 
      Stot[i, t] = x   #put the value of entropy in our list matrix

    plt.plot(t_n, S) #plot the entropy for one oscillator along time



plt.title("Plot of the entropy along time")
plt.xlabel('time in second')
plt.ylabel('value of S')
plt.grid()
plt.show()


plt.figure(dpi=200)
labelosc = [i for i in range(0, N)] # define a list of index for oscillators

plt.pcolormesh(t_n, labelosc,  Stot) #we use pcolormesh to save 
                                      #our poor memory bescause this is more
                                      #optimise than pcolor
plt.colorbar()

plt.title("Plot of the density graph of the entropy")
plt.ylabel('index of oscillators')
plt.xlabel('time in second ')
plt.show()

plt.figure(dpi=200)
labelosc = [i for i in range(0, N)] # define a list of index for oscillators

plt.pcolormesh(t_n, labelosc, A) #we use pcolormesh to save 
                                      #our poor memory bescause this is more
                                      #optimise than pcolor
plt.colorbar()

plt.title("Plot of the density graph of the phase")
plt.ylabel('index of oscillators')
plt.xlabel('time in second ')
plt.show()




# circle= np.linspace(0,2*np.pi,nb)

# for i in range(nb):
#     plt.plot(np.cos(circle),np.sin(circle),linewidth=0.5)
#     plt.scatter(np.cos(A[:,i]),np.sin(A[:,i]),cmap='gray')
#     plt.scatter(np.mean(np.cos(A[:,i])),np.mean(np.sin(A[:,i])))
#     plt.pause(0.01)
#     plt.clf()




# plt.xlim(-1,1)
# plt.ylim(-1,1)
# plt.show()






