program Exercice3
implicit none

integer, dimension(8, 8)::c
integer :: i, j

!Explicit loops to initialise the table
do i=1,8
   do j=1,8
      if (mod(i,2)==0) then !if i is even
      
         if (mod(j,2)==0) then !if j is even
            c(i,j)=1
         else !if j is odd
            c(i,j)=0
         end if
         
      else !if i is odd
      
         if (mod(j,2)==0) then !if j is even
            c(i,j)=0
         else !if j is odd
            c(i,j)=1
         end if
         
      end if
   end do
   write(*, '(8(I1, 1x))')c(i,:)
end do

!First command
do i=1,8
   c(  ::2, ::2) = 1
   write(*, '(8(I1, 1x))')c(:,:)
end do

!Second command
do i=1,8
   c(2::2,2::2) = 1
   write(*, '(8(I1, 1x))')c(:,:)
end do

end program
