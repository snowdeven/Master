program Exercice2
implicit none

real :: a, b, x

a = 5.2
b = 9.3
x = 0.0
print *, 'a contains the value', a
print *, 'b contains the value', b

!Exchange the values of two variables a and b
x = a
a = b
b = x
print *, 'a contains the value', a
print *, 'b contains the value', b

end program
