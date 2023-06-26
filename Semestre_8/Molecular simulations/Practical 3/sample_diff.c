#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "system.h"

// Tmax  = maximum timesteps for the correlation time
// T0max = maximum number of time origins 

#define Tmax  75000
#define T0max 2500

void SampleDiff(int Switch)
{
  int Ttel,i,T,Dt;
  static int Tvacf,Tt0[T0max],T0;
  static double Vacf[Tmax],Nvacf[Tmax],R2t[Tmax];
  static double Vxt0[Maxpart][T0max],Vyt0[Maxpart][T0max],Vzt0[Maxpart][T0max];
  static double Rx0[Maxpart][T0max],Ry0[Maxpart][T0max],Rz0[Maxpart][T0max];
  FILE *FilePtrMsd,*FilePtrVacf;

  switch(Switch)
  {
    // initialize everything
    case INITIALIZE:
      Tvacf=0;
      T0=0;
      for(i=0;i<Tmax;i++) {
        R2t[i]=0.0;
        Nvacf[i]=0.0;
        Vacf[i]=0.0;
      }
      break;
    case SAMPLE:
      Tvacf++;
      if((Tvacf%50)==0)   {
        // new time origin
        // store the positions/velocities; the current velocities
        // are Velocities[i] and the current positions are PositionsNONPDB[i].
        // question: why do you have to be careful with Pbc ?
        // make sure to study algorithm 8 (page 91) of Frenkel/Smit
        // before you start to make modifications
        // note that most variable names are different here then in
        // Frenkel/Smit. in this Way, you will have to think more... 

        // start modification
          T0++;
          Ttel=(T0-1)%T0max;
	  //printf("\nTvacf,T0,Tomax,Ttel=%5d, %5d, %5d, %5d",Tvacf,T0,T0max,Ttel);
          Tt0[Ttel]=Tvacf;

          // store particle positions/velocities

          for(i=0;i<NumberOfParticles;i++) {
            Rx0[i][Ttel]=PositionsNONPDB[i].x;
            Ry0[i][Ttel]=PositionsNONPDB[i].y;
            Rz0[i][Ttel]=PositionsNONPDB[i].z;
            Vxt0[i][Ttel]=Velocities[i].x;
            Vyt0[i][Ttel]=Velocities[i].y;
            Vzt0[i][Ttel]=Velocities[i].z;
          }

        // end modification
      }

      // loop over all time origins that have been stored

      // start modification
         for(T=0;T<MIN(T0,T0max);T++) {
           Dt=Tvacf-Tt0[T];

           // only if the time difference is shorter than the maximum correlation time
           if(Dt<Tmax) {
             Nvacf[Dt]+=1.0;

             for(i=0;i<NumberOfParticles;i++)  {
               Vacf[Dt]+=Velocities[i].x*Vxt0[i][T]+Velocities[i].y*Vyt0[i][T]+Velocities[i].z*Vzt0[i][T];
               R2t[Dt]+=SQR(PositionsNONPDB[i].x-Rx0[i][T])+
                        SQR(PositionsNONPDB[i].y-Ry0[i][T])+
                        SQR(PositionsNONPDB[i].z-Rz0[i][T]);
             }
           }
         }
      // end modification
      break;
    case WRITE_RESULTS:
      // write everything to disk
      FilePtrMsd=fopen("msd.dat","w");
      FilePtrVacf=fopen("vacf.dat","w");
       for(i=0;i<Nsteps-Nsteps_equil;i++)   {
        if(Nvacf[i]>=0.5) {
          Vacf[i]/=(NumberOfParticles*Nvacf[i]);
          R2t[i]/=(NumberOfParticles*Nvacf[i]);
        } else  {
          Vacf[i]=0.0;
          R2t[i]=0.0;
        }
        fprintf(FilePtrVacf,"%6f    %8f\n",i*Tstep,Vacf[i]);
        fprintf(FilePtrMsd,"%6f   %8f\n",i*Tstep,R2t[i]);
      }
      fclose(FilePtrVacf);
      fclose(FilePtrMsd);
  }
}
