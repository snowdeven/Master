#include <stdio.h>
#include <stdlib.h> 
#include <math.h>
#include "system.h"

// Some auxiliary functions for reading the input
void skip_hashed_lines(FILE *f) {
 char c;
 int go;
 c=fgetc(f);
 if(c=='#') {
   go=1;
   while(go) {
     c=fgetc(f);
     if(c==EOF) break;
     else if(c=='\n') {
       c=fgetc(f); 
       if(c!='#') break;
     }
   }
 }
 ungetc(c,f);
 return;
}

void finish_line(FILE *f) {
 char c;
 c=fgetc(f);
 while(c!='\n') {
   if(c==EOF) {
     fprintf(stderr,"Error: unexpected EOF before all input parameters have been read");
     exit(1);
   }
   c=fgetc(f);
 }
 ungetc(c,f);
 return;
}

// read in system information
void Readdat(void) { 
  FILE *f=fopen("input.in", "r");
    
  // Read the input file
  skip_hashed_lines(f);
  if(!fscanf(f,"%d",&NumberOfParticles)) {
    fprintf(stderr,"Error: Could not read number of Particles from input file\n");
    exit(1);
  }
  finish_line(f); skip_hashed_lines(f);
  if(!fscanf(f,"%d",&Nsteps)) {
    fprintf(stderr,"Error: Could not read number of Steps from input file\n");
    exit(1);
  }
  finish_line(f); skip_hashed_lines(f);
  if(!fscanf(f,"%d",&Nsteps_equil)) {
    fprintf(stderr,"Error: Could not read number of Equilibration steps from input file\n");
    exit(1);
  }
  finish_line(f); skip_hashed_lines(f);
  if(!fscanf(f,"%d",&Nsteps_rescale)) {
    fprintf(stderr,"Error: Could not read number of Rescaling steps from input file\n");
    exit(1);
  }
  if (Nsteps_rescale > Nsteps_equil) {
    fprintf(stderr,"Error: Setting Nsteps_rescale=%d > Nsteps_equil=%d does not make sense\n",Nsteps_rescale,Nsteps_equil);
    exit(1);
  }
  finish_line(f); skip_hashed_lines(f);
  if(!fscanf(f,"%d",&Pre_equilibrate)) {
    fprintf(stderr,"Error: Could not read number Pre_equilibrate from input file\n");
    exit(1);
  }
  finish_line(f); skip_hashed_lines(f);
  if(!fscanf(f,"%lf",&Temperature)) {
    fprintf(stderr,"Error: Could not read Temperature from input file\n");
    exit(1);
  }
  finish_line(f); skip_hashed_lines(f);
  if(!fscanf(f,"%lf",&Tstep)) {
    fprintf(stderr,"Error: Could not read Timestep from input file\n");
    exit(1);
  }
  finish_line(f); skip_hashed_lines(f);
  if(!fscanf(f,"%lf",&Density)) {
    fprintf(stderr,"Error: Could not read Density from input file\n");
    exit(1);
  }
  finish_line(f); skip_hashed_lines(f);
  if(!fscanf(f,"%d",&Symmetry)) {
    fprintf(stderr,"Error: Could not read Symmetry from input file\n");
    exit(1);
  }
    if(fgetc(f)!=EOF) {
      ;//printf("Found some text beyond input parameters. This will be ignored.\n");
    }
    //printf("Successfuly finished reading input file\n");
    
    //Compute the box length
    //   we want to compute the box length 'Box' so that
    //   the resulting density (NumberOfParticles/Box^3)
    //   corresponds to the value ('Density')
    //   provided in the input file.
    //
    // note: pow(x,y) gives x^y     [pow=power]
    
    Box=pow(NumberOfParticles/Density,1.0/3.0);         //<-- compléter cette ligne
    printf("Using box size L = %.4f \n", Box);

    
  if(NumberOfParticles>Maxpart) {
    fprintf(stderr,"Sorry, maximum allowed number of particles is: %d\n",Maxpart);
    exit(1);
  }
 
  // Calculate Some Parameters
  CutOff=2.5;
  Ecut=4.0*(pow(SQR(CutOff),-6.0)-pow(SQR(CutOff),-3.0));
 
  // print information to the screen
  //printf("### Parameters ###\n");
  printf("# Number of particles              %d\n",NumberOfParticles);
  printf("# Number of integration steps      %d\n",Nsteps);
  printf("# Number of equilibration steps    %d\n",Nsteps_equil);
  printf("# Number of rescaling steps        %d\n",Nsteps_rescale);
    printf("# Energy minimization              %s\n",(Pre_equilibrate > 0)? "YES" : "NO");
  printf("# Temperature                      %g\n",Temperature);
  printf("# Timestep                         %g\n",Tstep);
  printf("# Density                          %g\n",Density);
  printf("# Startup configuration:           %d\n",Symmetry);
  printf("# Cut-Off radius                   %g\n\n",CutOff);

  printf("# Computed Box length              %g\n",Box);
//  printf("Cut-Off energy                   %f\n",Ecut);
  return;
}
