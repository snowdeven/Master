import math as m

#déclaration des variables

nbpeas = 500000000
Boxes=[]
i=1
#find nb of facto of peas

while nbpeas > 0:
    if nbpeas -m.factorial(i) < 0 :
        nbpeas -= m.factorial(i-1)
        Boxes.append((i-1))
        i = 1
    else:
        i += 1
        
        
for i in set(Boxes):
    
    print( Boxes.count(i), "boxes of",str(i) +"!")

      
      

    
        
        