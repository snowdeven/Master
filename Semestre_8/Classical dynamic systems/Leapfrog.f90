program Leapfrog
    Interface bigJ 
         Function bigJ(mat,sgn) 
            character, intent(in) :: sgn
            Real, intent(in) :: mat(:,:)
            complex(kind=8) bigJ (size(mat),size(mat)) 
         End Function 
    End Interface 
    
    implicit none
    integer, parameter :: j=1
    integer ::  SizeJ, SizeX
    integer :: i,k
    integer, dimension(:), allocatable :: m
    real, dimension(2*j+1,2*j+1):: mat
    character(len=1) :: sgn
    
    
    
    allocate(m(2*j+1))

    do i=1,2*j+1
        m(i) = j-i +1
    end do 


    print*,m
    sgn="+"

    

    bigJ("+")

    
end program Leapfrog

function bigJ(mat,sgn)
    implicit none
    Real, intent(in) :: mat(:,:)
    integer :: i,k
    character(len=1) :: sgn
    integer, dimension(size(mat)) :: m
    
    complex(kind=8), dimension(0:size(mat),0:size(mat)):: bigJ


    do i=1,2*j+1
        do k=1,2*j+1
            if (sgn == "+") then
                if (m(k)+1 == m(i)) then
                    bigJ(i,k) = sqrt(dfloat(j*(j+1) - m(k)*(m(k)+1)))
                end if
            else if (sgn == "-") then
                if (m(i) == m(k)) then
                    bigJ(i,k) = m(k)
                end if
            else
                if (m(k)-1 == m(i)) then
                    bigJ(i,k) = sqrt(dfloat(j*(j+1) - m(k)*(m(k)-1)))
                end if
            end if
        end do
    end do
end function