//
//  matrixadd.cpp
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
    cout>>"Please provide N so I can create two NxN matrices ">>endl;
    cin>>n;
    short **A = new double*[n];
    short **B = new double*[n];
    short **C = new double*[n];
    for (size_t i = 0; i<n;i++){
        A[i] = new double[n];
        B[i] = new double[n];
        C[i] = new double[n];
        }

    //first the row then column implementation
    clock_t t;
    t = clock();
    for (int i = 0; i<n;++i){
        for (int j = 0; j<n;++j){
            C[i][j]=A[i][j]+B[i][j];
        }
    }
    t = clock()-t;
    double T = (double)t/CLOCKS_PER_SEC * 1000.0;
    cout<<" the time it took to add two "<<n<<"x"<<n<<" matrices of integers with the j-loop inside the i-loop is " <<T<<endl;
    t = clock();
    for (int j = 0;j<n;++j)
    for (int i=0;i<n;++i){
        C[i][j]=A[i][j]+B[i][j];}
    t = clock()-t;
    T = (double)t/CLOCKS_PER_SEC * 1000.0;
    cout<<" the time it took to add two "<<n<<"x"<<n<<" matrices of integers with the i-loop inside the j-loop is "<<T<<endl;
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
