program Exercice4
implicit none

integer :: nb_raw, nb_col, i=0
integer, dimension (:,:), allocatable :: table !Table of variable size

print*, 'Choose the number of lines and the number of columns.'
read "(I4)", nb_raw
read "(I4)", nb_col

if ((nb_raw<=0) .or. (nb_col<=0)) then !if user write negatives numbers or 0
   print*, 'The numbers must be positive.'
else
   allocate(table(nb_raw, nb_col)) !Define size of the table with user's numbers
   table(:,:)=1 !fill table with 1
   
   do i=1, nb_raw
   	print *, table(i,:) !Print table
   end do
   
   deallocate(table) !deallocate the table at the end
end if
end program
