
// Stochastic velocity rescale, as described in
// Bussi, Donadio and Parrinello, J. Chem. Phys. 126, 014101 (2007)
//
// This subroutine implements Eq.(A7) and returns the new value for the kinetic energy,
// which can be used to rescale the velocities.
// The procedure can be applied to all atoms or to smaller groups.
// If it is applied to intersecting groups in sequence, the kinetic energy
// that is given as an input (kk) has to be up-to-date with respect to the previous rescalings.
//
// When applied to the entire system, and when performing standard molecular dynamics (fixed c.o.m. (center of mass))
// the degrees of freedom of the c.o.m. have to be discarded in the calculation of ndeg,
// and the c.o.m. momentum HAS TO BE SET TO ZERO.
// When applied to subgroups, one can chose to:
// (a) calculate the subgroup kinetic energy in the usual reference frame, and count the c.o.m. in ndeg
// (b) calculate the subgroup kinetic energy with respect to its c.o.m. motion, discard the c.o.m. in ndeg
//     and apply the rescale factor with respect to the subgroup c.o.m. velocity.
// They should be almost equivalent.
// If the subgroups are expected to move one respect to the other, the choice (b) should be better.
//
// If a null relaxation time is required (taut=0.0), the procedure reduces to an instantaneous
// randomization of the kinetic energy, as described in paragraph IIA.
//
// HOW TO CALCULATE THE EFFECTIVE-ENERGY DRIFT
// The effective-energy (htilde) drift can be used to check the integrator against discretization errors.
// The easiest recipe is:
// htilde = h + conint
// where h is the total energy (kinetic + potential)
// and conint is a quantity accumulated along the trajectory as minus the sum of all the increments of kinetic
// energy due to the thermostat.
//



#include <math.h>
#include "thermostat_Bussi.h"

double resamplekin(double kk,double sigma, int ndeg, double taut){
/*
  kk:    present value of the kinetic energy of the atoms to be thermalized (in arbitrary units)
  sigma: target average value of the kinetic energy (ndeg k_b T/2)  (in the same units as kk)
  ndeg:  number of degrees of freedom of the atoms to be thermalized
  taut:  relaxation time of the thermostat, in units of 'how often this routine is called'
*/
  double factor,rr;
  if(taut>0.1){
    factor=exp(-1.0/taut);
  } else{
    factor=0.0;
  }
  rr = gasdev();
  return kk + (1.0-factor)* (sigma*(resamplekin_sumnoises(ndeg-1)+rr*rr)/ndeg-kk)
            + 2.0*rr*sqrt(kk*sigma/ndeg*(1.0-factor)*factor);
}

double resamplekin_sumnoises(int nn){
/*
  returns the sum of n independent gaussian noises squared
   (i.e. equivalent to summing the square of the return values of nn calls to gasdev)
*/
  double rr;
  if(nn==0) {
    return 0.0;
  } else if(nn==1) {
    rr=gasdev();
    return rr*rr;
  } else if(nn%2==0) {
    return 2.0*gamdev(nn/2);
  } else {
    rr=gasdev();
    return 2.0*gamdev((nn-1)/2) + rr*rr;
  }
}

//
//  THE FOLLOWING ROUTINES ARE TRANSCRIBED FROM NUMERICAL RECIPES
//


// gamma-distributed random number, implemented as described in numerical recipes
double gamdev(const int ia)
{
	int j;
	double am,e,s,v1,v2,x,y;

	if (ia < 1) {}; // FATAL ERROR
	if (ia < 6) {
		x=1.0;
		for (j=1;j<=ia;j++) x *= ran1();
		x = -log(x);
	} else {
		do {
			do {
				do {
					v1=ran1();
					v2=2.0*ran1()-1.0;
				} while (v1*v1+v2*v2 > 1.0);
				y=v2/v1;
				am=ia-1;
				s=sqrt(2.0*am+1.0);
				x=s*y+am;
			} while (x <= 0.0);
			e=(1.0+y*y)*exp(am*log(x/am)-s*y);
		} while (ran1() > e);
	}
	return x;
}


// gaussian-distributed random number, implemented as described in numerical recipes
double gasdev()
{
	static int iset=0;
	static double gset;
	double fac,rsq,v1,v2;

	if (iset == 0) {
		do {
			v1=2.0*ran1()-1.0;
			v2=2.0*ran1()-1.0;
			rsq=v1*v1+v2*v2;
		} while (rsq >= 1.0 || rsq == 0.0);
		fac=sqrt(-2.0*log(rsq)/rsq);
		gset=v1*fac;
		iset=1;
		return v2*fac;
	} else {
		iset=0;
		return gset;
	}
}


// random number generator
double ran1()
{
#define NTAB 32
    //const int NTAB=32;
	const int IA=16807,IM=2147483647,IQ=127773,IR=2836;
	const int NDIV=(1+(IM-1)/NTAB);
	const double EPS=3.0e-16,AM=1.0/IM,RNMX=(1.0-EPS);
	static int iy=0;
	static int iv[NTAB];
	int j,k;
	double temp;
        static int idum=0; /* ATTENTION: THE SEED IS HARDCODED */

	if (idum <= 0 || !iy) {
		if (-idum < 1) idum=1;
		else idum = -idum;
		for (j=NTAB+7;j>=0;j--) {
			k=idum/IQ;
			idum=IA*(idum-k*IQ)-IR*k;
			if (idum < 0) idum += IM;
			if (j < NTAB) iv[j] = idum;
		}
		iy=iv[0];
	}
	k=idum/IQ;
	idum=IA*(idum-k*IQ)-IR*k;
	if (idum < 0) idum += IM;
	j=iy/NDIV;
	iy=iv[j];
	iv[j] = idum;
	if ((temp=AM*iy) > RNMX) return RNMX;
	else return temp;
}
