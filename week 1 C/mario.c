#include <cs50.h>
#include <stdio.h>

void make_pyramid(int n);

int main(void)
{
    int a;
    do
    {

        a = get_int("Height: ");
    }
    while (!(a <= 8 && a >= 1));

    printf("\n");
    make_pyramid(a);
}

void make_pyramid(int n)
{
    for (int i = 1; i <= n; i++)
    {
        int cnt = n - i;

        for (int j = 1; j <= n; j++)
        {
            if (cnt < j)
            {
                printf("#");
            }
            else
            {
                printf(" ");
            }
        }

        printf("  ");

        for (int j = 1; j <= i; j++)
        {
            printf("#");
        }

        printf("\n");
    }
}
