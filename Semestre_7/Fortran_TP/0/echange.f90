program echange
implicit none
real :: a,b,d
a= 5.2
b= 9.3
d=0


print *, 'a contient la valeur',a
print *, 'b contient la valeur',b
d = a
a = b
b = d
print *, 'a contient la valeur',a
print *, 'b contient la valeur',b
end program echange
