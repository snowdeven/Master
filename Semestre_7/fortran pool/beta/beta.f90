program beta
    
    use mod_beta
    implicit  none
    integer :: i, j, io 
    real(kind=8), dimension(6) :: P, k
    real(kind=8), dimension(6,8) :: Coef
    real(kind=8), dimension(8,6) :: mP
    real(kind=8),  parameter :: pi  = 4 * datan (1.0_8)
    real(kind=8), dimension(6,6) :: M
    integer, parameter :: n=1000
    real(kind=8), dimension(n) :: l
    real(kind=8), dimension(n) :: ODC_h,ODC_b,ODC_t,ODC_th,ODC_tb,ODC_bh,lz
    real(kind=8), dimension(n,n) :: D, ar0, ar1, at0, at1, a, b, req, V
    real(kind=8) :: z=2.0_8 , borninf=-1.0_8, bornsup=5.0_8

    open(10,file='coef.txt',iostat=io)
    do i=1,6
        read(10, *)Coef(i,:) 
    end do
    close(10)
    
    l(1) = 0
    do i=2,n
        l(i) = i *3.17_8/n
    end do

    k=[1,1,1,1,1,1]

    M(1,:) = fourier_dev(k,n/2,1,6,n)
    M(2,:) = fourier_dev(k,n/4,n/2,6,n)
    M(3,:) = fourier_dev(k,n/2,n/2,6,n)
    M(4,:) = fourier_dev(k,1,1,6,n)
    M(5,:) = fourier_dev(k,n/4,1,6,n)
    M(6,:) = fourier_dev(k,n/4,n/4,6,n)

    

    do i=1,8
        call cramer(Coef(:,i),M,P)
        mP(i,:) = P
    end do 

    call fourrier(D, req, ar0, ar1, at0, at1, a, b,mP,n)

    ! print*,D(1,1), req(1,1), ar0(1,1), ar1(1,1), at0(1,1), at1(1,1), a(1,1), b(1,1)
    ! print*,D(1,1)*z

    open(10,file="pot.txt")
    do i=1,n
        do j=1,n
            V(i,j) = pot(D, req, ar0, ar1, at0, at1, a, b,i,j,z)
        end do
        write(10,*)l(i)," ",z," ",V(i,:)
    end do
    close(10)

    lz(1)=borninf
    do i=2,n
        lz(i) =borninf + i*(abs(borninf)+bornsup)/n
    end do
    open(10,file="1Dcuts.txt")
    do i=1,n
        ODC_b(i)  = pot(D,req, ar0, ar1, at0, at1, a, b, n/2,1,lz(i))
        ODC_bh(i) = pot(D,req, ar0, ar1, at0, at1, a, b, n/4,n/2,lz(i))
        ODC_h(i)  = pot(D,req, ar0, ar1, at0, at1, a, b, n/2,n/2,lz(i))
        ODC_t(i)  = pot(D,req, ar0, ar1, at0, at1, a, b, 1,1,lz(i))
        ODC_tb(i) = pot(D,req, ar0, ar1, at0, at1, a, b, n/4,1,lz(i))
        ODC_th(i) = pot(D,req, ar0, ar1, at0, at1, a, b, n/4,n/4,lz(i))
        write(10,*)ODC_b(i)," ",ODC_bh(i)," ",ODC_h(i)," ",ODC_t(i)," ",ODC_tb(i)," ",ODC_th(i)," ",lz(i)
    end do
    close(10)
    
end program beta