program exo3
implicit none
real(kind=8),  dimension(5) :: A, B, C
real(kind=8) :: maxi_value_A, maxi_value_B, maxi_value_C

call RANDOM_NUMBER(A)
call RANDOM_NUMBER(B)
call RANDOM_NUMBER(C)

A(:) = A(:)*20
print*,A
B(:) = B(:)*20
print*,B
C(:) = C(:)*20
print*,C
Call find_Max_value(A,B,C)
print*, maxi_value_A, maxi_value_B, maxi_value_C



contains
    subroutine find_Max_value(A,B,C)
        implicit none
        real(kind=8), dimension(5) :: A,B,C
        real(kind=8) :: maxi_value_A, maxi_value_B, maxi_value_C
        
        maxi_value_A = MAXVAL(A)
        maxi_value_B = MAXVAL(B)
        maxi_value_C = MAXVAL(C)
    end subroutine
end program exo3