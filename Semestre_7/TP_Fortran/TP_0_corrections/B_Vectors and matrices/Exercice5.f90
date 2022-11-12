program Exercice5
implicit none

integer, parameter :: N = 10
real(kind=8), dimension(N, N)::A
real(kind=8) :: estimate1, estimate2
integer :: i, j
real(kind=8), dimension(N)::mu, eigenvec

!Definition of Lehmer matrix from Exercice 2
do i=1,10
   do j = 1,10   
   A(i,j) = min(i,j)/real(max(i,j), kind=4)
   end do 
end do

!Creation of an arbitrary vector
call Random_number(eigenvec)
estimate1 = 0d0

do 
   mu = matmul(a, eigenvec) !Multiply an arbitrary vector by the matrix
   estimate2 = dot_product(eigenvec, mu)/norm2(eigenvec)/norm2(eigenvec) !Computation of precision

   if (estimate2-estimate1 < 1d-10) then !if there is a precision of 10**-10
      write(*, "('The maximum eigenvalue of matrix is', F13.10)") estimate2
      exit
   endif
   
   estimate1=estimate2 !The new value of precision
   eigenvec = matmul(a, eigenvec) !The new value of arbitrary vector is the result of the multiplication

end do
end program
