program Exercice4
implicit none

integer, parameter :: N=14
real, dimension (N) :: vec
integer :: i
real(kind=8) :: dev, average

!to decomment for a) example
!vec = [5.0, 3.0, 17.0, -7.56, 78.1, 99.99, 0.8, 11.7, 33.8, 29.6]
!to decomment for b) example
vec = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0]
dev = deviation (vec, N)
print*, dev

contains
   function deviation(vec, N) !internal function which returns standard deviation of a series of real numbers
      real, dimension(:), intent(in) :: vec
      real(kind=8) :: deviation
      real(kind=8) :: average
      integer :: i, N
      
      average = 0
      do i = 1, N
         average = average + vec(i) !computation of the average
      end do
      average = average/N !computation of the average
      deviation=sqrt(sum((vec-average)**2)/N) !computation of the standard deviation
   end function deviation

end program
