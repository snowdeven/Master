#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include "system.h"

#define Maxx 500

// samples the radial distribution function
void SampleRDF(int Ichoice)
{
  int i,j;
  double r2;
  static double Ggt,Gg[Maxx],Delta;
  VECTOR dr;
  FILE *FilePtr;

  switch(Ichoice)
  {
    case INITIALIZE:
      for(i=0;i<Maxx;i++)
        Gg[i]=0.0;

      Ggt=0.0;
      Delta=Box/(2.0*Maxx);
      break;
    case SAMPLE:
      Ggt+=1.0;
      // loop over all pairs
      for(i=0;i<NumberOfParticles-1;i++)
      {
        for(j=i+1;j<NumberOfParticles;j++)
        {
          dr.x=Positions[i].x-Positions[j].x;
          dr.y=Positions[i].y-Positions[j].y;
          dr.z=Positions[i].z-Positions[j].z;

          // apply boundary conditions
          dr.x-=Box*rint(dr.x/Box);
          dr.y-=Box*rint(dr.y/Box);
          dr.z-=Box*rint(dr.z/Box);

          r2=sqrt(SQR(dr.x)+SQR(dr.y)+SQR(dr.z));

          // calculate in which bin this interaction is in
          if(r2<0.5*Box)
            Gg[(int)(r2/Delta)]+=2.0;
        }
      }
      break;
    case WRITE_RESULTS:
      // Write Results To Disk
      FilePtr=fopen("rdf.dat","w");
      fprintf(FilePtr,"#   r      g(r)\n");
      for(i=0;i<Maxx-1;i++)
      {
        r2=(4.0*M_PI/3.0)*(NumberOfParticles/CUBE(Box))*CUBE(Delta)*(CUBE(i+1)-CUBE(i));
        fprintf(FilePtr,"%f %f\n",(i+0.5)*Delta,Gg[i]/(Ggt*NumberOfParticles*r2));
      }
      fclose(FilePtr);
      break;
  }
}

// samples the velocity distribution function
void SampleVelDistr(int Ichoice)
{
  FILE *FilePtr;
  int i; // indexing variable
  int index; // index within the VelDist array
  double sum; // sum of the bins
  double vx,vy,vz,v; // velocities in x,y.z and magniture of \vec v
  
  const int n_bins=50; // number of bins is a pre-defined constant
  static double Delta; // incremnet between bins
  static double VelDist[50]; // array to store the histogram
  
  switch(Ichoice)
  {
    case INITIALIZE:
      //printf("Initialize velocity distribution");
      for(i=0;i<n_bins;i++) VelDist[i]=0.0;
      Delta=0.1*sqrt(Temperature); // higher temperature requires wider bins, the form for Delta(t) found by trial and error and works for our temperature ranges but may not work outside of them
      break;
    case SAMPLE:
      // loop over all pairs
      for(i=0;i<NumberOfParticles;i++)
      {
        vx=Velocities[i].x;
        vy=Velocities[i].y;
        vz=Velocities[i].z;
	v=sqrt(vx*vx+vy*vy+vz*vz);
        // calculate to which bin current "v" falls
	index=(int)(v/Delta);
	if(index<n_bins) {
          VelDist[index]+=1.0;
	}  else {
	  // all overflow values are written to the last entry
          VelDist[n_bins-1]+=1.0;
	}
      }
      break;
    case WRITE_RESULTS:
      // Renormalize it first
      sum=0.0;
      for(i=0;i<n_bins;i++) sum+=VelDist[i];
      // Write Results To Disk
      FilePtr=fopen("VelDist.dat","w");
      if(FilePtr==NULL) fprintf(stderr,"Cannot open VelDist.dat\n");
      fprintf(FilePtr,"#   v    f(v)\n");
      for(i=0;i<n_bins;i++) {
        fprintf(FilePtr,"%e   %6e\n",(i+0.5)*Delta,VelDist[i]/(sum*Delta));
      }
      fclose(FilePtr);
      break;
  }
}
