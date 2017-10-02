//
//  HPC03.cpp
//  
//
//  Created by Nina Stein on 9/5/17.
//
//

#include <stdio.h>
#include <iostream>
#include <fstream>
#include <math.h>
#include <vector>
#include <sstream>
using namespace std;

float apple (float x){
    float ans;
    float arg = 1-pow(x,2);
    ans = sqrt(arg);
    return ans;
}


int main(){
    float N=1000;
    float i;
    float sum=0;
    for ( i = 1; i<N+1;i++){
        float check =  (i-1/2)/N;
        float temp = apple (check);
        sum = sum+temp;
        }
    float final = 4*sum/N;
    cout<<"I calculate pi to be " <<final<<endl;
    

    
    return 0;
}
