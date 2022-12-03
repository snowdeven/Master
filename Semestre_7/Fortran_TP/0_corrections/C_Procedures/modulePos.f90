module pos
   implicit none
   
contains
   function bisection(vec, k) !returns the position of a particular number in a growing sequence of integer numbers
   integer :: bisection
   integer, intent(in) :: k
   integer, dimension(:), intent(in) :: vec
   integer :: i, ihalf, j
   
   i =1 !i indice of the lower bound
   j= size(vec) !j indice of the upper bond
   
   do while (k /= i .or. k/=j)
      if (i>=j) then !if lower bond is higher than upper bond
         print*, 'Not good numbers.'
         exit
      else
         ihalf = (i+(j-1))/2 !computation of the middle point
         if k>ihalf then !k higher than middle point
            i = ihalf+1
         else !k smaller than middle point
            j = ihalf
         end if
      end if
   end do 
   
   if (k==j) then
      bisection = i
   else
      bisection = j
   end if
   
   end function bisection

end module
