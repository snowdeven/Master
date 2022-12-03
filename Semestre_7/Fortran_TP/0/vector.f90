program modulus_vectorus
implicit none
real(kind=4), dimension(10) :: vector
real(kind=4) :: Norme
integer :: n , sum , i
n=10
vector=[1,2,1,2,1,2,1,2,1,2]
sum=0

Norme = DOT_PRODUCT(vector,vector)**0.5
write(*,*)Norme

do i=1,n
sum= sum +vector(i)*vector(i)
end do
write(*,*)sum**0.5

write(*,*)NORM2(vector)
end program modulus_vectorus
