#include "system.h"

VECTOR Positions[Maxpart];        // positions
VECTOR OldPositions[Maxpart];    // old positions
VECTOR Velocities[Maxpart];        // velocities
VECTOR Forces[Maxpart];           // forces
VECTOR OldForces[Maxpart];           // forces
VECTOR PositionsNONPDB[Maxpart]; // positions that are not put back in the box

double Tstep;         // Timestep

double Box;           // Boxlengths
double CutOff;        // Cut-Off Radius
double Ecut;          // Cut-Off Energy

double UKinetic;      // Kinetic Energy
double UPotential;    // Potential Energy
double UTotal;        // Total Energy

double Temperature;   // Temperature
double Pressure;      // Pressure
double Density; //Density

int Symmetry; // symmetry of the initial setup
int Nsteps;
int Nsteps_rescale;
int Nsteps_equil;
int Pre_equilibrate;
int NumberOfParticles;  
