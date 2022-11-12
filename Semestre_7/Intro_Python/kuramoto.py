import numpy as np

N=15

Ksup=np.zeros((N,N))

for i in range(N):
    for j in range(N):
        if j > i:
            Ksup[i][j] = 1
            


K = np.transpose(Ksup)+Ksup




W= 2 *np.pi *np.random.rand(1,N)



theta = 2 *np.pi *np.random.rand(1,N)


def F(x,y0,N):
  
 
    return x




theta_point=[]
for i in range(0,N):
    non_lin_coupling =0
    for j in range(0,N):
    
        non_lin_coupling +=  K[i][j] * np.sin(theta[0][j]-theta[0][j])   
    theta_point.append(W[0][i] + (1/N)*(non_lin_coupling))
        
        
    


x=np.array([1,
            2,
            ])
 
def RK4(t0,tf,y0,N):
    """_summary_

    Args:
        t0 (_type_): _description_
        tf (_type_): _description_
        y0 (_type_): _description_
        N (_type_): _description_

    Returns:
        _type_: _description_
    """        
        y=(y0)
        x=[t0]
        t_n=0
        h=(tf-t0)/N
        for i in range(0,N-1):
            K1=F(y[i])
            K2=F(y[i]+K1*h/2)
            K3=F(y[i]+K2*h/2)
            K4=F(y[i]+K3*h)
            y.append(y[i] +( K1 + 2*K2 + 2*K3 +K4 )*h/6)   
            t_n += h
            x.append(t_n)
        return x , y

def new_func(y0):
    y=[y0]
    return y
    
    


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
