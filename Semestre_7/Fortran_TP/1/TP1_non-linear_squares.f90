program TP1

implicit none
real(kind=4),dimension(3,3) :: mat
real(kind=4),dimension(:), allocatable :: y_axis
real(kind=4),dimension(:), allocatable :: cry_axis 

real(kind=4),dimension(:), allocatable :: x_axis
real(kind=4),dimension(:), allocatable :: crx_axis

integer :: i ,j, z,a ,b ,c ,io
integer :: Nblines=0
real(kind=8) :: mean, square_mean, var ,std
real(kind=8) :: cr_x_mean,cr_x2_mean,cr_x3_mean,cr_x4_mean,cr_y_mean,cr_y_x_mean,cr_y_x2_mean



open(10,file="spectre_1.txt",iostat=io)

do 
 read(10, *, iostat=io) !read numbers on the file
    if(io/=0) exit !exit of the loop if it is the end of the file
    Nblines = Nblines + 1 !computation of number of values on the file
end do

close(10)

ALLOCATE(y_axis(Nblines))
ALLOCATE(cry_axis(Nblines))

open(10,file="spectre_1.txt")

do i=1,Nblines
    read(10, *)y_axis(i)
    ! print*,y_axis(i)
    cry_axis= 1/y_axis(i)
    ! print*,cry_axis(i)

end do

close(10)


ALLOCATE(x_axis(Nblines))





x_axis(1)=2280
do i=2,Nblines
    x_axis(i)= 2280 + (i-1)*0.01
    ! print*,x_axis(i), x_axis(i)**2
end do


ALLOCATE(crx_axis(Nblines))


mean=sum(x_axis)/Nblines

square_mean = sum(x_axis**2)/Nblines
std=((square_mean-(mean**2))**0.5)



do i=1,Nblines
    crx_axis(i)=(x_axis(i)-mean)/std
    ! print*,crx_axis(i)
    ! print*,((square_mean-(mean**2))**0.5)
    
end do 

cr_x_mean=(sum(crx_axis))/Nblines
cr_x2_mean=sum(crx_axis**2)/Nblines
cr_x3_mean=sum(crx_axis**3)/Nblines
cr_x4_mean=sum(crx_axis**4)/Nblines

cr_y_mean=sum(cry_axis)/Nblines

cr_y_x_mean=sum(cry_axis*crx_axis)/Nblines
cr_y_x2_mean=sum(cry_axis*(crx_axis**2))/Nblines





! z=1

! do i=1,3
!     do  j=1,3	
!         mat(i,j) = z

!         z=z+1
!     end do
! end do

! function det(mat) result(det)
!     implicit none
!     real :: det
!     real, intent(in) :: mat

!     a=mat(1,1)*(mat(2,2)*mat(3,3)-mat(3,2)*mat(2,3))
!     b=mat(1,2)*(mat(2,1)*mat(3,3)-mat(3,1)*mat(2,3))
!     c=mat(1,3)*(mat(2,1)*mat(3,2)-mat(3,1)*mat(2,2))
!     det=a-b+c
! end function det     

! print*,det(mat)












end program TP1
