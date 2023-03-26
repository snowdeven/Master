program Ising
use,intrinsic :: ISO_Fortran_env
implicit none

!================ Parameter of the simulation ======================
integer, parameter :: N = 10                !lattice made with N*N spins
integer, parameter :: Nsteps = 10000     !nb of MC sweeps (cycles)
integer, parameter :: Nequil = 0
           !equilibration period
!--------------------------------------------------------------------
! The temperature must be given as argument to this program, for example
!            ./a.out 1.0
! to perform a simulation at temperature T = 1
! If T>0: one simulation is performed at this temperature
! Si T=0: a loop is performed over several temperature, from Ti to Tf in NstepT steps
real(REAL64) :: T                     !Temperature
real(REAL64) :: Ti, Tf                !Temperature interval
integer      :: NstepT, stepT
!===================================================================

integer, dimension(0:N-1,0:N-1) :: spin     !lattice with N x N spins
! ***********************************************************************
! WARNING: in the 'spin' array, one counts starting from 0 and not from 1S
! ***********************************************************************
integer :: i, j, k
integer :: Nspins, random_spin
integer :: step, big_step
integer(INT64) :: E, dE, M
real(REAL64)   :: r, beta, a,b,delta

integer :: nb_args
character(len=50) :: argument
character(len=100) :: filename


!Variables to compute averages
integer(INT64) :: E_acc
integer(INT64) :: M_acc
real(REAL64)   :: E_av, M_av

integer, allocatable :: seed(:), mySeed(:)
integer nbOfSeeds, clock
    
call initialize_random()    !Initialize the random number generator
!call random_number(r)        !command that assigns a random number in interval [0, 1]
                              !to the variable r

! Read the temperature given as argument
nb_args = command_argument_count()
if (nb_args == 1) then
   call get_command_argument(1, argument)
   read (argument,*) T
else
   print *, 'Error: a temperature must be given as argument'
   stop
end if

Nspins = N * N

print *, '-------------------------------------'
print *, 'N: ', N
print *, 'Nsteps: ', Nsteps
print *, 'Nequil: ', Nequil

if (T > 0) then            ! Only one simulation at a given temperature
    NstepT = 1
    Tf = T
    Ti = T
    print *, 'T: ', T
else                    ! Several simulations in a temperature interval
    NstepT = 10
    Ti = 1.5
    Tf = 3
    print *, 'T from', Ti, 'to ', Tf, 'with ', NstepT, 'simulations'
end if
print *, '-------------------------------------'

!Output files
if (NstepT == 1) then
    open(unit=10,file="data.dat")
    write(10,*) '# Cycle    Energy/N    Magnetization/N'
else
    !File M_xx.dat (where xx = N = size of lattice) containing the averages <E/N> (energy) et <M/N>
    write (filename, "(A2,I0.2,A4)") "M_", N, ".dat"   !filenames: M_05.dat,  M_10.dat, ...    
    open(unit=11,file=trim(filename))
    write(11,*) '# T  E/N  M/N'
end if
 

!===================================================================

