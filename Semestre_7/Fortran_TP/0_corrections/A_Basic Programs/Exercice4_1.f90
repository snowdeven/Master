program Exercice4_1
implicit none

real (kind=4) :: number
character (len=26) :: name

print *, 'Enter a file name' !ask user a name file
read *, name !read the name of the file
open(unit=10, file=name) !open the file

do 
 print *, 'Enter a number (0 to stop)' !ask user number
 read (*,*) number !read user's number
 if(number==0) exit !if number is 0, stop the program
 write(10, fmt='(F8.3)') number !write the number on the file
end do

 close(10) !close the file

end program
