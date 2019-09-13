#include <stdio.h>
#include <time.h>

int main(void) {
    time_t t = time(NULL);
    struct tm *tm = localtime(&t);
    char s[64];
    strftime(s, sizeof(s), "%c", tm);
    printf("%s\n", s);
    //printf("%c\n", tm);
    
    printf("t = %d\n", t);
    printf("t = %p\n", (void*) &t);
    return 0;
    
    
    
    
}


