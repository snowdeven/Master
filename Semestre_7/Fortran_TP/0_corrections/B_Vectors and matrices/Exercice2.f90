program Exercice2
implicit none

integer, parameter :: N = 10
real, dimension(N, N)::A
integer :: i, j

do i=1,10
   do j = 1,10   
   A(i,j) = min(i,j)/real(max(i,j), kind=4) !Computation of Aij
   end do
   
   write(*, '(10f8.3, 1x)',advance='no')A(i,:) !Display each line on the screen
end do

end program
