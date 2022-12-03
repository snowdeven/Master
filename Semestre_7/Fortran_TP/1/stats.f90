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

        function deter(mat)
            implicit none
            real(kind=8), intent(in) :: mat(3,3)
            real(kind=8) :: a,b,c,deter
        
            a=mat(1,1)*(mat(2,2)*mat(3,3)-mat(3,2)*mat(2,3))
            b=mat(1,2)*(mat(2,1)*mat(3,3)-mat(3,1)*mat(2,3))
            c=mat(1,3)*(mat(2,1)*mat(3,2)-mat(3,1)*mat(2,2))
            deter=a-b+c
        end function deter

        function Compute(x,y,w,z,Nb)
        
            implicit none 
            integer :: Nb, z
            real(kind=8), dimension(:) :: x, y, w
            real(kind=8),dimension(3,3) :: coef, coef_var
            real(kind=8),dimension(3) :: Compute
            real(kind=8),dimension(3) :: col
            integer :: i, j
        

            do i=1,3
                do j=1,3
                    ! coef(i,j) = sum(x**(int(i+j-2)))/Nb
                    coef(i,j)=mean((w**z)*x**(int(i+j-2)),Nb)
                end do 
            end do 
            
            col(1)=mean((w**z)*y,Nb)
            col(2)=mean((w**z)*y*x,Nb)
            col(3)=mean((w**z)*y*x**2,Nb)
            
            

            coef_var=coef
            coef_var(:,1)=col
            Compute(1)=deter(coef_var)/deter(coef)
            
            coef_var=coef
            coef_var(:,2)=col
            Compute(2)=deter(coef_var)/deter(coef)
            
            coef_var=coef
            coef_var(:,3)=col
            Compute(3)=deter(coef_var)/deter(coef)
            
        end function Compute
        
        function Lorentz(omega,S,gamma,Omega_m)
            implicit none
            real(kind=8), intent(in) :: omega, S, gamma, Omega_m
            real(kind=8) :: Lorentz
            real , parameter :: pi=3.14159265
            Lorentz= (S*gamma)/(pi*((omega-Omega_m)**2 + gamma**2))
        end function Lorentz
                
end module stats
