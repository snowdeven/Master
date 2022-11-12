program Exercice3
implicit none

real :: r

r=somme()
print*, r

contains
   function somme () !function which simulates a roll of 2 dices and compute the total score
      integer :: somme
      real :: x, y
      call random_number (x) !intrinsic subroutine random_number to obtain pseudo-random value for x between 0 and 1
      x = int(6*x)+1 !x between 1 and 6
      call random_number (y) !intrinsic subroutine random_number to obtain pseudo-random value for y between 0 and 6
      y = int(6*y)+1 !y between 1 and 6
      somme = x+y !sum of the 2 values of the roll
   end function somme


end program
