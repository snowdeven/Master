import numpy as np
import matplotlib.pyplot as plt

    
t0=0 #time at t=0
tf=10#time at the end of simulation
y0=1 #initial condition
N=30 #number of step between t0 and tf

###### definding all the integrator needed ######

def F(y):#definding the differential equation
    return y

def euler(t0,tf,y0,N):
        
        y=[y0]# y initial condition
        x=[t0]# x initial condition
        t_n=0
        h=(tf-t0)/N #step of the algorithmm 
        for i in range(0,N-1):# calculation for all the time axis
            y.append(y[i] + F(y[i])* h)   # y value at time t+1
            t_n += h
            x.append(t_n)# x value  t+1
        return x , y # return our both axis 
    
def RK2(t0,tf,y0,N):
        
        y=[y0]# y initial condition
        x=[t0]# x initial condition
        t_n=0
        h=(tf-t0)/N #step of the algorithmm 
        for i in range(0,N-1):# calculation for all the time axis
            y.append(y[i] + F(y[i]+F(y[i])*h/2)*h)   # y value at time t+1
            t_n += h
            x.append(t_n)# x value  t+1
        return x , y # return our both axis 
    
def RK4(t0,tf,y0,N):
        
        y=[y0]# y initial condition
        x=[t0]# x initial condition
        t_n=0
        h=(tf-t0)/N #step of the algorithmm 
        for i in range(0,N-1):# calculation for all the time axis
            K1=F(y[i])
            K2=F(y[i]+K1*h/2)
            K3=F(y[i]+K2*h/2)
            K4=F(y[i]+K3*h)
            y.append(y[i] +( K1 + 2*K2 + 2*K3 +K4 )*h/6)    # y value at time t+1
            t_n += h
            x.append(t_n) # x value  t+1
        return x , y # return our both axis 
    
###### plot the results for each oscillator ######

x=np.linspace(t0,tf,N) #x-axis for the exactly solution

plt.plot(x,np.exp(x),color='r',label='Exact solution')#excat solution for F(y)

plt.plot(euler(t0,tf,y0,N)[0],euler(t0,tf,y0,N)[1],color='r',label='euler')
plt.plot(RK2(t0,tf,y0,N)[0],RK2(t0,tf,y0,N)[1],color='b',label='RK2')
plt.plot(RK4(t0,tf,y0,N)[0],RK4(t0,tf,y0,N)[1],color='g',label='RK4')
plt.ylabel("Value of y")
plt.xlabel("Time in second")
plt.legend()

plt.show()


