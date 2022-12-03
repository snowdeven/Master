program Exercice6_b
implicit none

integer :: square_sum, i, somme, square

square_sum = 0
i =0
somme = 0

do while (square_sum <= 500) !stopping calculations as soon as the sum of the squares exceeds 500
 i = i + 1
 somme = somme + i !computation of the sum of integers
 print *, 'i = ', i
 square = i*i
 square_sum = square_sum + square !computation of sum of the squares
 print *, 'i**2 = ', square
end do

print *, 'The sum is :', somme
print *, 'The square sum is :', square_sum

end program
