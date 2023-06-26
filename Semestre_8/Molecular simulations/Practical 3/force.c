#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "system.h"
 
// Calculate The Forces And Potential Energy
void Force(void) {
  int i,j;
  double Fr,r2i,r6i;
  VECTOR dr;
 
  // set forces, potential energy and pressure to zero
  for(i=0;i<NumberOfParticles;i++)  {
    Forces[i].x=0.0;
    Forces[i].y=0.0;
    Forces[i].z=0.0;
  }
 
  UPotential=0.0;
  Pressure=0.0;
  // loop over all particle pairs
  for(i=0;i<NumberOfParticles-1;i++)  {
    for(j=i+1;j<NumberOfParticles;j++)    {
      dr.x=Positions[i].x-Positions[j].x;
      dr.y=Positions[i].y-Positions[j].y;
      dr.z=Positions[i].z-Positions[j].z;

      // find the nearest image neighbour 
      if (dr.x > Box/2)  
	      dr.x -= Box;
      else if (dr.x < -Box/2) 
	      dr.x += Box;
      if (dr.y > Box/2)  
	      dr.y -= Box;
      else if (dr.y < -Box/2) 
	      dr.y += Box;
      if (dr.z > Box/2)  
	      dr.z -= Box;
      else if (dr.z < -Box/2) 
	      dr.z += Box;
      r2i=SQR(dr.x)+SQR(dr.y)+SQR(dr.z);

      // check if the distance is within the cutoff radius
      if(r2i<SQR(CutOff))  {
          //r2i corresponds to 1/r^2
        r2i=1.0/r2i;
        r6i=CUBE(r2i);
 
	// Finish the following two lines to enable the calculation of
	// the truncated Lennard-Jones potential
    // Fr is the scalar product F.r = |F||r|

        UPotential += 4.0 * (SQR(r6i) - r6i) - Ecut;
        Fr = 48.0 * (SQR(r6i) - 0.5*r6i);
        

        Pressure+=Fr;
        Fr=Fr*r2i;
 
        Forces[i].x+=Fr*dr.x;
        Forces[i].y+=Fr*dr.y;
        Forces[i].z+=Fr*dr.z;
 
        Forces[j].x-=Fr*dr.x;
        Forces[j].y-=Fr*dr.y;
        Forces[j].z-=Fr*dr.z;
      }
    }
  }
 
  // the interaction part of the pressure
  Pressure/=3.0*CUBE(Box);
} 
