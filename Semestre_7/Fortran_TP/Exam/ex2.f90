program exo2
implicit none
integer :: n, i

print*,"give me a number n and i will give you his multiplication table"
read(*,*)n

do i=1,10
    print*,n,"*",i,"=",n*i
end do 




end program exo2