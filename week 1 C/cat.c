#include <cs50.h>
#include <stdio.h>

void meow(int n);
int get_positive_int(void);

int main(void)
{
    // this is how you make comments
    const int b = 3;
    int a = get_positive_int();
    meow(a);
}

void meow(int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("meow\n");
    }
}

int get_positive_int(void)
{
    int n;
    do
    {
        n = get_int("Number: ");
    }
    while (n < 1);
    return n;
}
