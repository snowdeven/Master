program Exercice1
implicit none

real, dimension(10) :: v
real(kind=4)::norm1, norm3, norm4
integer :: i

v = [1, 2, 1, 2, 1, 2, 1, 2, 1 ,2]
norm1=0

!Norm of the vector using an explicit loop on the indices
do i=1,10
   norm1=norm1+v(i)**2
end do
norm1=sqrt(norm1)
print*, 'The norm of the vector with the first method is :', norm1

!Norm of the vector using the intrinsic function scalar product
norm3=dot_product(v, v)
norm3=sqrt(norm3)
print*, 'The norm of the vector with the second method is :', norm3

!Norm of the vector using the intrinsic function for norm
norm4=norm2(v)
print*, 'The norm of the vector with the third method is :', norm4

end program
