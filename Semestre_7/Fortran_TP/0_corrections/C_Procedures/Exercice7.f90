program Exercice7
use pos !use the pos module containing the bisection function
implicit none

integer, parameter :: N = 10
integer, dimension(N) :: vec
integer :: nbr, k

vec = [1, 3, 5, 7, 11, 17, 29, 33, 78, 99]
k = 7
nbr = bisection(vec, k) !use bisection function of pos module
print*, nbr

end program
