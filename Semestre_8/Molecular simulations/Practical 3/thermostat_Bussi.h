//
//  resamplekin.h
//  
//
//  Created by Vincent Ballenegger on 20/10/12.
//  Copyright (c) 2012 __MyCompanyName__. All rights reserved.
//

#ifndef _resamplekin_h
#define _resamplekin_h

double resamplekin(double kk,double sigma, int ndeg, double taut);
double resamplekin_sumnoises(int nn);

double ran1();
double gasdev();
double gamdev(const int ia);

#endif
