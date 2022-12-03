program Exercice2
implicit none

real(kind=4) :: x, y, z

x = 2.3
y = 1.9

z = somme(x, y) !use of the internal function
print*, z

contains
   function somme (x, y) !internal function which returns the sum of 2 real numbers
      real :: somme
      real, intent(in) :: x, y !input variables
    somme = x+y
   end function somme

end program
