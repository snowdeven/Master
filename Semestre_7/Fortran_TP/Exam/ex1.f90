program exo1
    implicit none
    integer, dimension(100) :: zeta
    integer :: i

zeta(:)=0
zeta(1)=8
zeta(2)=8
zeta(10)=8
zeta(34)=8
zeta(99)=8
zeta(100)=8

do i=1,100
    print*,"index =",i,"value = ",zeta(i)
end do

end program exo1