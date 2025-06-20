#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>


int main(void)
{
    FILE *input = fopen("large" ,"r");
    int a = 0;
    int b = 0;
    int c = 0;
    int d = 0;
    char word[50];
    while (fscanf(input, "%s", word) != EOF)
    {
        if (word[0] == '\'')
        {
            a++;
        }
        if (word[1] == '\'' )
        {
            b++;
        }
        if (word[2] == '\'')
        {
            c++;
        }
        if (word[1] == '\'' && word[2] == '\'' )
        {
            d++;
        }


    }
    fclose(input);
    printf("how many commas in first place  = %i \n",a);
    printf("how many commas in second place  = %i \n",b);
    printf("how many commas in third  place  = %i \n",c);
    printf("how many times comma in the second followed in 3rd = %i \n",d);

}
