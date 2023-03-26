Program matrix_op
        implicit none 
        Interface bigJ 
            Function bigJ (j,type) 
            Integer(kind=8) :: j
            character(len=1) :: type
            Complex(kind=8) bigJ(2*j+1,2*j+1) 
            End Function 
        End Interface
        Interface com
            Function com (j,x,y) 
            Integer(kind=8) :: j
            Complex(kind=8), Dimension(2*j+2,2*j+2) :: x,y
            Complex(kind=8)  com(2*j+2,2*j+2) 
            End Function 
        End Interface
        Interface A
            Function A(j,M,x,y,z) 
            Integer(kind=8) :: j
            Complex(kind=8), Dimension(2*j+2,2*j+2) :: M,x,y,z
            Complex(kind=8)  A(2*j+2,2*j+2) 
            End Function 
        End Interface
        
        Integer(kind=8) :: j=100
        Integer(kind=8) :: i,lJ,lX
        real(kind=8) :: pr, std=0.01,an
        real(kind=8),parameter :: pi=3.14159265
        Integer(kind=8) :: n=1000, t0=0, tf=200
        real(kind=8) :: h, v
        Complex(kind=8), Dimension(:,:),allocatable :: Jx, Jy, Jz
        Complex(kind=8), Dimension(:,:),allocatable :: X1, X2, X3
        Complex(kind=8), Dimension(:,:),allocatable :: V1, V2, V3, Vi

        h=(tf-t0)/dfloat(n)
        lJ=2*j+1
        lX=2*j+2
        v=0
        

        allocate(Jx(lJ,lJ),Jy(lJ,lJ),Jz(lJ,lJ))
        

        Jx = bigJ(j,"x")
        Jy = bigJ(j,"y")
        Jz = bigJ(j,"z")

        ! do i=1,lJ
        !     print*,Jz(i,:)
        ! end do 
        ! print*,"------------"
        ! print*,Jz(:2,:)
        


        allocate(X1(lX,lX),X2(lX,lX),X3(lX,lX))
        X1=0
        X2=0
        X3=0

        X1(:lJ,:lJ) = Jx/j
        X1(lX,lX) = 0
        X2(:lJ,:lJ) = Jy/j
        X2(lX,lX) = 0
        X3(:lJ,:lJ) = Jz/j
        X3(lX,lX) = 0

        deallocate(Jx,Jy,Jz)

        do i=1,lJ
            call random_stdnormal(pr,std)
            call random_number(an)
            X1(lX,i) =pr*exp((0.0,1.0)*an*2*pi)
            X1(i,lX) =pr*exp((0.0,-1.0)*an*2*pi)
            print*,X1(lX,i),X1(i,lX),1,i
            
            call random_stdnormal(pr,std)
            call random_number(an)
            
            X2(lX,i) =pr*exp((0.0,1.0)*an*2*pi)
            X2(i,lX) =pr*exp((0.0,-1.0)*an*2*pi)
            ! print*,X2(lX,i),X2(i,lX),2,i
            call random_stdnormal(pr,std)
            call random_number(an)
            
            X3(lX,i) =pr*exp((0.0,1.0)*an*2*pi)
            X3(i,lX) =pr*exp((0.0,-1.0)*an*2*pi)
            ! print*,X3(lX,i),X3(i,lX),3,i
        end do

        allocate(V1(lX,lX),V2(lX,lX),V3(lX,lX),Vi(lX,lX))

        V1=0
        V2=0
        V3=0


        V1= A(j,X1,X1,X2,X3) * (h/2.0)
        V2= A(j,X2,X1,X2,X3) * (h/2.0)
        V3= A(j,X3,X1,X2,X3) * (h/2.0)

        ! print*,"______V1_______"
        ! do i=1,lX
        !     print*,V1(i,:)
        ! end do
        ! print*,"______-_______"

        ! print*,"______V2_______"
        ! do i=1,lX
        !     print*,V2(i,:)
        ! end do
        ! print*,"______-_______"

        ! print*,"______V3_______"
        ! do i=1,lX
        !     print*,V3(i,:)
        ! end do
        ! print*,"______-_______"

        open(10,file="data.dat")
        do i=1,n
        ! compute V at time t+1/2
        V1 = V1 + A(j,X1,X1,X2,X3)*h
        V2 = V2 + A(j,X2,X1,X2,X3)*h
        V3 = V3 + A(j,X3,X1,X2,X3)*h
        ! Compute X at time t+1
        X1 = X1 + V1*h
        X2 = X2 + V2*h
        X3 = X3 + V3*h
        
        ! print*,X1(lX,:lJ)
        ! print*,"------------"
        ! print*,X1(:lJ,lX)
        ! print*,"____________"
        ! print*,"------------"
        write(10,"(F7.3,F6.3,F6.3,F6.3)")i*h  , real(sqrt(sum((X1(lX,:lJ)*X1(:lJ,lX))))),&
                        real(sqrt(sum((X2(lX,:lJ)*X2(:lJ,lX))))),&
                        real(sqrt(sum((X3(lX,:lJ)*X3(:lJ,lX)))))
        

        end do 





        deallocate(X1,X2,X3)
        deallocate(V1,V2,V3)

        close(10)




        

