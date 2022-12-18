program non_linear_fit 
    !! main file of non-linear_fit program
    !! in this file we call fit one times for each spectre_i.txt
    !! and we call linear_fit two times for l_gamma and l_omega_m for the linear regression
implicit none
integer :: i
real(kind=8),dimension(5):: l_gamma,l_omega_m, p

do i=1,5
call fit(i,l_gamma,l_omega_m)
end do

p=[1,3,6,10,15]
call linear_fit(p,l_gamma,5,"./Result/regr_gamma.txt")
call linear_fit(p,l_omega_m,5,"./Result/regr_omega.txt")

contains
    subroutine fit(nbf,l_gamma,l_omega_m)
            !! subroutine fit do the fit for a spectre_i.txt with several steps:
            !!  -first we read the file spectre_i.txt with i is "nbf" to count his number of lines
            !!  -after we allocate all the list that we need to do the fit
            !!  -we read again the same file to extract his data "fw_axis" and we building "w_axis"
            !!  -we can compute all the list that we need "weight, y_axis, x_axis" and the real "av_w, std_w"
            !!  -know we have the x and y axis we can call our function "compute" to get our coefficients
            !!  "omega_m, gamma, S" 
            !!  (we call it two times one with z=0 to have non weighted case and the other with z=1 to get weighted case)
            !!  -we fill "l_gamma, l_omega_m" with their respective values to do linear regression after
            !!  -we print the result to see our data in terminal
            !!  -finally we write our data in a file result_i.txt to plot this after

            ! Args:
            !   nbf (integer) : the number of the file that we study
            !   l_gamma (list) : empty list of value of gamma
            !   l_omega_m (list) : empty list of values of omega_m
            
            
            use TP1_mod
            implicit none
            real , parameter :: pi=3.1415926536
            real(kind=8) :: Av_w, std_w
            real(kind=8),dimension(:), allocatable :: fw_axis, weight, w_axis, y_axis, x_axis
            real(kind=8),dimension(3) :: A ,B
            integer, intent(in) :: nbf
            real(kind=8),dimension(5),intent(inout):: l_gamma,l_omega_m

            integer :: i, io, Nblines=0

            Nblines=0
            open(10,file='./Data/spectre_'//trim(str(nbf))//'.txt',iostat=io)
            do 
            read(10, *, iostat=io)!read numbers on the file
                if(io/=0) exit !exit of the loop if it is the end of the file
                Nblines = Nblines + 1 !computation of number of values on the file
            end do
            close(10)

            ALLOCATE(fw_axis(Nblines),weight(Nblines),y_axis(Nblines),w_axis(Nblines),x_axis(Nblines))

            open(10,file='./Data/spectre_'//trim(str(nbf))//'.txt',iostat=io)
            do i=1,Nblines
                read(10, *)fw_axis(i) 
                w_axis(i)= 2280 + (i-1)*0.01
            end do
            close(10)
            
            weight=fw_axis**2
            y_axis= 1/fw_axis
            Av_w= mean(w_axis,Nblines)
            std_w=std(w_axis,Nblines)
            x_axis=(w_axis-Av_w)/std_w

            
            A=Compute(w_axis,x_axis,y_axis,weight,0,Nblines)
            B=Compute(w_axis,x_axis,y_axis,weight,1,Nblines)
            l_gamma(nbf)=A(2)
            l_omega_m(nbf)=A(1)

            
            print*,"spectre_"//trim(str(nbf))," :: non weighted"
            print*,"Omega_m =",A(1),"gamma =",A(2),"S =",A(3)

            print*,"spectre_"//trim(str(nbf))," :: weighted"
            print*,"Omega_m =",B(1),"gamma =",B(2),"S =",B(3)
            print*," "

            open(10,file='./Result/result_'//trim(str(nbf))//'.txt')
            do i=1,Nblines
                write(10,*)fw_axis(i),",",Lorentz(w_axis(i),A(3),A(2),A(1)),",",w_axis(i),",",Lorentz(w_axis(i),B(3),B(2),B(1))
            end do
            close(10)

        end subroutine

        subroutine linear_fit(x,y,length,file)
            !! subroutine linear_fit to compute the linear regression with several steps:
            !!  -first we compute our two matrix of x
            !!  -after we compute the two other matrix with a column of y
            !!  -we compute the coef a and b of our curve
            !!  -finally we write in a file the result

            ! Args:
            !   nbf (integer) : the number of the file that we study
            !   l_gamma (list) : empty list of value of gamma
            !   l_omega_m (list) : empty list of values of omega_m
            

            use TP1_mod
            implicit none
            real(kind=8), dimension(5) :: x, y
            real(kind=8), dimension(2,2) :: mat, mat_var
            real(kind=8) :: a, b
            integer :: length
            character(len=23) :: file
            real(kind=8),dimension(2) :: col
        

            col(1)= mean(y,length)
            col(2)= mean(x*y,length)

            mat(1,1)=1
            mat(1,2)= mean(x,length)
            mat(2,1)= mean(x,length)
            mat(2,2)= mean(x**2,length)

            mat_var=mat
            mat_var(:,1)=col
            
            
            b=deter_2(mat_var)/deter_2(mat)

            mat_var=mat
            mat_var(:,2)=col

            a=deter_2(mat_var)/deter_2(mat)

            open(10,file=file)
            do i=1,5
                write(10,*)x(i),",", y(i),",",a ,",",b
            end do
            close(10)

        end subroutine 

end program non_linear_fit
