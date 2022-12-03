program Exercice4_2
implicit none

real(kind=8) :: entier, mean_value, deviation=0
integer :: i=0, sum_number=0, io
character(len=26) :: name_file

print *, 'Enter a file name' !ask user a file name
read *, name_file !read the name of the file
open(unit=10, file=name_file) !open the file

do 
 read(10, *, iostat=io) entier !read numbers on the file
 if(io/=0) exit !exit of the loop if it is the end of the file
  
 sum_number = sum_number + entier !computation of the sum of the numbers
 i = i + 1 !computation of number of values on the file
enddo

mean_value = sum_number/i !computation of mean value
print *, 'The mean value is', mean_value

rewind(unit=10) !return begin on the file
i = 0

do
 read(10, *, iostat=io) entier
 if(io/=0) exit
 
 deviation = deviation + (entier - mean_value)**2 !computation of deviation
 i = i + 1
enddo

deviation = sqrt(deviation/i) !computation of deviation
print *, 'The standard deviation is', deviation

 close(10) !close file

end program
