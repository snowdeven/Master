module Global
    integer, parameter:: ww = 8
    real(ww) :: pi = 3.1415926535

end module

function prob(x)
   use Global
   real(ww):: x
   real(ww):: prob

    !Calculate the probability p(x)
    if (0 <= x .and. x <= 5) then
        prob = (sin(pi*x)/(5*exp((-pi*x/3))+1) + 1.5)
    else 
        prob=0
    endif

end function

program main
    use Global
    implicit none

    integer :: i, N=1000, io
    real(ww) :: x
    real(ww) :: prob
    real(ww) :: delta=0.5 ,d,r
    
    real(ww), allocatable :: position(:)


    !Random number generator variables
    integer, allocatable :: seed(:), mySeed(:)
  	integer nbOfSeeds, clock

  	!Random number generator initialisation
  	call random_seed(size=nbOfSeeds)
  	allocate(seed(nbOfSeeds))
  	call random_seed(get=seed)
  	call system_clock(COUNT=clock)
  	mySeed = clock + 37 * [(i, i = 0,nbOfSeeds-1)]
  	call random_seed(PUT = mySeed)
  	!print *, "Random number generator's seed", mySeed


	  ! Test of the generator
    call random_number(x)       !Fortran command which assigns a random number to x
    								            !in the interval [0, 1]
    print *, "Random number: ", x

    print *, 'At this point: p(x) = ', prob(x)
    print *, ''

    ! Monte Carlo calculation
    N = 1000

    print *, "Monte Carlo calculation"
    print *, "------------------"
    print *, "N: ", N

    allocate(position(N))   !Memory allocation for an array of N elements
    open(10,file="data.dat")
    do i=1,N
        position(i)= x
        Call random_number(d)
        d=((d*2)-1)*delta
        Call random_number(r)
        if (min(1.0_8,prob(x+d)/prob(x)) > r ) then
            position(i) = x+d
            x = x+d
        else
            position(i)= x
        end if
        write(10,*)position(i)
    end do
    close(10)
	deallocate(position)

    
end program
