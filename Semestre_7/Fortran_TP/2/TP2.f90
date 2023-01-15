program TP2
    ! declaration of variables
    implicit none
    integer(kind=4), parameter :: n = 50,nbe=1000
    integer(kind=4) :: ncmax=30, Iflag=1, m=11, jlev=0, ncount, node, i, n2
    real(kind=8), dimension(0:n) :: V, F, RR
    real(kind=8) :: r0=0.1D0, rn=2.6D0, a, b, eps=1.0D-04, tol=1.0D-04,&
    finit=0.D0, energ=-0.99D0, h, hc, e, de, borninf, bornsup
    
    
    ! value of the parameter a of the morse potential
    a = sqrt((2*4159.48-8083.20)/(2*60.80)) 
    ! value of the parameter b of the morse potential
    b = ((8083.20-2*4159.48)/(a*(8083.20-3*4159.48)))**2

    h=(rn-r0)/DFLOAT(n) !computation of the step 
    hc= h*h/b 

    ! potential vector
    call POT(n,r0,h,a,b,jlev,RR,V)

    e=energ
    ncount=0

    write(*,*) "No iter energ M de nodes"
    3 continue ! refence to start a loop but continue do nothing

    call SHOOT(n,a,h,hc,finit,eps,e,V,F,node,de,m,Iflag,b,jlev,RR) 

    
    ncount = ncount + 1 !increase the number of iterations finished
    ! write the result of the iteration
    write(*,200) ncount, e, m, de, node
    200 FORMAT(I4,5X, E15.7,I4,E15.7,I4)

    !if we have reach the number max of iterations we go to 999
    if (ncount > ncmax) go to 999 
    
    e=e+de ! correction of the energy with de compute in SHOOT

    !we check if the correction on the energy is correct if not we go to 3
    if (ABS(de/e) > tol) GOTO 3 

    ! write the result 
    open(1,file="mywavefunction8.txt")
    do i=0,n
        write(1,*)RR(i),",",F(i),",",V(i)
        ! 100 FORMAT(2E15.7)
    end do
    close(1)

    STOP ! this STOP the program
    ! we write the fact that we have reach the number max of iterations
    999 write(*,*)"No convergence reached with",ncmax,"iterations" 

    ! ------------ Question_2 ------------

    ! borninf=-0.96
    ! bornsup=-0.78

    ! open(10,file="./Result/Q2/Q2.txt")
    ! do i=0,nbe
    !     h=(rn-r0)/DFLOAT(n)
    !     hc= h*h/b
    !     ! potential vector
    !     call POT(n,r0,h,a,b,jlev,RR,V)
    !     e=borninf +ABS(borninf-bornsup)/nbe *i
    !     ncount=0
    !     de=0
    !     3 continue
    !     call SHOOT(n,a,h,hc,finit,eps,e,V,F,node,de,m,Iflag,b,jlev,RR)
    !     ncount = ncount + 1
    !     ! check the number of iteration
    !     if (ncount > ncmax) write(*,*)"No convergence reached with",ncmax,"iterations"
    !     e=e+de
    !     ! check the correction on the energys
    !     if (ABS(de/e) > tol) GOTO 3
    !     write(10,*)borninf +ABS(borninf-bornsup)/nbe *i,",",ncount
    ! end do
    ! close(10)

    ! ------------ Question_3 r0 ------------

    ! borninf=0.1
    ! bornsup=1.5

    ! open(10,file="./Result/Q3/Q3_r0.txt")
    ! do i=0,nbe
    !     r0=borninf +ABS(borninf-bornsup)/nbe *i
    !     h=(rn-r0)/DFLOAT(n)
    !     hc= h*h/b
    !     ! potential vector
    !     call POT(n,r0,h,a,b,jlev,RR,V)
    !     e=-0.95
    !     ncount=0
    !     de=0
    !     3 continue
    !     call SHOOT(n,a,h,hc,finit,eps,e,V,F,node,de,m,Iflag,b,jlev,RR)
    !     ncount = ncount + 1
    !     ! check the number of iteration
    !     if (ncount > ncmax) write(*,*)"No convergence reached with",ncmax,"iterations"
    !     e=e+de
    !     ! check the correction on the energys
    !     if (ABS(de/e) > tol) GOTO 3

    !     write(10,*)borninf +ABS(borninf-bornsup)/nbe *i,",",ncount,',',e 
    ! end do
    ! close(10)

    ! ------------ Question_3 rn ------------
    
    ! borninf=1
    ! bornsup=3

    ! open(10,file="./Result/Q3/Q3_rn.txt")
    ! do i=0,nbe
    !     rn=borninf +ABS(borninf-bornsup)/nbe *i
    !     h=(rn-r0)/DFLOAT(n)
    !     hc= h*h/b
    !     ! potential vector
    !     call POT(n,r0,h,a,b,jlev,RR,V)
    !     e=-0.20
    !     ncount=0
    !     de=0
    !     3 continue
    !     call SHOOT(n,a,h,hc,finit,eps,e,V,F,node,de,m,Iflag,b,jlev,RR)
    !     ncount = ncount + 1
    !     ! check the number of iteration
    !     if (ncount > ncmax) write(*,*)"No convergence reached with",ncmax,"iterations"
    !     e=e+de
    !     ! check the correction on the energys
    !     if (ABS(de/e) > tol) GOTO 3

    !     write(10,*)borninf +ABS(borninf-bornsup)/nbe *i,",",ncount,',',e 
    ! end do
    ! close(10)

    


    !------------ Question_3 eps ------------
    ! borninf=0.0000001
    ! bornsup=1
    ! print*,borninf
    ! open(10,file="./Result/Q3/Q3_eps.txt")
    ! do i=0,nbe
    !     eps=borninf +ABS(borninf-bornsup)/nbe *i
    !     h=(rn-r0)/DFLOAT(n)
    !     hc= h*h/b
    !     ! potential vector
    !     call POT(n,r0,h,a,b,jlev,RR,V)
    !     e=-0.20
    !     ncount=0
    !     de=0
    !     3 continue
    !     call SHOOT(n,a,h,hc,finit,eps,e,V,F,node,de,m,Iflag,b,jlev,RR)
    !     ncount = ncount + 1
    !     ! check the number of iteration
    !     if (ncount > ncmax) write(*,*)"No convergence reached with",ncmax,"iterations"
    !     e=e+de
    !     ! check the correction on the energys
    !     if (ABS(de/e) > tol) GOTO 3

    !     write(10,*)borninf +ABS(borninf-bornsup)/nbe *i,",",ncount,',',e 
    ! end do
    ! close(10)


    !------------ Question_3 tol ------------

    ! borninf=0.0000001
    ! bornsup=0.0001


    ! open(10,file="./Result/Q3/Q3_tol.txt")
    ! do i=0,nbe
    !     tol=borninf +ABS(borninf-bornsup)/nbe *i
    !     h=(rn-r0)/DFLOAT(n)
    !     hc= h*h/b
    !     ! potential vector
    !     call POT(n,r0,h,a,b,jlev,RR,V)
    !     e=-0.20
    !     ncount=0
    !     de=0
    !     3 continue
    !     call SHOOT(n,a,h,hc,finit,eps,e,V,F,node,de,m,Iflag,b,jlev,RR)
    !     ncount = ncount + 1
    !     ! check the number of iteration
    !     if (ncount > ncmax) write(*,*)"No convergence reached with",ncmax,"iterations"
    !     e=e+de
    !     ! check the correction on the energys
    !     if (ABS(de/e) > tol) GOTO 3

    !     write(10,*)borninf +ABS(borninf-bornsup)/nbe *i,",",ncount,',',e 
    ! end do
    ! close(10)



    !------------ Question_4  ------------
    ! borninf=-0.96
    ! bornsup=-0.1

    ! open(10,file="./Result/Q4/Q4.txt")
    ! do i=0,nbe
    !     !v=0 => energ= 
    !     h=(rn-r0)/DFLOAT(n)
    !     hc= h*h/b
    !     ! potential vector
    !     call POT(n,r0,h,a,b,jlev,RR,V)
    !     e=borninf +ABS(borninf-bornsup)/nbe *i
    !     de=0
    !     call SHOOT(n,a,h,hc,finit,eps,e,V,F,node,de,m,Iflag,b,jlev,RR)

    !     write(10,*)borninf +ABS(borninf-bornsup)/nbe *i,",",de
    ! end do
    ! close(10)







    contains
    !this program contains several subroutines to calculate the potential, the shoot method and the propagator.

        subroutine POT(n,r0,h,a,b,jlev,RR,V)
            !! subroutine Pot compute the potential for each point on our line from r0 to rn
            !! and it compute also the discretisation of our line with a step given in argument

            ! Args:
            !   n (integer) : the number of points on our line
            !   r0 (integer) : the value of the starting point
            !   h (real) : value of the distance between two points
            !   a (real) : parameter of our point compute explain in the report
            !   b (real) : parameter of our point compute explain in the report
            !   jlev (integer) : value of J the quantum orbital number
            !   RR (vector(0:n)) : empty list of values of RR
            !   V (vector(0:n)) : empty list of values of V


            implicit none
            integer(kind=4) :: n, jlev, i
            real(kind=8), dimension(0:n) :: V, RR
            real(kind=8) :: r0, h, a, b

            do i=0,n
                RR(i) = r0 + (i)*h
                V(i) = exp(-2.0*a*(RR(i)-1.D0))-2.D0*exp(-a*(RR(i)-1.D0))
            end do
        end subroutine 

        subroutine SHOOT(n,a,h,hc,finit,eps,e,V,F,node,de,m,Iflag,b,jlev,RR)
            !! subroutine SHOOT compute the method to find the energy and correct it

            ! Args:
            !   n (integer) : the number of points on our line
            !   r0 (integer) : the value of the starting point
            !   h (real) : value of the distance between two points
            !   hc (real): value of h*h/b
            !   finit (integer) : value of F(r_n)
            !   eps (real) : value of F(1) or f(n-1) to approximate
            !   nodes (integer): number of node (when Psi= 0 expect the bound conditions)
            !   F (vector(0:n))empty list to put the values of Psi
            !   de (real) : correction of the energy
            !   m (integer): value of the index of r_m
            !   a (real) : parameter of our point compute explain in the report
            !   b (real) : parameter of our point compute explain in the report
            !   Iflag (integer) : parameter to set m=f1 when Iflag is equal to 1
            !   jlev (integer) : value of J the quantum orbital number
            !   RR (vector(0:n)) : empty list to put values of RR
            !   V (vector(0:n)) : empty list to put values of V
        implicit none 
        integer(kind=4):: n, node, m, Iflag, Istep, Iinit, Ifin, i,jlev
        real(kind=8), dimension(0:n):: V,F,RR
        real(kind=8) :: a, b, h, hc, finit, eps, e, de, f0, f1, coeff, an, fsm,fm
        Istep=1
        Iinit=1
        Ifin=n-1
        if (Iflag == 0) Ifin = m ! i don't understand this condition because iflag is always equal to 1
        f0 = finit
        f1 = eps 
        call PROPAG(n,hc,Istep,Iinit,Ifin,Iflag,f0,f1,e,V,F,m,b,jlev,RR) ! propagation to the right with Istep = 1
        fm= F(m)
        Istep = -1
        Iinit = n-1
        Ifin=m+1
        f0=finit
        f1=eps
        call PROPAG(n,hc,Istep,Iinit,Ifin,Iflag,f0,f1,e,V,F,m,b,jlev,RR)! propagation to the left with Istep = - 1
        coeff=F(m)/fm !normalisation
        do i=0,m-1
            F(i)=F(i)*coeff
        end do 
        node=0
        an= 0.D0 
        do i=1,N
            an=an+F(i)*F(i) ! computation of the norm of Psi
            if (F(i)*F(i-1) < 0.D0) node = node + 1 ! detection of nodes
        end do
        fsm=(F(m+1) + F(m-1) -2.D0 *F(m))!Psi seconde derivative in m
        de= F(m)*((b*jlev*(jlev+1)/RR(m)**2+V(m)-e)*F(m)-fsm/hc)/an !computation of de with cooley method
        return
        end subroutine 

        subroutine PROPAG(n,hc,Istep,Iinit,Ifin,Iflag,f0,f1,e,V,F,m,b,jlev,RR)
            !! subroutine SHOOT compute the method to find the energy and correct it

            ! Args:
            !   n (integer) : the number of points on our line
            !   r0 (integer) : the value of the starting point
            !   h (real) : value of the distance between two points
            !   hc (real): value of h*h/b
            !   finit (integer) : value of F(r_n)
            !   eps (real) : value of F(1) or f(n-1) to approximate
            !   nodes (integer): number of node (when Psi= 0 expect the bound conditions)
            !   F (vector(0:n))empty list to put the values of Psi
            !   de (real) : correction of the energy
            !   m (integer): value of the index of r_m
            !   a (real) : parameter of our point compute explain in the report
            !   b (real) : parameter of our point compute explain in the report
            !   Iflag (integer) : parameter to set m=f1 when Iflag is equal to 1
            !   jlev (integer) : value of J the quantum orbital number
            !   RR (vector(0:n)) : empty list to put values of RR
            !   V (vector(0:n)) : empty list to put values of V
            implicit none
            integer(kind=4) :: n, Istep, Iinit, Ifin, Iflag, m, i, i1, jlev
            real(kind=8), dimension(0:n):: V,F,RR
            real(kind=8) :: hc, f0, f1, e, b

            F(Iinit-Istep) = f0
            F(Iinit) = f1

            do i=Iinit,Ifin,Istep
                i1 = i + Istep
                F(i1)=(2.0D0+hc*(b*jlev*(jlev+1)/RR(i)**2+V(i)-E))*F(i)-F(i-Istep) ! computation of Psi(i+1) with finites differences method
                if (Iflag == Istep)then
                    if (F(i1) < F(i)) then !detection of m only only when Istep is equal to one 
                        m=i1
                    return
                    end if
                end if
            end do
            return
        end subroutine 
        
end program