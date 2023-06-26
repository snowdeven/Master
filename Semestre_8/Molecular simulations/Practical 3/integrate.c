#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include "system.h" 

 
// integrate the equations of motion
void Integrate() {
  int i;
  VECTOR dr;
  
  // The following variables are already defines:
  //
  // Position of particle i: Positions[i]
  // Velocity of particle i: Velocities[i]
  // Force on particle i: Forces[i]
  // Time step: Tstep

  // Note: the forces depend on the positions of the particles.
  // The array Forces[NumberOfParticles] is already up-to-date because the function Force() has already been called.
  // Check in the code where it has been called !

 // Velocity Verlet integrator

  for(i=0;i<NumberOfParticles;i++)  {
        dr.x = Tstep*Velocities[i].x+0.5*Tstep*Tstep*Forces[i].x;
        dr.y = Tstep*Velocities[i].y+0.5*Tstep*Tstep*Forces[i].y;
        dr.z = Tstep*Velocities[i].z+0.5*Tstep*Tstep*Forces[i].z;

        // Absolute positions for calculation of MSD (mean square displacement)
        PositionsNONPDB[i].x += dr.x;
        PositionsNONPDB[i].y += dr.y;
        PositionsNONPDB[i].z += dr.z;

        // In-box positions due to periodic boundaries used for PDB
        Positions[i].x += dr.x;
        Positions[i].y += dr.y;
        Positions[i].z += dr.z;

        //Apply periodic boundary conditions
        if(Positions[i].x>=Box)
            Positions[i].x-=Box;
        else if(Positions[i].x<0.0)
            Positions[i].x+=Box;

        if(Positions[i].y>=Box)
            Positions[i].y-=Box;
        else if(Positions[i].y<0.0)
            Positions[i].y+=Box;

        if(Positions[i].z>=Box)
            Positions[i].z-=Box;
        else if(Positions[i].z<0.0)
            Positions[i].z+=Box;

    
       // Make a copy of the Forces[NumberOfParticles] array
       OldForces[i].x = Forces[i].x;
       OldForces[i].y = Forces[i].y;
       OldForces[i].z = Forces[i].z;
    }
    // Compute the new forces
    Force();

    // Update the velocities according to
    for(i=0;i<NumberOfParticles;i++) { 
        Velocities[i].x += 0.5*Tstep*(OldForces[i].x+Forces[i].x);
        Velocities[i].y += 0.5*Tstep*(OldForces[i].y+Forces[i].y);
        Velocities[i].z += 0.5*Tstep*(OldForces[i].z+Forces[i].z);
    }
    

//    if (1.) {
//        printf("f[0] = %f %f %f\n",Forces[0].x,Forces[0].y,Forces[0].z);
//    }
 
}
