program TP2
    ! declaration of variables
    implicit none
    integer(kind=4), parameter :: n = 50
    integer(kind=4) :: ncmax=30, Iflag=1, m=11, jlev=0, ncount, node, i
    real(kind=8), dimension(0:n) :: V, F, RR

    real(kind=8) :: r0=0.1D0, rn=2.6D0, a=1, b=1, eps=1.0D-04, tol=1.0D-04,&
    finit=0.D0, energ=-0.99D0, h, hc, e, de
    
    h=(rn-r0)/DFLOAT(n)
    hc= h*h/b

    ! potential vector
    call POT(n,r0,h,a,b,jlev,RR,V)

    e=energ
    ncount=0

    write(*,*) "No iter energ M de nodes"
    3 continue

    call SHOOT(n,a,h,hc,finit,eps,e,V,F,node,de,m,Iflag)

    ncount = ncount + 1
    ! write the result of the iteration
    write(*,200) ncount, e, m, de, node
    200 FORMAT(I4,5X, E15.7,I4,E15.7,I4)

    ! check the number of iteration
    if (ncount > ncmax) go to 999
    e=e+de

    ! check the correction on the energy
    if (ABS(de/e) > tol) GOTO 3

    ! write the result 
    open(1,file="mywavefunction.txt")
    do i=0,n
        write(1,*)RR(i),",",F(i)
        ! 100 FORMAT(2E15.7)
    end do
    close(1)

    STOP
    999 write(*,*)"No convergence reached with",ncmax,"iterations"







    contains
    

        subroutine POT(n,r0,h,a,b,jlev,RR,V)
            implicit none
            integer(kind=4) :: n, jlev, i
            real(kind=8), dimension(0:n) :: V, RR
            real(kind=8) :: r0, h, a, b

            do i=0,n
                RR(i) = r0 + (i)*h
                V(i) = exp(-2.0*a*(RR(i)-1.D0))-2.D0*exp(-a*(RR(i)-1.D0))
            end do
        end subroutine 

        subroutine SHOOT(n,a,h,hc,finit,eps,e,V,F,node,de,m,Iflag)
        implicit none 
        integer(kind=4):: n, node, m, Iflag, Istep, Iinit, Ifin, i
        real(kind=8), dimension(0:n):: V,F
        real(kind=8) :: a, b, h, hc, finit, eps, e, de, f0, f1, coeff, an, fsm,fm
        Istep=1
        Iinit=1
        Ifin=n-1
        if (Iflag == 0) Ifin = m
        f0 = finit
        f1 = eps 
        call PROPAG(n,hc,Istep,Iinit,Ifin,Iflag,f0,f1,e,V,F,m)
        fm= F(m)
        Istep = -1
        Iinit = n-1
        Ifin=m+1
        ! f0=finit
        ! f1=eps
        call PROPAG(n,hc,Istep,Iinit,Ifin,Iflag,f0,f1,e,V,F,m)
        coeff=F(m)/fm
        do i=0,m-1
            F(i)=F(i)*coeff
        end do 
        node=0
        an= 0.D0
        do i=1,N
            an=an+F(i)*F(i)
            if (F(i)*F(i-1) < 0.D0) node = node + 1
        end do
        fsm=F(m+1) + F(m-1) -2.D0 *F(m)
        de= F(m)*((V(m)-e)*F(m)-fsm/hc)/an
        return
        end subroutine 

        subroutine PROPAG(n,hc,Istep,Iinit,Ifin,Iflag,f0,f1,e,V,F,m)
            implicit none
            integer(kind=4) :: n, Istep, Iinit, Ifin, Iflag, m, i, i1
            real(kind=8), dimension(0:n):: V,F
            real(kind=8) :: hc, f0, f1, e 

            F(Iinit-Istep) = f0
            F(Iinit) = f1

            do i=Iinit,Ifin,Istep
                i1 = i + Istep
                F(i1)=(2.0D0+hc*(V(i)-E))*F(i)-F(i-Istep)
                if (Iflag == Istep)then
                    if (F(i1) < F(i)) then
                        m=i1
                    return
                    end if
                end if
            end do
            return
        end subroutine 
end program