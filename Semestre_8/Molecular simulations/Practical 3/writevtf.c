#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include "system.h"

// store the trajectory in the vtf format
void WriteVcf(FILE *FilePtr)
{
  int i;
  fprintf(FilePtr,"timestep ordered\n");
  for(i=0;i<NumberOfParticles;i++)
  {
    fprintf(FilePtr,"%.6g %.6g  %.6g \n", Positions[i].x/Box,Positions[i].y/Box,Positions[i].z/Box);
  }
  fprintf(FilePtr,"\n");
  return;
}

void WriteVsf(FILE *FilePtr)
{
  //int i;
  fprintf(FilePtr,"pbc 1.0 1.0 1.0\n");
  //fprintf(FilePtr,"pbc %lf %lf %lf\n",Box,Box,Box);
  fprintf(FilePtr,"atom 0:%d radius 1.0 name H type 1\n",NumberOfParticles-1);
  fprintf(FilePtr,"\n");
  return;
}

