program Exercice4_3
implicit none

real(kind=8) :: entier, mean_value, deviation=0, maxi=0, mini=0
integer :: i=0, sum_number=0, io
character(len=26) :: name_file

print *, 'Enter a file name'
read *, name_file
open(unit=10, file=name_file)

do 
 read(10, *, iostat=io) entier
 if(io/=0) exit
  
 sum_number = sum_number + entier
 i = i + 1
enddo

mean_value = sum_number/i
print *, 'The mean value is', mean_value

rewind(unit=10)
i = 0

do
 read(10, *, iostat=io) entier
 if(io/=0) exit
 
 if(i==0) then !during the first loop, we initialize the maximal and minimal values
  maxi = entier !maximal value is the value of the first number
  mini = entier !minimal value is the value of the first number
 else
  if (entier > maxi) then !if number is higher than maximum value
   maxi = entier !maximal value is the number
  endif
  if (entier < mini) then !if number is smaller than minimal value
   mini = entier !minimal value is the number
  endif
 endif
 
 deviation = deviation + (entier - mean_value)**2
 i = i + 1
enddo

deviation = sqrt(deviation/i)
print *, 'The standard deviation is', deviation
print *, 'The maximal value is', maxi
print *, 'The minimal value is', mini


 close(10)

end program
