program TP1 

use stats
use non_linear_fit
implicit none
character(len=13)::file
integer :: i


do i=1,5
    read*,file
call    fit(file)
end do 

end program TP1