do stepT = 1, NstepT 
    if (NstepT > 1) T = Ti + (stepT-1) * (Tf - Ti)/(NstepT - 1)
    beta = 1/T

    print *, 'Simulation ', stepT, '   (T=', T, ')'

    print *, 'Initial configuration: '
     do i = 0, N-1
        do j = 0, N-1
           call random_number(r)
                      ! <-- modify this line so that the orientation of the spin is random
           if (r<0.5) then 
            spin(i,j) = 1 
           else
            spin(i,j) = -1
           end if
            ! Hint: use int(...) or floor(...)
        end do
     end do
     
    if (NstepT == 1) call display()
 
    M = sum(spin)                   ! <-- Modify this line
    E = energy()
    print *, 'Energy per spin: ', real(E)/Nspins
    print *, 'Magnetization per spin: ', real(M)/Nspins

    E_acc = 0                          ! accumulator variable used in the computation of <E>
    M_acc = 0                          ! accumulator variable used in the computation of <M>

    do big_step = 1, Nsteps            ! loop over MC sweeps
        do step = 1, Nspins            ! loop to perform 1 sweep over the lattice

            call random_number(a)
            call random_number(b)
            call random_number(r)

            i = a*N
            j = b*N

            delta=2*spin(i,j)*(spin(modulo(i+1,N),j) &
            + spin(modulo(i-1,N),j) &
            + spin(i,modulo(j+1,N)) &
            + spin(i,modulo(j-1,N)))

            if (min(1.0_8,exp(-beta*delta)) > r ) then
                spin(i,j) = -1* spin(i,j)
                E = E + delta 
                M = M + 2*spin(i,j)
            ! else
            !     spin(i,j) = spin(i,j)
            end if
            

            !--------------------------------------------------------
            ! Modify the code here in order to:
            !   - Choose a spin at random
            !   - Attempt to flip it
            !   - Accept or reject this move
			!     (if the move is accepted, update the spin array and the variables E and M)
            !--------------------------------------------------------

            !Accumulate the values of the energy E and the magnetization M
            if (big_step > Nequil) then
                E_acc = E_acc + E
                M_acc = M_acc + M
            end if
        end do
        
        if (NstepT <= 1 .and. modulo(big_step, 2) == 0) then
           !Save the observables in file data.dat
           write(10,*) big_step, real(E)/Nspins, real(M)/Nspins
        end if
    end do
    
    print *, 'Final configuration: '
    if (NstepT == 1) call display()
    print *, 'Energy: ', real(E)/Nspins
    print *, 'Magnetization per spin: ', real(M)/Nspins

    !--------------------------------------------------------
    !Computation of the averages <E> and <M> per spin    (to be completed)
    E_av = real(E_acc)/((Nsteps-Nequil)*Nspins)          !<-- E_av should contain <E>
    M_av = real(M_acc)/((Nsteps-Nequil)*Nspins)    
    !--------------------------------------------------------

    print *, '  - Energy: ', E_av/ Nspins
    print *, '  - Magnetization: ', M_av/ Nspins
    
    if (NstepT > 1) then
        !Save the averages in file M_xx.dat
        write(11,*) T, E_av, abs(M_av)
    end if


    
    print*,E,"==",energy()

    print*,M,"==",sum(spin)
    !--------------------------------------------------------
    !Final check
    ! Check that the variable E contains indeed the correct energy by comparing it
	! to the value returned by energy()
    !--------------------------------------------------------
    
end do

if (NstepT == 1) close(10)
if (NstepT > 1)  close(11)

contains

!======================================================================
function energy()
! Computes the total energy of the spin network

   implicit none
   integer :: energy
   integer :: i, j
   energy = 0
   !Note: instead of the following two loops, one could have used a loop like
   !      forall (i=1:N, j=1:N)
   do i = 0, N-1
      do j = 0, N-1
        !Compute the energy with the 4 nearest neighbors
        energy = energy - spin(i,j)*(spin(modulo(i+1,N),j) &
                                    + spin(modulo(i-1,N),j) &
                                    + spin(i,modulo(j+1,N)) &
                                    + spin(i,modulo(j-1,N)))
      end do
   end do
   energy = energy / 2
end function

!======================================================================
subroutine display()
! Displays the spin network (using + or - symbols)

    implicit none
    character :: c
    do i = 0, N-1
       do j = 0, N-1
          if (spin(i,j) == 1) then
             c = '+'
          else
             c = '-'
          end if
          write(*,'(a1)',advance='no') c
       end do
       write(*,*) ''
    end do
end subroutine


!======================================================================
subroutine initialize_random()
!Subroutine to initialise the seeds of the random number generator

    implicit none
    call random_seed(size=nbOfSeeds)
    allocate(seed(nbOfSeeds))
    call random_seed(get=seed)
    call system_clock(COUNT=clock)
    mySeed = clock + 37 * [(i, i = 0,nbOfSeeds-1)]
    call random_seed(PUT = mySeed)
    !print *, "Seed =", mySeed
end subroutine

end program