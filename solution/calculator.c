#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
    char buf[10];
    char buf2[10];
    char buf3[10];
    int a1;
    int a2;

    printf("Welcome to the calculator.\n");
    printf("What operation would you like to perform?\n");
    printf("\t(a)ddition\n\t(s)ubtraction\n\t(m)ultiplication\n");
    fgets(buf, 10, stdin);

    printf("Enter first number: ");
    fgets(buf2, 10, stdin);
    a1 = atoi(buf2);
    printf("Enter second number: ");
    fgets(buf3, 10, stdin);
    a2 = atoi(buf3);

    if (strcmp(buf,"a\n") == 0) {
        printf("The sum is %d\n", a1+a2);
    }
    else if (strcmp(buf,"s\n") == 0) {
        printf("The difference is %d\n", a1-a2);
    }
    else if (strcmp(buf,"m\n") == 0) {
        printf("The product is %d\n", a1*a2);
    }
}