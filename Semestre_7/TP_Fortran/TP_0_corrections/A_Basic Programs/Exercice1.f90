program Exercice1
implicit none
real (kind=8) :: eps,one
integer :: i, n

one=1.
eps=1.
n=1000 !Number of iterations

do i=1,n
 if (one == 1.+eps) then !if we have the precision of the calculations of the computer (eps is too small for the computer)
  exit !stop the loop
 end if
 eps=eps/2. !the value of the variable is divided by 2 at each loop
 write(*,*) i, one, eps !write on the screen
enddo
end program
