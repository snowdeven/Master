program Exercice1
implicit none

real(kind=4)::a, b, c
a=5.1
b=2.5

call somme(a, b, c) !use of the internal subroutine
print*, c


contains
subroutine somme (a, b, c) !Definition of internal subroutines which returns the sum of 2 real numbers
   real, intent(in) :: a, b !input variables
   real, intent(out) :: c !output variables
   c = a+b
end subroutine somme

end program

