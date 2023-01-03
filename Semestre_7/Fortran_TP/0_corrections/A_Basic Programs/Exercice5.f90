program Exercice5
implicit none

real(kind=8) :: a, b, c, delta, racine_delta, x1, x2
complex(kind=8) :: x3, x4, i

print *, 'Give 3 coefficients a, b, c of the quadratic equation ax**2+bx+c=0'
read *, a, b, c !read the 3 user's coefficients of the quadratic equation

if (a==0) then !case bx+c=0
 print *, 'This is not a quadratic equation.'
 
else
 delta = b*b-4*a*c !computation of delta
 racine_delta = sqrt(abs(delta))
 
 if (delta == 0) then !one solution
  x1 = -b/(2*a)
  print *, 'There is one solution :', x1
 
 else if (delta > 0) then !2 real solutions
  x1 = (-b - racine_delta)/(2*a)
  x2 = (-b + racine_delta)/(2*a)
  print *, 'There is two real solutions :', x1, x2
  
 else !2 complex solutions
  x3 = (-b - i*racine_delta)/(2*a)
  x4 = (-b + i*racine_delta)/(2*a)
  print *, 'There is two complex solutions :', x3, x4
 endif

endif

end program
