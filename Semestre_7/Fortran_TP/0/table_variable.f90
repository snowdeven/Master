program table_variable
implicit none

integer :: rows , col ,i
real(kind=4),dimension(:,:),allocatable :: T

write(*,*) "Give me a positive rows:"
read(*,*)rows

write(*,*) "Give me a positive col:"
read(*,*)col


if (rows < 0 .or. col <0 ) stop






allocate(T(rows,col))

T(1:rows,1:col)=1
do i=1,rows
print*,T(i,1:rows)
end do
deallocate(T)





end program table_variable 

