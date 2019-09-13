/*Satita Vittayaareekul sv439 167000051*/
/*command line: gcc -Wall -fPIC -shared -o newtime.so newtime.c -ldl
			     export LD_PRELOAD=$PWD/newtime.so
			     ./expire
 */
#define _GNU_SOURCE
#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <dlfcn.h>
int count=0;

time_t time(time_t *tloc)
{
  time_t (*new_time)(time_t* tloc);
  new_time = dlsym(RTLD_NEXT, "time");
  time_t returnvalue;
  //printf("count: %d\n", count);
  if(count == 0){
    count++;
    time_t *expiration = (time_t*)malloc(41);
    *expiration = 1488153600;
    *tloc = *expiration;
    time_t second = 1488153600;
    return second;
    
  }else{
    returnvalue = new_time(tloc);
  }
  
  return returnvalue;
}
