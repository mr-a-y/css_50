#include <cs50.h>
#include <stdio.h>

int main (void){
    int x = get_int("what is x?  ");
    int y = get_int("What is y?  ");

    if (x<y){
        printf("x is less then y \n");
    }
    else if (x>y){
        printf("x is greater then y \n");
    }
    else {
        printf("x is euqal then y \n");
    }

}
