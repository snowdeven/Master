program Exercice6_a
implicit none

integer :: n, i, somme, square, somme_square, somme_i, somme_i_square

n = 10
somme = 0
somme_square = 0

do i=1, n, 1
 print *, 'i =', i
 somme = somme + i !computation of the sum of integers
 square = i*i
 print *, 'i**2 =', square
 somme_square = somme_square + square !computation of the sum of the squares
end do

print *, 'The sum of integers is :', somme
print *, 'The sum of squares is :', somme_square

!Sums calculated with the analytic expressions
somme_i = n*(n+1)/2
somme_i_square = n*(n+1)*(2*n+1)/6

print *, 'The sum of integers with expresson is :', somme_i
print *, 'The sum of squares with expression is :', somme_i_square

end program
