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
        if (zm>=2){
            mand = false;
            break;
        }
    }
    return mand;
}
int main(){
    float h = 0.01;//spacing between grid points
    float N = 4/h; //number of grid points per side
    float x=-2;
    float y=-2;
    vector<float>real;
    vector<float>imaginary;
    int numpts = 0;
    for (int i=0; i<N;i++){
        for (int j = 0;j<N;j++){
            if (Mandelbrot(x,y,10000)==true){
                real.push_back(x);
                imaginary.push_back(y);
//                cout<<x<<","<<y<<endl;
                numpts +=1;
            }
            y = -2 + h*j;
        }
        x = -2 + h*i;
    }
    cout<<"The area of the mandelbrot set is "<<numpts*h*h<<" according to this. And yeah, I have no idea what the units should be here. " <<endl;
    
}
