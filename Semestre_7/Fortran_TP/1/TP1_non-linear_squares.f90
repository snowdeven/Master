program TP1 

use stats
implicit none
real , parameter :: pi=3.1415926536
real(kind=8) :: Omega_m, gamma, S, Av_w, Av_w2, std_w
real(kind=8),dimension(:), allocatable :: fw_axis, fw2_axis, w_axis, y_axis, x_axis
real(kind=8),dimension(3) :: A
character(len=13)::file

integer :: i, io, Nblines=0


file="spectre_1.txt"

open(10,file=file,iostat=io)
do 
 read(10, *, iostat=io)!read numbers on the file
    if(io/=0) exit !exit of the loop if it is the end of the file
    Nblines = Nblines + 1 !computation of number of values on the file
end do
close(10)

ALLOCATE(fw_axis(Nblines),fw2_axis(Nblines),y_axis(Nblines),w_axis(Nblines),x_axis(Nblines))

open(10,file=file)
do i=1,Nblines
    read(10, *)fw_axis(i) 
    w_axis(i)= 2280 + (i-1)*0.01
end do
close(10)

fw2_axis=fw_axis**2
y_axis= 1/fw_axis
Av_w=sum(w_axis)/Nblines
Av_w2 = sum(w_axis**2)/Nblines
std_w=sqrt(Av_w2-(Av_w**2))
x_axis=(w_axis-Av_w)/std_w

A=compute(x_axis,y_axis,fw2_axis,1,Nblines)

Omega_m= Av_w - (std_w*A(2))/(2*A(3))
gamma=std_w*sqrt((A(1)/A(3))-(A(2)/2*A(3))**2)
S=(pi*std_w) /sqrt(A(1)*A(3) - (A(2)**2 /4))

print*,"Omega_m = ",Omega_m,"gamma = ",gamma,"S = ",S


open(10,file="result.txt")
do i=1,Nblines
    write(10,*)fw_axis(i),",",Lorentz(w_axis(i),S,gamma,Omega_m),",",w_axis(i)
end do
close(10)


! call fit()



end program TP1
