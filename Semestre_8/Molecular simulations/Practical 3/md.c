#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include "ran_uniform.h"
#include "system.h"


int main(void) { 
  time_t  tstart,tend;
    
    printf("    ----------------------------------------  \n");
    printf("   |   A simple Molecular Dynamics program  | \n");
    printf("    ----------------------------------------  \n");
 
  // initialize the random number generator with the system time
  InitializeRandomNumberGenerator(time(0l));

  // Read Data
  Readdat();
 
  time(&tstart);
  
  // Generate Initial Coordinates/Velocities
  Init();
 
  // Finally, Perform An Md Simulation 
  Mdloop();
  
  time(&tend);
  printf("\nTime elapsed: %d seconds.\n",(int)(tend-tstart));
  
  return 0; 
}
