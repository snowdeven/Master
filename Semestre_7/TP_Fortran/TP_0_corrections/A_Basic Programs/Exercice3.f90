program Exercice3
implicit none

real :: a=5.25, q=1.05
integer :: i=4

i = a - q !a and q are real but i is an integer
a = i + q
print *, 'a=', a

end program
