program Matrix
implicit none
integer, parameter :: N = 5
integer :: i ,j 
real(kind=4), dimension(N,N) :: A



do i=1,N
do  j=1,N
	
A(i,j) = real(MINVAL([i,j]))/real(MAXVAL([i,j]))
	
end do
end do


do i=1,N
print *,A(i,1:N)
end do



end program Matrix
