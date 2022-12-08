module non_linear_fit
    implicit none

    contains


    subroutine fit(file)
            use stats
            implicit none
            real , parameter :: pi=3.1415926536
            real(kind=8) :: Av_w, Av_w2, std_w
            real(kind=8),dimension(:), allocatable :: fw_axis, weight, w_axis, y_axis, x_axis
            real(kind=8),dimension(3) :: A ,B
            character(len=13)::file
        
            integer :: i, io, Nblines=0
        
            open(10,file=file,iostat=io)
            do 
            read(10, *, iostat=io)!read numbers on the file
                if(io/=0) exit !exit of the loop if it is the end of the file
                Nblines = Nblines + 1 !computation of number of values on the file
            end do
            close(10)
        
            ALLOCATE(fw_axis(Nblines),weight(Nblines),y_axis(Nblines),w_axis(Nblines),x_axis(Nblines))
        
            open(10,file=file,iostat=io)
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
        
            A=Compute(w_axis,x_axis,y_axis,weight,0,Nblines)
        
            B=Compute(w_axis,x_axis,y_axis,weight,1,Nblines)
        
            
        
            print*,"Omega_m = ",A(1),"gamma = ",A(2),"S = ",A(3)
            print*,"Omega_m = ",B(1),"gamma = ",B(2),"S = ",B(3)
        
        
            open(10,file="result.txt")
            do i=1,Nblines
                write(10,*)fw_axis(i),",",Lorentz(w_axis(i),A(3),A(2),A(1)),",",w_axis(i),",",Lorentz(w_axis(i),B(3),B(2),B(1))
            end do
            close(10)
        
        end subroutine
end module non_linear_fit