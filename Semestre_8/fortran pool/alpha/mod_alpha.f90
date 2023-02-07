module mod_alpha
    ! this mod contains all the function and subroutines in the file alpha.f90
    implicit none
    
    contains
        ! this subroutines compute the Cramer's rules 
        subroutine cramer(lambda,M,P)
            implicit none
            integer, parameter :: n=3
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
                P(k) = det(Mk,n)/det(M,n)
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
        subroutine fourrier(D,al,req,P,n)
            implicit none
            integer :: n
            real(kind=8),  parameter :: pi  = 4 * atan (1.0_8)
            real(kind=8), dimension(:,:):: D,al,req
            real(kind=8), dimension(n) :: l
            real(kind=8), dimension(3,3):: P
            integer :: i,j
            l(1) = 0
            do i=2,n
                l(i) = i *3.17/n
            end do
            do i=1,n
                do j=1,n
                    D(i,j) = sum(fourier_dev(P(1,:),i,j,3,n))
                    al(i,j) = sum(fourier_dev(P(2,:),i,j,3,n))
                    req(i,j) = sum(fourier_dev(P(3,:),i,j,3,n))
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
                &,coef(3)*(f(l(i)+l(j))+f(l(i)-l(j)))]
            
        end function fourier_dev

        !this function compute cos((2*pi*X)/3.17) to make the program more readable
        function f(X)
            implicit none
            real(kind=8),  parameter :: pi  = 4 * atan (1.0_8)
            real(kind=8) :: f, X

            f=dcos((2*pi*X)/3.17)

        end function f
        
        ! this function compute the potential for given coordinates with 
        ! the array parameter
        function pot(D,al,req,i,j,z,n)
            implicit none 
            integer :: n, i, j
            real(kind=8), dimension(:,:) :: D, al, req
            real(kind=8) :: pot, z

            pot = D(i,j)*(dexp(-2*al(i,j)*(z-req(i,j)))-2*dexp(-al(i,j)*(z-req(i,j))))
        end function pot

end module mod_alpha