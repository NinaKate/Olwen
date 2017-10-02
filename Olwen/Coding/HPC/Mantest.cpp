//
//  Mandelbrot.cpp
//
//
//  Created by Nina Stein on 9/17/17.
//
//

#include <stdio.h>
#include <cmath>
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <math.h>
#include <vector>
#include <sstream>
using namespace std;

vector<float> compsq(float real,float imag){
    float rsq = real*real-imag*imag;
    float imsq = 2*real*imag;
    vector<float>endsq;
    endsq.push_back(rsq);
    endsq.push_back(imsq);
    return endsq;
}
bool Mandelbrot(float ci,float cj, int N){
    float zm = 0;
    bool mand = true;
    vector<float>zvec;
    zvec.push_back(0);
    zvec.push_back(0);
    vector<float> c;
    c.push_back(ci);
    c.push_back(cj);
    float zsq;
    for (int n = 0;n<N;n++){
        vector<float>temp;
        temp = compsq(zvec[0],zvec[1]);
        zvec[0] = temp[0]+ci;
        zvec[1] = temp[1]+cj;
        zm = pow((zvec[0]*zvec[0] + zvec[1]*zvec[1]),0.5);
    
        cout<<zm<<false<<endl;
        if (zm>=2){
            mand = false;
            break;
        }
    }
    return mand;
}
int main(){
    cout<<Mandelbrot(0.3,0.1,200)<<endl;
}
