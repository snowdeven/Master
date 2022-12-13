program TP1 

use stats
use non_linear_fit
implicit none
! character(len=13)::file
integer :: nbf, i
real(kind=8),dimension(5):: l_gamma,l_omega_m, p




do i=1,5
call fit(i,l_gamma,l_omega_m)

end do





p=[1,3,6,10,15]

call linear_fit(p,l_gamma,5,"regr_gamma.txt")


call linear_fit(p,l_omega_m,5,"regr_omega.txt")



contains


    subroutine fit(nbf,l_gamma,l_omega_m)
            use stats
            implicit none
            real , parameter :: pi=3.1415926536
            real(kind=8) :: Av_w, Av_w2, std_w
            real(kind=8),dimension(:), allocatable :: fw_axis, weight, w_axis, y_axis, x_axis
            real(kind=8),dimension(3) :: A ,B
            integer, intent(in) :: nbf
            real(kind=8),dimension(5),intent(out):: l_gamma,l_omega_m
        
            integer :: i, io, Nblines=0
            
            Nblines=0
            open(10,file='spectre_'//trim(str(nbf))//'.txt',iostat=io)
            do 
            read(10, *, iostat=io)!read numbers on the file
                if(io/=0) exit !exit of the loop if it is the end of the file
                Nblines = Nblines + 1 !computation of number of values on the file
            end do
            close(10)
        
            ALLOCATE(fw_axis(Nblines),weight(Nblines),y_axis(Nblines),w_axis(Nblines),x_axis(Nblines))
        
            open(10,file='spectre_'//trim(str(nbf))//'.txt',iostat=io)
            do i=1,Nblines
                read(10, *)fw_axis(i) 
                w_axis(i)= 2280 + (i-1)*0.01
            end do
            close(10)
            


            
            weight=fw_axis**2
            y_axis= 1/fw_axis
            Av_w=sum(w_axis)/Nblines
            Av_w2 = sum(w_axis**2)/Nblines
            std_w=sqrt(Av_w2-(Av_w**2))
            x_axis=(w_axis-Av_w)/std_w

            print*,mean(x_axis,Nblines)
            A=Compute(w_axis,x_axis,y_axis,weight,0,Nblines)
        
            B=Compute(w_axis,x_axis,y_axis,weight,1,Nblines)
        
            l_gamma(nbf)=A(2)
            l_omega_m(nbf)=A(1)
            

        
            print*,"Omega_m = ",A(1),"gamma = ",A(2),"S = ",A(3)

            print*,"Omega_m = ",B(1),"gamma = ",B(2),"S = ",B(3)
            
            open(10,file='result_'//trim(str(nbf))//'.txt')
            do i=1,Nblines
                write(10,*)fw_axis(i),",",Lorentz(w_axis(i),A(3),A(2),A(1)),",",w_axis(i),",",Lorentz(w_axis(i),B(3),B(2),B(1))
            end do
            close(10)
        end subroutine
        subroutine linear_fit(x,y,lenght,file)
            use stats
            implicit none
            real(kind=8), dimension(5) :: x, y
            real(kind=8), dimension(2,2) :: mat, mat_var
            real(kind=8) :: a, b,a_0,a_1
            integer :: lenght
            character(len=14) :: file
        
            mat(1,1)=1
            mat(1,2)= mean(x,lenght)
            mat(2,1)= mean(x,lenght)
            mat(2,2)= mean(x**2,lenght)

            mat_var=mat
            mat_var(1,1)=mean(y,lenght)
            mat_var(1,2)=mean(x*y,lenght)
            
            b=deter_2(mat_var)/deter_2(mat)

            mat_var=mat
            mat_var(2,1)=mean(y,lenght)
            mat_var(2,2)=mean(x*y,lenght)

            a=deter_2(mat_var)/deter_2(mat)

            open(10,file=file)
            do i=1,5
                write(10,*)x(i),",", y(i),",",a ,",",b
            end do

            close(10)
        end subroutine 


end program TP1
