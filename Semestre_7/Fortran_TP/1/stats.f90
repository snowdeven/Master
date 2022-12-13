module stats
    implicit none

    contains

        function mean(list,length)

            integer :: length
            real(kind=8) :: mean
            real(kind=8), dimension(:) :: list 

            mean = sum(list)/length
        
        end function mean

        function std(list,length)

            integer :: length
            real(kind=8) :: std 
            real(kind=8), dimension(:) :: list

            std = (sum(list**2)/length - (sum(list)/length)**2)**0.5

        end function std

        function deter_3(mat)
            implicit none
            real(kind=8), intent(in) :: mat(3,3)
            real(kind=8) :: a,b,c,deter_3
        
            a=mat(1,1)*(mat(2,2)*mat(3,3)-mat(3,2)*mat(2,3))
            b=mat(1,2)*(mat(2,1)*mat(3,3)-mat(3,1)*mat(2,3))
            c=mat(1,3)*(mat(2,1)*mat(3,2)-mat(3,1)*mat(2,2))
            deter_3=a-b+c
        end function deter_3

        function deter_2(mat)
            implicit none
            real(kind=8), intent(in) :: mat(2,2)
            real(kind=8) :: a,b,deter_2
        
            a=mat(1,1)*mat(2,2)
            b=mat(1,2)*mat(2,1)
            deter_2=a-b
        end function deter_2


        function Compute(w,x,y,weight,z,Nb)
        
            implicit none 
            real , parameter :: pi=3.1415926536
            integer :: Nb, z
            real(kind=8), dimension(:) :: w, x, y, weight
            real(kind=8),dimension(3,3) :: coef, coef_var
            real(kind=8),dimension(3) :: Compute
            real(kind=8),dimension(3) :: val
            real(kind=8),dimension(3) :: col
            integer :: i, j
        

            do i=1,3
                do j=1,3
                    coef(i,j)=mean((weight**z)*x**(int(i+j-2)),Nb)
                end do 
            end do 
            

            col(1)=mean((weight**z)*y,Nb)
            col(2)=mean((weight**z)*y*x,Nb)
            col(3)=mean((weight**z)*y*x**2,Nb)
            
            

            coef_var=coef
            coef_var(:,1)=col
            val(1)=deter_3(coef_var)/deter_3(coef)
            
            coef_var=coef
            coef_var(:,2)=col
            val(2)=deter_3(coef_var)/deter_3(coef)
            
            coef_var=coef
            coef_var(:,3)=col
            val(3)=deter_3(coef_var)/deter_3(coef)
            

            Compute(1)= mean(w,Nb) - (std(w,Nb)*val(2))/(2*val(3))
            Compute(2)=std(w,Nb)*sqrt((val(1)/val(3))-(val(2)/2*val(3))**2)
            Compute(3)=(pi*std(w,Nb)) /sqrt(val(1)*val(3) - (val(2)**2 /4))
        
        end function Compute
        
        function Lorentz(omega,S,gamma,Omega_m)
            
            implicit none
            real(kind=8), intent(in) :: omega, S, gamma, Omega_m
            real(kind=8) :: Lorentz
            real , parameter :: pi=3.14159265
            Lorentz= (S*gamma)/(pi*((omega-Omega_m)**2 + gamma**2))
        end function Lorentz
        character(len=20) function str(k)
        !   "Convert an integer to string."
            integer, intent(in) :: k
            write (str, *) k
            str = adjustl(str)
        end function str
end module stats
