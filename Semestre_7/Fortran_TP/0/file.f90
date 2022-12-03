program file

character(len=50) :: Name
integer :: Number


write(*,*) "Give file name pls:"
read(*,*)Name

print *,Name

open(unit=10,file=Name)

do i=1,10
write(*,*) "Give a number pls:"
read(*,*)Number
if (Number == 0) exit 
write(10,*)Number
write(*,*)Number
end do

end program file

