#include <stdlib.h>
#include <stdio.h>

#define Maxpart 1500

#define SQR(x) ((x)*(x))
#define CUBE(x) ((x)*(x)*(x))
#define MIN(x,y) ((x)<(y)?(x):(y))

enum{INITIALIZE,SAMPLE,WRITE_RESULTS};

typedef struct
{
  double x;
  double y;
  double z;
} VECTOR;

extern VECTOR Forces[Maxpart];           // forces
extern VECTOR OldForces[Maxpart];           // forces
extern VECTOR Positions[Maxpart];        // positions
extern VECTOR OldPositions[Maxpart];    // old positions
extern VECTOR Velocities[Maxpart];        // velocities
extern VECTOR PositionsNONPDB[Maxpart]; // positions that are not put back in the box

extern double Tstep;         // Timestep

extern double Box;           // Boxlengths
extern double CutOff;        // Cut-Off Radius
extern double Ecut;          // Cut-Off Energy

extern double UKinetic;      // Kinetic Energy
extern double UPotential;    // Potential Energy
extern double UTotal;        // Total Energy

extern double Temperature;   // Temperature
extern double Pressure;      // Pressure
extern double Density;      // Density

extern int Symmetry;	// Symmetry of the initial setup
extern int Nsteps;
extern int Nsteps_rescale; // Number of steps of velocity rescaling
extern int Nsteps_equil; // Number of steps which are considered as equilibration
extern int Pre_equilibrate; // flag if pre-equilibration should be performed
extern int NumberOfParticles;
extern int NumberOfInitializationSteps;

void WriteVsf(FILE *FilePtr);
void WriteVcf(FILE *FilePtr);
void WritePdb(FILE *FilePtr);
void SampleRDF(int Ichoise);
void SampleDiff(int Switch);
void SampleVelDistr(int Switch);
void Force(void);
void Integrate();
void Readdat(void);
void Init(void);
void Mdloop(void);