End Program 

Function bigJ(j,type) 
    
    character(len=1) :: type
    Integer(kind=8) :: j,k
    Complex(kind=8) bigJ(2*j+1,2*j+1)
    Complex(kind=8), Dimension(2*j+1,2*j+1) :: mat_plus,mat_moins,mat_z
    Integer(kind=8), dimension(2*j+1) :: mr
    
    do i=1,2*j+1
        mr(i) = j-i +1
        
    end do
    do i=1,2*j+1
        do k=1,2*j+1
            if (mr(k)+1 == mr(i)) then
                mat_plus(i,k) = sqrt(dfloat(j*(j+1) - mr(k)*(mr(k)+1)))
            else
                mat_plus(i,k) = 0
            end if
        
            if (mr(i) == mr(k)) then
                mat_z(i,k) = mr(k)
            else 
                mat_z(i,k) = 0
            end if
        
            if (mr(k)-1 == mr(i)) then
                mat_moins(i,k) = sqrt(dfloat(j*(j+1) - mr(k)*(mr(k)-1)))
            else 
                mat_moins(i,k) = 0
            end if
        end do
    end do

    if (type == "x") then
        bigJ = (mat_plus+mat_moins)/2
    else if (type == "z") then
        bigJ = mat_z
    else if (type == "y") then
        bigJ = (mat_plus-mat_moins)/(0.0,2)
    else
        stop "ERROR on type only '+','-','z' are allowed"
    end if
End Function 
Function com(j,x,y)
    Integer(kind=8) :: j
    Complex(kind=8), Dimension(2*j+2,2*j+2) :: x,y,com


    com = (matmul(x,y)-(matmul(y,x)))

end function
Function A(j,M,x,y,z)
    Interface com
            Function com (j,x,y) 
            Integer(kind=8) :: j
            Complex(kind=8), Dimension(2*j+2,2*j+2) :: x,y
            Complex(kind=8)  com(2*j+2,2*j+2) 
            End Function 
        End Interface
    Integer(kind=8) :: j
    Complex(kind=8), Dimension(2*j+2,2*j+2) :: M,x,y,z,A


    A = (com(j,x,com(j,M,x))+com(j,y,com(j,M,y))+com(j,z,com(j,M,z)))

end function
subroutine random_stduniform(u)
    implicit none
    real(kind=8),intent(out) :: u
    real(kind=8) :: r
    call random_number(r)
    u = 1 - r
end subroutine random_stduniform
subroutine random_stdnormal(x,std)
    implicit none
    real(kind=8),intent(out) :: x
    real(kind=8),intent(in) :: std
    real(kind=8),parameter :: pi=3.14159265
    real(kind=8) :: u1,u2

    call random_stduniform(u1)
    call random_stduniform(u2)

    x = std*sqrt(-2*log(u1))*cos(2*pi*u2)
end subroutine random_stdnormal