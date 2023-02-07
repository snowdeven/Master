program alpha
    ! This program perform the computation of potential surface for the system N/W(100)
    ! with the morse potential
    use mod_alpha
    implicit none

    ! declaration of all the variables use in the program
    integer :: i,j, io
    integer, parameter :: n=100
    real(kind=8),  parameter :: pi  = 4 * atan (1.0_8)
    real(kind=8), dimension(3) :: P,k
    real(kind=8), dimension(3,3) :: Coef, M, mP
    real(kind=8), dimension(n) :: l
    real(kind=8), dimension(n) :: ODC_h,ODC_b,ODC_t,ODC_th,ODC_tb,ODC_bh,lz
    real(kind=8), dimension(n,n) :: D, al, req,V
    real(kind=8) :: z=2.0_8 , borninf=-2.0_8, bornsup=5.0_8

    ! read the data from "coef.txt"
    open(10,file='coeff.txt',iostat=io)
    do i=1,3
        read(10, *)Coef(i,:) 
    end do
    close(10)

    ! compute the axis x and y
    l(1) = 0
    do i=2,n
        l(i) = i *3.17/n
    end do

    ! set the matrix M
    k=[1,1,1]
    M(1,:) = fourier_dev(k,n/2,1,3,n)
    M(2,:) = fourier_dev(k,n/2,n/2,3,n)
    M(3,:) = fourier_dev(k,1,1,3,n)

    ! apply the cramer's rules and 
    ! store these coefficient in the array mP
    do i=1,3
        call cramer(Coef(:,i),M,P)
        mP(i,:) = P
    end do 
    
    ! compute the Fourier expansion 
    ! for all the parameter
    call fourrier(D,al,req,mP,n)

    ! compute the value of potential in the all unit cell
    ! and for a given z to store them in "pot.txt"
    open(10,file="pot.txt")
    do i=1,n
        do j=1,n
            V(i,j) = pot(D,al,req,i,j,z,n)
        end do
        write(10,*)l(i)," ",z," ",V(i,:)
    end do
    close(10)

    ! compute the z axis with the specify boundary
    lz(1)=borninf
    do i=2,n
        lz(i) =borninf + i*(abs(borninf)+bornsup)/n
    end do 

    ! compute the 1D cuts for all the sites
    ! and store them in the file "1Dcuts.txt"
    open(10,file="1Dcuts.txt")
    do i=1,n
        ODC_b(i) = pot(D,al,req,n/2,1,lz(i),n)
        ODC_bh(i) = pot(D,al,req,n/4,n/2,lz(i),n)
        ODC_h(i) = pot(D,al,req,n/2,n/2,lz(i),n)
        ODC_t(i) = pot(D,al,req,1,1,lz(i),n)
        ODC_tb(i) = pot(D,al,req,n/4,1,lz(i),n)
        ODC_th(i) = pot(D,al,req,n/4,n/4,lz(i),n)
        write(10,*)ODC_b(i)," ",ODC_bh(i)," ",ODC_h(i)," ",ODC_t(i)," ",ODC_tb(i)," ",ODC_th(i)," ",lz(i)
    end do
    close(10)
end program 