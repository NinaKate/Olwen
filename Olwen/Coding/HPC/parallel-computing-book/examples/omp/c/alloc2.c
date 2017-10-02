/* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
   %%%%
   %%%% This program file is part of the book and course
   %%%% "Parallel Computing"
   %%%% by Victor Eijkhout, copyright 2013-6
   %%%%
   %%%% alloc2.c : dealing with statically allocated data
   %%%%
   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
*/

#include <stdlib.h>
#include <stdio.h>
#include <omp.h>

int main(int argc,char **argv) {

  int nthreads;
#pragma omp parallel
#pragma omp master
  nthreads = omp_get_num_threads();

  int array[nthreads];
  for (int i=0; i<nthreads; i++)
    array[i] = 0;

#pragma omp parallel firstprivate(array)
  {
    int t = omp_get_thread_num();
    array[t] = t;
  }

  printf("Array result:\n");
  for (int i=0; i<nthreads; i++)
    printf("%d:%d, ",i,array[i]);
  printf("\n");

  return 0;
}
