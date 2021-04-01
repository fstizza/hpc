#include "papi.h"
#include <stdlib.h>
#include <stdio.h>

/*
gcc hello_world.c -I/${PAPI_DIR}/include -L/${PAPI_DIR}/lib -o hello_world -lpapi
./hello_world

export PAPI_EVENTS="PAPI_TOT_INS,PAPI_TOT_CYC"
export PAPI_OUTPUT_DIRECTORY="scratch/measurement"

*/

int main()
{
    int retval;

    retval = PAPI_hl_region_begin("computationAA");
    if ( retval != PAPI_OK )
        exit(1);

    /* Do some computation here */
    double r = 0.000001;
    for (size_t i = 0; i < 1000000; i++)
    {
        r += 0.000001;
    }


    printf("Res: %f\n",r);

    retval = PAPI_hl_region_end("computationAA");
    if ( retval != PAPI_OK )
        exit(1);

    printf("Retval!: %d\n", retval);
}
