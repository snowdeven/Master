program echec
implicit none
integer, parameter :: N=8
real(kind=4), dimension(N,N) :: E

integer :: i ,j

E(1:N,1:N)=0

do i=1,N,2
do j=1,N,2
E(i,j)=1
end do
end do

do i=2,N,2
do j=2,N,2
E(i,j)=1
end do
end do


do i=1,N
print *,E(i,1:N)
end do

E( ::2, ::2) =1
E(2::2,2::2) =1

do i=1,N
print *,E(i,1:N)
end do


end program echec
