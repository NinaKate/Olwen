//
//  matrixmult.cpp
//  
//
//  Created by Nina Stein on 9/28/17.
//
//


#include <iostream>
#include <stdio.h>
#include <time.h>
#include <math.h>
using namespace std;
int main(){
    int n;
    cout<<"Please provide N so I can create two NxN matrices "<<endl;
    cin>>n;
    double **A = new double*[n];
    double **B = new double*[n];
    double **C = new double*[n];
    for (size_t i = 0; i<n;i++){
        A[i] = new double[n];
        B[i] = new double[n];
        C[i] = new double[n];
    }
    
    
    clock_t t;
    t = clock();
    for (int i = 0; i<n;++i){
        for (int j = 0; j<n;++j){
            for (int k=0;k<n;++k){
                C[i][j]+=A[i][k]*B[k][j];}
        }
    }
    t = clock()-t;
    double T = (double)t/CLOCKS_PER_SEC * 1000.0;
    cout<<" the time it took to multiply two "<<n<<"x"<<n<<" matrices is " <<T<<endl;
       for (size_t i = n-1; i>0;--i){
        delete[] C[i];
        delete[] B[i];
        delete[] A[i];
    }
    delete[] C;
    delete[] B;
    delete[] A;
    return 0;
}
