program stdandaverage
Implicit None
character(len=50) :: Name
integer :: Number,Coderror,Nb_line,Max_value,Min_value
real(kind=4) :: Sum,Sum2
Nb_line=0
Sum=0
Sum2=0
Max_value = 0
Max_value = 0
write(*,*) "Give file name pls:"
read(*,*)Name

open(unit=10,iostat=Coderror,file=Name)

do while(Coderror==0)
Number = 0

read(10,*,iostat=Coderror)Number

if (Coderror==0) Nb_line = Nb_line + 1
Sum = Sum + Number
Sum2= Sum2 + Number**2

if (Max_value < Number) Max_value = Number
if (Min_value > Number) Min_value = Number






end do

print *,'The average is :',Sum/Nb_line
print *,'The standart deviation :',Sum2/Nb_line -(Sum/Nb_line)**2
print *,'The Maximun is ',Max_value
print *,'The minimun is ',Min_value


end program stdandaverage
