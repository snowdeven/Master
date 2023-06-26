#include <stdio.h>
#include <stdlib.h>
#include <math.h> 
#include "system.h"
#include "ran_uniform.h"
 
// small number
#define TINY 0.000001 

// generates initial positions/velocities
void Init(void)
{
  FILE *vtfFile; // file to write the initial setup
  int i,j,k,Number,Nplace;
  int Nx,Ny,Nz; // Number of particles in x,y,z direction on hcp lattice
  int next=0; // which lattice dimension to increase next
  double dx,dy,dz; // Spacing between different layers on the hcp lattice
  double lat_k; // Lattice constant of the hcp lattice
  double tmp,Size;
  double Uold=0,EMStep,ForceValue; 
  
  
  // generate velocities from a Gaussian and calculate the kinetic energy 
  UKinetic=0.0;
  for(i=0;i<NumberOfParticles;i++)
  {
    Velocities[i].x=RandomGaussianNumber();
    Velocities[i].y=RandomGaussianNumber();
    Velocities[i].z=RandomGaussianNumber();
    UKinetic+= 0.5*(SQR(Velocities[i].x)+SQR(Velocities[i].y)+SQR(Velocities[i].z));
  }
  
  tmp=sqrt(Temperature*3.0*NumberOfParticles/(2*UKinetic));
  for(i=0;i<NumberOfParticles;i++)  {
    Velocities[i].x*=tmp;
    Velocities[i].y*=tmp;
    Velocities[i].z*=tmp;
  }
  UKinetic *=tmp*tmp;
 
    printf("\n");
    printf("INITIALIZATION\n");
    fflush(stdout);

  // calculate initial positions on a lattice
  Nplace=0; // number of already placed particles
    
  if(Symmetry==0) {     //Symmetry = StartupConfiguration
      
      if (Pre_equilibrate == 0) {
          printf("Warning: a random initial configuration may contain too much potential energy which will make the system explode. Turn on initial energy minimization!\n"); fflush(stdout);

      }
    for(i=0;i<NumberOfParticles;i++) {
      Positions[i].x=RandomNumber()*Box;
      Positions[i].y=RandomNumber()*Box;
      Positions[i].z=RandomNumber()*Box;
    }
  } else if(Symmetry==1) {
    Number=(int)(ceil(pow(NumberOfParticles,1.0/3.0)));
    Size=(1.0-TINY)*Box/(double)Number;
    Nplace=0;
    printf ("pid   i    j     k         x          y       z     \n");
    for(i=0;i<Number;i++) {
       for(j=0;j<Number;j++) {
         for(k=0;k<Number;k++)     {
           if(Nplace<NumberOfParticles)   {
	     // almost simple cubic lattice with small random deviations
             Positions[Nplace].x=(i+TINY*(RandomNumber()-0.5))*Size;
             Positions[Nplace].y=(j+TINY*(RandomNumber()-0.5))*Size;
             Positions[Nplace].z=(k+TINY*(RandomNumber()-0.5))*Size;
	     printf ("%03d  %03d %03d %03d   %6g  %6g  %6g\n",Nplace,i,j,k,Positions[Nplace].x, Positions[Nplace].y,Positions[Nplace].z);
           }
           Nplace++;
         }
       }
    }
    printf("We would need %d particles to produce a lattice without defects\n",Number*Number*Number);
  } else if(Symmetry==2) {
    lat_k=pow((1.0+TINY)/(Density),1.0/3.0); 
    // The following lines give us the exact Nx, Ny and Nz in the limit of infinite system
    // In a finite system, a mismatch will always occur
    Nx=(int)floor((Box/lat_k));
    Ny=(int)floor((2.0*Box/(sqrt(3.0)*lat_k)));
    Nz=(int)floor((Box/(sqrt(6.0)/3.0*lat_k)));
    // Check if it fits in and adjust Nx, Ny and Nz
    while(Nx*Ny*Nz<NumberOfParticles) {
      printf("%d x %d x %d will not fit, try to increase lattice size\n",Nx,Ny,Nz);
      if(next==0) {
        Nx+=1;
	next=1;
      } else if (next==1) { 
        Ny+=1;
	next=2;
      } else if (next==1) { 
        Nz+=1;
	next=3;
      } else { 
          printf("Problem: even %d x %d x %d will not fit, there must be some way out of here ... Exit!\n",Nx,Ny,Nz);
          exit(1);
      }
    }
    printf("Lattice size: %d x %d x %d\n",Nx,Ny,Nz);
    printf("We would need %d particles to produce a lattice without defects\n",Nx*Ny*Nz);
    // If it fits, re-adjust dx, dy, dz so that we fill the box
    dx=Box/Nx;
    dy=Box/Ny;
    dz=Box/Nz;
    printf("Box size: %lf\n",Box);
    for(i=0;i<Nx;i++) {
       for(j=0;j<Ny;j++) {
         for(k=0;k<Nz;k++)     {
           if(Nplace<NumberOfParticles)   {
	     //printf("Place particle %d at %d,%d,%d at ",Nplace,i,j,k);
	     //printf("%g,%g,%g\n",i*dx,j*dy,k*dz);
             Positions[Nplace].x=((i+0.5*(j%2)+0.5*(k%2)+TINY*(RandomNumber()-0.5)) * dx);
             Positions[Nplace].y=((j+                    TINY*(RandomNumber()-0.5)) * dy);
             Positions[Nplace].z=((k+                    TINY*(RandomNumber()-0.5)) * dz);
           } else break;
           Nplace++;
         }
       }
    }
  } else {
    fprintf(stderr,"Error: StartupConfiguration=%d is not an allowed value\n",Symmetry);
    exit(1);
  }
  // Put all particles are inside the box
  for(i=0;i<NumberOfParticles;i++) {
    while(Positions[i].x<0.0-TINY*Box) { 
      Positions[i].x+=Box;
    }
    while(Positions[i].x>Box+TINY*Box) { 
      Positions[i].x-=Box;
    }
    while(Positions[i].y<0.0-TINY*Box) { 
      Positions[i].y+=Box;
    }
    while(Positions[i].y>Box+TINY*Box) { 
      Positions[i].y-=Box;
    }
    while(Positions[i].z<0.0-TINY*Box) { 
      Positions[i].z+=Box;
    }
    while(Positions[i].z>Box+TINY*Box) { 
      Positions[i].z-=Box;
    }
  }
  vtfFile=fopen("traj.vtf","w");
  WriteVsf(vtfFile);
  WriteVcf(vtfFile);
  fclose(vtfFile);
//  vtfFile=fopen("traj.vtf","w");
//  WriteVsf(vtfFile);
//  WriteVcf(vtfFile);
  
 //Energy Minimization: steepest descent algorithm
  if(!Pre_equilibrate) {
      ;//printf("Skipping initial energy minimization\n\n"); fflush(stdout);
  } else {
    EMStep = 0.01*Box;
    printf("\nEnergy minimization:\n"); fflush(stdout);
    for(i=0; i<500; i++)  {
      if(i==0)  {
        Force();
        Uold = UPotential;
        printf("Before minimization: Upot = %10.4f\nMinimizing the potential energy...\n",Uold);
      }
 
      for (j=0; j<NumberOfParticles; j++) {
        ForceValue = sqrt(SQR(Forces[j].x)+SQR(Forces[j].y)+SQR(Forces[j].z));
        Positions[j].x += EMStep*Forces[j].x/ForceValue;
        Positions[j].y += EMStep*Forces[j].y/ForceValue;
        Positions[j].z += EMStep*Forces[j].z/ForceValue;
        //periodic boundary condition
        if(Positions[j].x<0)  
          Positions[j].x += Box;
        else if(Positions[j].x>=Box)
          Positions[j].x -= Box;
        if(Positions[j].y<0)  
          Positions[j].y += Box;
        else if(Positions[j].y>=Box)
          Positions[j].y -= Box;
        if(Positions[j].z<0)  
          Positions[j].z += Box;
        else if(Positions[j].z>=Box)
          Positions[j].z -= Box;
      }
 
      // calculate new potential energy
      Force();
       
      // check if the new positions are acceptable
      if (fabs((UPotential-Uold)/Uold) < 0.0001 || UPotential == 0) {
        printf("After minimization: UPot/N: %8g (reached after %d minimization steps)\n\n",UPotential/NumberOfParticles,i);
        break;
      } else {
        if(UPotential<Uold) 
          EMStep *= 1.5;
        else 
          EMStep *= 0.5;
          Uold=UPotential;
      }
    }
  }
  
  //The function PositionNONPDB is used to calculate the MSD
  for (j=0; j<NumberOfParticles; j++) {
	  PositionsNONPDB[j].x=Positions[j].x;
	  PositionsNONPDB[j].y=Positions[j].y;
	  PositionsNONPDB[j].z=Positions[j].z;
  }
  
  
 } 
