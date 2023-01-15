
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

##############################################################################
#                                                                            #
#                          ###################                               #
#                          #     FUNCTION    #                               #
#                          ###################                               #
#                                                                            #
##############################################################################
def fibo(n):
    """Function for fibonnaci numbers

    Args:
        n (integer): n fibonnaci numbers 

    Returns:
        fibo (list) : list of n fibonnaci numbers
    """    
    list=[0,1]
    for i in range(n):
        list.append(list[-2] +list[-1])
    return list
    


def CDH(n):
    """Function to convert n in base 10 to n in base 16
        CDH for Convert Decimal to Hexadecimal

    Args:
        n (integer): number that we want to convert

    Returns:
        r (str): return n in hexadecimal so in str 
    """    
    r=""
    d={0:"0",1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",
        10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
    while True :
        r += d[n%16]
        n = n // 16
        if n == 0 :
            return r[::-1]


def CHD(n):
    """Function to convert n in base 16 to n in base 10
        CHD for Convert Hexadecimal to Decimal

    Args:
        n (str): number that we want to convert

    Returns:
        r (integer): return n in decimal so in integer
    """   
    d={0:"0",1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",
        10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
    d= {v: k for k, v in d.items()}
    r, it = 0, 0
    n=n[::-1]
    for i in n:
        r+= d[i] * 16**it
        it +=1
    return r

##############################################################################
#                                                                            #
#                          ###################                               #
#                          #   QUESTION 5    #                               #
#                          ###################                               #
#                                                                            #
##############################################################################


#compute the Benford's law in base 10
#create dictionnary to have "i_digit" : frequency
it=1 #start at one because we don't take in account 0
ben_d={"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0} #ben_d for Benford's_law_Decimal
for i in ben_d.keys():
    ben_d[i] = np.log10(1+1/it) #add np.log10(1+1/it) for Benford's law in base 10 with it the i_digit
    it += 1

#compute the Benford's law in base 16
#create dictionnary to have "i_digit" : frequency
it=1 #start at one because we don't take in account 0
ben_h={"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0,
        "A":0,"B":0,"C":0,"D":0,"E":0,"F":0} #ben_h for Benford's_law_Hexadecimal
for i in ben_h.keys():
    ben_h[i] = np.log10(1+1/it)/np.log10(16) #add np.log10(1+1/it)/np.log10(16) 
                                             #for Benford's law in base 16 with it the i_digit
    it += 1    

#compute the distribution of first digit for fibonacci numbers in base 10 and 16
N=1000 #number of fibonacci number
#create dictionnary to have "i_digit" : frequency
fd_fib_d={"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0} #fd_fib_d for First_Digit_Fibonacci_Decimal
fd_fib_h={"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0,
            "A":0,"B":0,"C":0,"D":0,"E":0,"F":0} #fd_fib_h for First_Digit_Fibonacci_Hexadecimal

data=fibo(N)
for i in range(1,N):#loop over the number of elements
    nd=str(data[i]) #convert the number into str to get a list and have the first digit by list[0] in base 10
    nh=CDH(data[i]) #convert the number into str to get a list and have the first digit by list[0] in base 16
    fd_fib_d[nd[0]] = fd_fib_d.get(nd[0]) + 1/N #update the values for i digit by 1/N (already normalised) in base 10
    fd_fib_h[nh[0]] = fd_fib_h.get(nh[0]) + 1/N #update the values for i digit by 1/N (already normalised) in base 16

plt.style.use("ggplot") #style for all plot
width = 0.4 #width of bins for all hist

#histogram to compare distribution of first digit for fibonacci number against the Benford's law in base 10
fig, ax = plt.subplots()
x=np.array([i for i in range(1,len(fd_fib_d.keys())+1)]) #list of x_axis
rects1=plt.bar(x, fd_fib_d.values(),width=width, color='b',alpha=0.5,
    label=f"distribution of Fibonacci first digit in base 10 : prob total = {round(sum(fd_fib_d.values()),4)}") #hist for fd_fib_d 
rects2=plt.bar(x+width, ben_d.values(),width=width, color='r',alpha=0.5,
    label=f"Benford's law in base 10 : prob total = {round(sum(ben_d.values()),4)}") #hist for ben_d 
ax.set_xticks(x+width/2, labels=ben_d.keys()) #set the same label for both hist
ax.bar_label(rects1, labels=[f'{i:.1%}' for i in fd_fib_d.values()],fontsize='x-small') #set percent label on each bins for fd_fib_d
ax.bar_label(rects2, labels=[f'{i:.1%}' for i in ben_d.values()],fontsize='x-small') #set percent label on each bins for ben_d
plt.title("Histogram of frequency of first digit for Fibonacci numbers in base 10")
plt.xlabel("First digit")
plt.ylabel("Frequency") 
plt.legend()
plt.show()

#histogram to compare distribution of first digit for fibonacci number against the Benford's law in base 16
fig, ax = plt.subplots()
x=np.array([i for i in range(1,len(fd_fib_h.keys())+1)]) #list of x_axis
rects1=plt.bar(x, fd_fib_h.values(),width=width, color='b',alpha=0.5,
    label=f"distribution of Fibonacci first digit in base 16 : prob total = {round(sum(fd_fib_h.values()),4)}")#hist for fd_fib_h
rects2=plt.bar(x+width, ben_h.values(),width=width, color='r',alpha=0.5,
    label=f"Benford's law in base 16 : prob total = {round(sum(ben_h.values()),4)}") #hist for ben_h
ax.set_xticks(x+width/2, labels=ben_h.keys()) #set the same label for both hist
ax.bar_label(rects1, labels=[f'{i:.1%}' for i in fd_fib_h.values()],fontsize='x-small') #set percent label on each bins for fd_fib_h
ax.bar_label(rects2, labels=[f'{i:.1%}' for i in ben_h.values()],fontsize='x-small') #set percent label on each bins for ben_h
plt.title("Histogram of frequency of first digit for Fibonacci numbers")
plt.xlabel("First digit")
plt.ylabel("Frequency")
plt.legend()
plt.show()

##############################################################################
#                                                                            #
#                          ###################                               #
#                          #   QUESTION 6    #                               #
#                          ###################                               #
#                                                                            #
##############################################################################


# --------- first data set data_beer.csv ---------

#unpack the data from data_beer.csv
path=os.path.join(os.path.dirname(__file__),"data_beer.csv") #path of csv
df=pd.read_csv(path) #unpack with pandas
nb_bar=df['country'].value_counts() #take the colomun that we want 
nb_bar=nb_bar.to_dict() #transform datafram into dictionary

#compute the distribution of first digit for bar per country in base 10 and 16
#create dictionnary to have "i_digit" : frequency
fd_bar_d={"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0} #fd_bar_d for First_Digit_Bar_Decimal
fd_bar_h={"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0,
            "A":0,"B":0,"C":0,"D":0,"E":0,"F":0} #fd_bar_h for First_Digit_Bar_Hexadecimal

for i in nb_bar.keys():#loop over the number of elements
    nd=str(nb_bar[i]) #convert the number into str to get a list and have the first digit by list[0] in base 10
    nh=CDH(nb_bar[i]) #convert the number into str to get a list and have the first digit by list[0] in base 16
    fd_bar_d[nd[0]] = fd_bar_d.get(nd[0]) + 1/len(nb_bar) #update the values for i digit by 1/N (already normalised) in base 10
    fd_bar_h[nh[0]] = fd_bar_h.get(nh[0]) + 1/len(nb_bar) #update the values for i digit by 1/N (already normalised) in base 16

#histogram to compare distribution of first digit for bar per country against the Benford's law in base 10
fig, ax = plt.subplots() 
x=np.array([i for i in range(1,len(fd_bar_d.keys())+1)]) #list of x_axis
rects1=plt.bar(x, fd_bar_d.values(),width=width, color='b',alpha=0.5,
    label=f"distribution of bar per country first digit in base 10 : prob total = {round(sum(fd_bar_d.values()),4)}") #hist for fd_bar_d
rects2=plt.bar(x+width, ben_d.values(),width=width, color='r',alpha=0.5,
    label=f"Benford's law in base 10 : prob total = {round(sum(ben_d.values()),4)}") #hist for ben_d
ax.set_xticks(x+width/2, labels=ben_d.keys()) #set the same label for both hist
ax.bar_label(rects1, labels=[f'{i:.1%}' for i in fd_bar_d.values()],fontsize='x-small')#set percent label on each bins for fd_bar_d
ax.bar_label(rects2, labels=[f'{i:.1%}' for i in ben_d.values()],fontsize='x-small') #set percent label on each bins for fd_bar_d
plt.title("Histogram of frequency of first digit for bar per country")
plt.xlabel("First digit")
plt.ylabel("Frequency")
plt.legend()
plt.show()


#histogram to compare distribution of first digit for bar per country against the Benford's law in base 16
fig, ax = plt.subplots()
x=np.array([i for i in range(1,len(fd_bar_h.keys())+1)]) #list of x_axis
rects1=plt.bar(x, fd_bar_h.values(),width=width, color='b',alpha=0.5,
    label=f"distribution of bar per country first digit in base 16 : prob total = {round(sum(fd_bar_h.values()),4)}") #hist for fd_bar_h
rects2=plt.bar(x+width, ben_h.values(),width=width, color='r',alpha=0.5,
    label=f"Benford's law in base 16 : prob total = {round(sum(ben_h.values()),4)}") #hist for ben_h
ax.set_xticks(x+width/2, labels=ben_h.keys()) #set the same label for both hist
ax.bar_label(rects1, labels=[f'{i:.1%}' for i in fd_bar_h.values()],fontsize='x-small') #set percent label on each bins for fd_bar_h
ax.bar_label(rects2, labels=[f'{i:.1%}' for i in ben_h.values()],fontsize='x-small') #set percent label on each bins for ben_h
plt.title("Histogram of frequency of first digit for bar per country")
plt.xlabel("First digit")
plt.ylabel("Frequency")
plt.legend()
plt.show()

# --------- second data set data_beer2.csv ---------

#unpack the data from data_beer2.csv
path=os.path.join(os.path.dirname(__file__),"data_beer2.csv") #path of csv
df=pd.read_csv(path) #unpack with pandas
nb_bar=df['city'].value_counts() #take the colomun that we want 
nb_bar=nb_bar.to_dict() #transform datafram into dictionary

#compute the distribution of first digit for bar per city in base 10 and 16
#create dictionnary to have "i_digit" : frequency
fd_bar_d={"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0} #fd_bar_d for First_Digit_Bar_Decimal
fd_bar_h={"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0,
            "A":0,"B":0,"C":0,"D":0,"E":0,"F":0} #fd_bar_h for First_Digit_Bar_Hexadecimal

for i in nb_bar.keys(): #loop over the number of elements
    nd=str(nb_bar[i]) #convert the number into str to get a list and have the first digit by list[0] in base 10
    nh=CDH(nb_bar[i]) #convert the number into str to get a list and have the first digit by list[0] in base 16
    fd_bar_d[nd[0]] = fd_bar_d.get(nd[0]) + 1/len(nb_bar) #update the values for i digit by 1/N (already normalised) in base 10
    fd_bar_h[nh[0]] = fd_bar_h.get(nh[0]) + 1/len(nb_bar) #update the values for i digit by 1/N (already normalised) in base 16

#histogram to compare distribution of first digit for bar per city against the Benford's law in base 10
fig, ax = plt.subplots()
x=np.array([i for i in range(1,len(fd_bar_d.keys())+1)]) #list of x_axis
rects1=plt.bar(x, fd_bar_d.values(),width=width, color='b',alpha=0.5,
    label=f"distribution of bar per city first digit in base 10 : prob total = {round(sum(fd_bar_d.values()),4)}") #hist for fd_bar_d
rects2=plt.bar(x+width, ben_d.values(),width=width, color='r',alpha=0.5,
    label=f"Benford's law in base 10 : prob total = {round(sum(ben_d.values()),4)}") #hist for ben_d
ax.set_xticks(x+width/2, labels=ben_d.keys()) #set the same label for both hist
ax.bar_label(rects1, labels=[f'{i:.1%}' for i in fd_bar_d.values()],fontsize='x-small') #set percent label on each bins for fd_bar_d
ax.bar_label(rects2, labels=[f'{i:.1%}' for i in ben_d.values()],fontsize='x-small') #set percent label on each bins for fd_bar_d
plt.title("Histogram of frequency of first digit for bar per city in US")
plt.xlabel("First digit")
plt.ylabel("Frequency")
plt.legend()
plt.show()


#histogram to compare distribution of first digit for bar per city against the Benford's law in base 16
fig, ax = plt.subplots()
x=np.array([i for i in range(1,len(fd_bar_h.keys())+1)]) #list of x_axis
rects1=plt.bar(x, fd_bar_h.values(),width=width, color='b',alpha=0.5,
    label=f"distribution of bar per city first digit in base 16 : prob total = {round(sum(fd_bar_h.values()),4)}")#hist for fd_bar_h
rects2=plt.bar(x+width, ben_h.values(),width=width, color='r',alpha=0.5,
    label=f"Benford's law in base 16 : prob total = {round(sum(ben_h.values()),4)}") #hist for ben_h
ax.set_xticks(x+width/2, labels=ben_h.keys()) #set the same label for both hist
ax.bar_label(rects1, labels=[f'{i:.1%}' for i in fd_bar_h.values()],fontsize='x-small') #set percent label on each bins for fd_bar_h
ax.bar_label(rects2, labels=[f'{i:.1%}' for i in ben_h.values()],fontsize='x-small') #set percent label on each bins for ben_h
plt.title("Histogram of frequency of first digit for bar per city in US")
plt.xlabel("First digit")
plt.ylabel("Frequency")
plt.legend()
plt.show()