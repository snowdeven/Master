program Exercice6
implicit none

real(kind=4) :: A, B, C

subroutine Mistaken(A, B, C)
   real, intent(in) :: A
   real, intent(out) :: C
end subroutine Mistaken

end program
