#include <cs50.h>
#include <stdio.h>
 // this is the mario blocks using recursion
void draw(int h);

int main(void)
{
    int h = get_int("Height:  ");
    draw(h);
}

void draw(int h)
{
    if (h <= 0)
    {
        return;
    }
    draw(h-1);

    for (int i = 0; i < h; i++ )
    {
        printf("#");
    }
    printf("\n");
}
