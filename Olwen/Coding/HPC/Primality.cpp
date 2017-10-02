//
//  Primality.cpp
//  
//
//  Created by Nina Stein on 9/6/17.
//
//

#include <cmath>
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <math.h>
#include <vector>
#include <sstream>
using namespace std;


bool IsPrime(int test){
    vector<int> primes;
    int i = 3;
    bool prime = true;
    for (i=3;i<test;i+=2){
        if(i<9){
            primes.push_back(i);
        }
        else {
            for (int j = 0; j<primes.size();j++){
                if (i%primes[j]==0){prime = false;}
            }
            if (prime== true){primes.push_back(i);}
            
        }
    }
    prime = true;
    for (int j = 0; j<primes.size();j++){
        if (test%primes[j]==0){prime = false;}
    }
    return prime;
}
int main(){
        int testing = 0;
        cout<<"Please enter your even integer greater than 2:"<<endl;
        cin >> testing;
        vector<int> primes;
        int plen = 0;
        for (int n = 3; n < testing; n+=2){
            if (IsPrime(n)){
                primes.push_back(n);
                plen++;
            }
        }
        for (int i = 0; i <plen;i++){
            int check =0;
            check = testing - primes[i];
            if (IsPrime(check)){
                cout<<"Your even integer is the sum of "<<check<<" and "<<primes[i]<<endl;
                break;
            }
            
        }
        return 0;
    
}
