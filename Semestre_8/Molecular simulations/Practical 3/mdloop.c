#include <stdlib.h> 
#include <stdio.h> 
#include <math.h> 
#include "system.h"
#include "thermostat_Bussi.h"

#define RESCALE_OFF 0
#define RESCALE_T -1
#define RESCALE_BERENDSEN -2
#define RESCALE_BUSSI -3

void Mdloop(void)
{ 
  int i,j;
  double Av[5],Av2[5],tmp,Tempz;
  int Nsamp=0; // number of sampled values
  FILE *Fileenergy,*FileVtf;
    char thermostatName[100] = "velocity rescaling";
    
  int nsteps_resample=Nsteps/10; // number of steps after which sampling velocity distribution should be re-initialized

    printf("\nSIMULATION\n");
    
    switch (Nsteps_rescale) {
        case RESCALE_OFF:
            sprintf(thermostatName,"%s","OFF");
            break;
        case RESCALE_BERENDSEN:
            sprintf(thermostatName,"%s","Berendsen (not implemented yet)");
            break;
        case RESCALE_BUSSI:
            sprintf(thermostatName,"%s","Bussi");
            break;
        default:
            if (Nsteps_rescale > 0) {
                sprintf(thermostatName,"%s (%i steps)","velocity rescaling",Nsteps_rescale);
            }
            break;
    }
    printf("\nThermostat: %s\n",thermostatName);
    printf("vacf computed by resampling after %d steps\n",nsteps_resample);

    //
    // Initiatization
    //
  FileVtf=fopen("traj.vtf","a");
  Fileenergy=fopen("observables.dat","w");
//    fprintf(Fileenergy,"@with g0\n");
//    fprintf(Fileenergy,"@    s0 legend  \"Total energy\"\n");
//    fprintf(Fileenergy,"@    s1 legend  \"Potential energy\"\n");
//    fprintf(Fileenergy,"@    s2 legend  \"Kinetic energy\"\n");
//    fprintf(Fileenergy,"@    s3 legend  \"Temperature\"\n");
//    fprintf(Fileenergy,"@    s4 legend  \"Pressure\"\n");

  fprintf(Fileenergy,"#  i    Total    Potential    Kinetic    Temperature   Pressure\n");
 
  for(i=0;i<5;i++) { 
    Av[i]=0.0;
    Av2[i]=0.0;
  }

  // initialize radial distribution function and mean-square displacement
  SampleRDF(INITIALIZE);
  SampleDiff(INITIALIZE);
  SampleVelDistr(INITIALIZE);

    printf("\n");
    printf("Step:\t UTotal/N \t UPot/N \t UKin/N \t Temperature \t Pressure\n");

    //
    // MD loop
    //
    
  for(i=0;i<Nsteps;i++) {
	  
    //Obtain the potential energy and the interaction part of the pressure
    Force();
    
   //Calculate the Kinetic Energy
      UKinetic = 0;
      for (j=0; j<NumberOfParticles; j++) 
          UKinetic+=0.5*(SQR(Velocities[j].x)+SQR(Velocities[j].y)+SQR(Velocities[j].z));
      
      //Apply thermostat
      //----------------
      //  Nsteps_rescale > 0 : apply velocity-rescaling during Nsteps_rescale
      //  Nsteps_rescale = -1: apply velocity-rescaling during the whole simulation
      //  Nsteps_rescale = -2: use Berendsen thermostat
      //  Nsteps_rescale = -3: use Bussi thermostat
      
      tmp = 1.0;
      //Velocity rescaling
      if(i<Nsteps_rescale || Nsteps_rescale == -1) {        //velocity rescaling
          tmp=sqrt(Temperature*3.0*NumberOfParticles/(2*UKinetic));
          UKinetic *= tmp*tmp;
      }
      //Other thermostat
      if (Nsteps_rescale == RESCALE_BUSSI) {
          // Bussi thermostat
          // ----------------
          double UKinetic_old = UKinetic;
          UKinetic = resamplekin(UKinetic,3*NumberOfParticles/2.0*Temperature, 3*NumberOfParticles, 46.0);
          //Note: the relaxation time of the thermstat is hard-coded
          //(tau = 46*timestep = 0.1 ps if reduced timestep = 0.001)
          
          tmp =sqrt(UKinetic/UKinetic_old);                             //  <--- modifier cette ligne


      } else if (Nsteps_rescale == RESCALE_BERENDSEN){
          //Berendsen thermostat
          // ----------------
          tmp = 1.0;
          // (Berendsen thermostat not implemented yet)
      }
      if (tmp != 1.0) {
          //scale the velocities by the factor determined by the thermostat
          for(j=0;j<NumberOfParticles;j++)  {
              Velocities[j].x *= tmp;
              Velocities[j].y *= tmp;
              Velocities[j].z *= tmp;
          }
      }
    
    // add the kinetic part of the pressure
    Pressure +=2.0/3*UKinetic/CUBE(Box);
    UTotal = UKinetic+UPotential;
    Tempz = 2.0*UKinetic/(3.0*NumberOfParticles);
    UKinetic /= NumberOfParticles;
    UPotential /= NumberOfParticles;
    UTotal /= NumberOfParticles;
    if((i%500)==0) 
      printf("%d \t %lf \t %lf \t %lf \t %lf \t %lf\n",i,UTotal,UPotential,UKinetic,Tempz,Pressure);
    if(i%50==0) { 
      WriteVcf(FileVtf); 
      fflush(FileVtf); 
    }
    // Write down the observables for every integration step
    fprintf(Fileenergy,"%4d  %8g   %8g   %8g   %8g   %8g\n",i,UTotal,UPotential,UKinetic,Tempz,Pressure);
    
    // If we are beyond equilibration, add the instantaneous values to the averages
    if(i>Nsteps_equil) {
            Av[0]+=Tempz;
            Av[1]+=Pressure;
            Av[2]+=UKinetic;
            Av[3]+=UPotential;
            Av[4]+=UTotal;
            Av2[0]+=Tempz*Tempz;
            Av2[1]+=Pressure*Pressure;
            Av2[2]+=UKinetic*UKinetic;
            Av2[3]+=UPotential*UPotential;
            Av2[4]+=UTotal*UTotal;
           // sample radial distribution function, MSD and Velocity distribution
           SampleRDF(SAMPLE);
           SampleDiff(SAMPLE);
           SampleVelDistr(SAMPLE);
	   Nsamp++;
    }
    
    // integrate the equations of motion, get the positions and velocities at the next step
    Integrate();
  }
    
    //
    // Terminate
    //
 
  //print averages to screen
  //Nsamp=Nsteps-Nsteps_equil;
  for(i=0;i<5;i++) {
	    Av[i] /= (double)Nsamp;
    	    Av2[i] /= (double)Nsamp;
   }
   printf("\n");
   
   //print the average and standard deviation
   printf("Quantity       Average   Standard_deviation\n");
   printf("Temperature    %8g  +/-(%lf)\n",Av[0],sqrt(Av2[0]-Av[0]*Av[0]));
   printf("Pressure       %8g  +/-(%lf)\n",Av[1],sqrt(Av2[1]-Av[1]*Av[1]));
   printf("UKinetic/N     %8g  +/-(%lf)\n",Av[2],sqrt(Av2[2]-Av[2]*Av[2]));
   printf("UPotential/N   %8g  +/-(%lf)\n",Av[3],sqrt(Av2[3]-Av[3]*Av[3]));
   printf("UTotal/N       %8g  +/-(%lf)\n",Av[4],sqrt(Av2[4]-Av[4]*Av[4]));
  
  SampleDiff(WRITE_RESULTS);
  SampleRDF(WRITE_RESULTS);
  SampleVelDistr(WRITE_RESULTS);
    
    printf("\n");
    printf("Saved file: %s\n","traj.vtf");
    printf("Saved file: %s\n","observables.dat");
    printf("Saved file: %s\n","VelDist.dat");
    printf("Saved file: %s\n","msd.dat");
    printf("Saved file: %s\n","vacf.dat");
    printf("Saved file: %s\n","rdf.dat");

  fclose(Fileenergy);
  fclose(FileVtf);
}
