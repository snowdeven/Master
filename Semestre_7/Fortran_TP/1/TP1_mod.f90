module TP1_mod
    !! This module is useful to keep all our function that we repeat many times for TP_1
    implicit none
    contains
    !it contains:
    !mean, std, deter_3, deter_2
    !compute, Lorentz, str
    
        function mean(list,length)
            !! computation of mean 
            ! Args:
            !   list (real,dimension(length)) : list of values that we want the mean
            !   length (integer) : number of values in list
            !Returns:
            !   mean (integer) : average of our list
            integer :: length
            real(kind=8) :: mean
            real(kind=8), dimension(:) :: list 

            mean = sum(list)/length
        
        end function mean

        function std(list,length)
            !! computation of the standart deviation
            ! Args:
            !   list (real,dimension(length)) : list of values that we want the standart deviation
            !   length (integer) : number of values in list
            !Returns:
            !   std (integer) : std of our list
            integer :: length
            real(kind=8) :: std 
            real(kind=8), dimension(:) :: list

            std = (sum(list**2)/length - (sum(list)/length)**2)**0.5
            
        end function std

        function deter_3(mat)
            !! function to get the determinant for a 3x3 matrix
            ! Args:
            !   mat (real,dimension(3,3)) : matrix that we want the determinant
            !Returns:
            !   deter_3 (integer) : determinant of our matrix
            implicit none
            real(kind=8), intent(in) :: mat(3,3)
            real(kind=8) :: a,b,c,deter_3
        
            a=mat(1,1)*(mat(2,2)*mat(3,3)-mat(3,2)*mat(2,3)) 
            b=mat(1,2)*(mat(2,1)*mat(3,3)-mat(3,1)*mat(2,3))
            c=mat(1,3)*(mat(2,1)*mat(3,2)-mat(3,1)*mat(2,2))
            deter_3=a-b+c
        end function deter_3

        function deter_2(mat)
            !! function to get the determinant for a 2x2 matrix
            ! Args:
            !   mat (real,dimension(3,3)) : matrix that we want the determinant
            !Returns:
            !   deter_3 (integer) : determinant of our matrix
            implicit none
            real(kind=8), intent(in) :: mat(2,2)
            real(kind=8) :: a,b,deter_2
        
            a=mat(1,1)*mat(2,2)
            b=mat(1,2)*mat(2,1)
            deter_2=a-b
        end function deter_2

        function Compute(w,x,y,weight,z,Nb)
            !! compute the main calculation to get omega_m, S and gamma with the followings steps:
            !!   -we create "mat" our matrix 3x3 of x 
            !!   -we compute "col" this is the colomun with y in our matrix 
            !!   -we create "mat_var" a copy of our matrix "var" 
            !!   -we compute "a_coef" a list of coefficients a_0, a_1, a_2
            !!    to compute a_0 we take the ratio deter_3(mat_var)/deter_3(mat) with the first column equal to "col"
            !!    to compute a_1 same thing but this is the second column equal to "col"
            !!    to compute a_2 same thing but this is the last column that it equals to "col"
            !!   -and finally we compute omega_m, gamma, S with this coefficient respecting the formula in the report.
            ! Args:
            !   w (real,dimension(3,3)) : matrix that we want the determinant
            !   x (real,dimension(Nb)) : list of our x_axis
            !   y (real,dimension(Nb)) : list of our y_axis
            !   weight (real,dimension(Nb)) : list of weight
            !   z (integer) : a number to precise weighted or not
            !                 with weight**z if z=0 not weighted otherwise weighted
            !   Nb (integer) : length of our list
            !Returns:
            !   compute (real,dimension(3)) : list of omega_m, gamma and S
            implicit none 
            real , parameter :: pi=3.1415926536
            integer :: Nb, z, i, j
            real(kind=8), dimension(:) :: w, x, y, weight
            real(kind=8),dimension(3,3) :: mat, mat_var
            real(kind=8),dimension(3) :: Compute, a_coef, col
            

            !double loop to create our matrix of x and not assign each elements with a value
            do i=1,3
                do j=1,3
                    mat(i,j)=mean((weight**z)*x**(int(i+j-2)),Nb)
                end do 
            end do 
            
            col(1)=mean((weight**z)*y,Nb)
            col(2)=mean((weight**z)*y*x,Nb)
            col(3)=mean((weight**z)*y*x**2,Nb)
            
            mat_var=mat
            mat_var(:,1)=col
            a_coef(1)=deter_3(mat_var)/deter_3(mat)

            mat_var=mat
            mat_var(:,2)=col
            a_coef(2)=deter_3(mat_var)/deter_3(mat)
            
            mat_var=mat
            mat_var(:,3)=col
            a_coef(3)=deter_3(mat_var)/deter_3(mat)
            
            Compute(1)= mean(w,Nb) - (std(w,Nb)*a_coef(2))/(2*a_coef(3))
            Compute(2)=std(w,Nb)*sqrt((a_coef(1)/a_coef(3))-(a_coef(2)/2*a_coef(3))**2)
            Compute(3)=(pi*std(w,Nb)) /sqrt(a_coef(1)*a_coef(3) - (a_coef(2)**2 /4))
        
        end function Compute
        
        function Lorentz(omega,S,gamma,Omega_m)
            !! compute a lorentzian function
            ! Args:
            !   omega (real) : the value for it we want evaluate our Lorentzian function
            !   omega_m (real) : the first coefficient value, this is the average of x_axis for our lorentzian
            !   gamma (real) : the second coefficient value, this is the half-width at half size of our lorentzian
            !   S (real): the integral density of intensity of the spectral line
            !Returns:
            !   Lorentz (real) : value of our lorentzian for omega 
            implicit none
            real(kind=8) :: omega, S, gamma, Omega_m, Lorentz
            real , parameter :: pi=3.14159265

            Lorentz= (S*gamma)/(pi*((omega-Omega_m)**2 + gamma**2))

        end function Lorentz

        character(len=20) function str(k)
        !! change the type of k into string
            ! Args:
            !   k (integer) : the integer that we want to change
            !Returns:
            !   str (character) : the character k
            integer, intent(in) :: k
            write (str, *) k
            str = adjustl(str)
        end function str

end module TP1_mod
