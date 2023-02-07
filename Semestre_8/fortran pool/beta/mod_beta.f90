module mod_beta
    ! this mod contains all the function and subroutines in the file beta.f90
    implicit none

    contains
        ! this subroutines compute the Cramer's rules 
        subroutine cramer(lambda,M,P)
            implicit none
            integer, parameter :: n=6
            real(kind=8),dimension(n) :: lambda, P
            real(kind=8),dimension(n,n) :: M, Mk
            integer :: i, j, k

            do k=1,n
                do i=1,n
                    do j=1,n
                        Mk(i,j) = M(i,j) 
                    end do
                end do
                ! set the matrix M by replace the colomun by lambda
                Mk(:,k) = lambda(:) 
                P(k) = det(Mk,6)/det(M,6)
            end do
            return 
        end subroutine

        ! this function compute the determinant for array "a" with a given dimension
        recursive function det(a,n) result(d)
        real(kind=8), dimension(n,n), intent(in) :: a
        integer, intent(in) :: n
        real(kind=8), dimension(n-1, n-1) :: b
        real(kind=8) :: d
        integer :: i, sgn
        if (n == 1) then
            d = a(1,1)
        else
            d = 0
            sgn = 1
            do i=1, n
                b(:, :(i-1)) = a(2:, :i-1)
                b(:, i:) = a(2:, i+1:)
                d = d + sgn * a(1, i) * det(b, n-1)
                sgn = sgn * (-1)
            enddo
        end if
        end function det

        ! this subroutine compute the Fourier expension for all the parameter
        subroutine fourrier(D, req, ar0, ar1, at0, at1, a, b,P,n)
            implicit none
            integer :: n
            real(kind=8),  parameter :: pi  = 4 * atan (1.0_8)
            real(kind=8), dimension(:,:):: D, ar0, ar1, at0, at1, a, b, req
            real(kind=8), dimension(n) :: l
            real(kind=8), dimension(8,6):: P
            integer :: i,j

            !compute the vector of axis x and y
            l(1) = 0
            do i=2,n
                l(i) = i *3.17_8/n
            end do

            do i=1,n
                do j=1,n
                    D(i,j)   = sum(fourier_dev(P(1,:),i,j,6,n))
                    req(i,j) = sum(fourier_dev(P(2,:),i,j,6,n))
                    ar0(i,j) = sum(fourier_dev(P(3,:),i,j,6,n))
                    ar1(i,j) = sum(fourier_dev(P(4,:),i,j,6,n))
                    at0(i,j) = sum(fourier_dev(P(5,:),i,j,6,n))
                    at1(i,j) = sum(fourier_dev(P(6,:),i,j,6,n))
                    a(i,j)   = sum(fourier_dev(P(7,:),i,j,6,n))
                    b(i,j)   = sum(fourier_dev(P(8,:),i,j,6,n))
                end do
            end do
        end subroutine fourrier

        ! this function compute the Fourier developpement and put it in a vector
        function fourier_dev(coef,i,j,or,n)
            implicit none
            integer :: i, j , or, n,k
            real(kind=8), dimension(n) :: l
            real(kind=8), dimension(:) :: coef
            real(kind=8), dimension(or) :: fourier_dev
            
            !compute the vector of axis x and y
            l(1) = 0
            do k=2,n
                l(k) =k *3.17_8/n
            end do

            fourier_dev =[coef(1) &
                &,coef(2)*(f(l(i))+f(l(j))) &
                &,coef(3)*(f(l(i)+l(j))+f(l(i)-l(j))) &
                &,coef(4)*(f(2*l(i))+f(2*l(j))) &
                &,coef(5)*(f(2*l(i)+l(j))+f(l(i)+2*l(j))+f(2*l(i)-l(j))+f(l(i)-2*l(j))) &
                &,coef(6)*(f(2*(l(i)+l(j)))+f(2*(l(i)-l(j))))]
        end function fourier_dev

        !this function compute cos((2*pi*X)/3.17) to make the program more readable
        function f(X)
            implicit none
            real(kind=8),  parameter :: pi  = 4 * atan (1.0_8)
            real(kind=8) :: f, X

            f=dcos((2*pi*X)/3.17_8)

        end function f

        ! this function compute the potential for given coordinates with 
        ! the array parameter
        function pot(D,req, ar0, ar1, at0, at1, a, b, i,j,z)
            implicit none 
            integer ::  i, j
            real(kind=8), dimension(:,:) :: D, ar0, ar1, at0, at1, a, b, req
            real(kind=8) :: pot, z,al, fz

            fz=0.5*(1+dtanh(a(i,j)*z + b(i,j)))
            al = (1-fz)*(ar0(i,j)+ar1(i,j)*z) + fz*(at0(i,j)+at1(i,j)*z)
            pot = D(i,j)*(dexp(-2*al*(z-req(i,j))) -2*dexp(-al*(z-req(i,j))))
        end function pot

end module mod_beta