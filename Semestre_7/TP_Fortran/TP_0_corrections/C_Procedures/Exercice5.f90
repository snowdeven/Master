subroutine proc()
integer, save :: nb_call=0
nb_call=nb_call+1
print*, "It has been called",nb_call," times "
return
end
