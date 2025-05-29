#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int points(string x);
int compares(char x, string y);

int main(void)
{
    string p1 = get_string("Player 1: ");
    string p2 = get_string("Player 2: ");

    int cnt1 = points(p1);
    int cnt2 = points(p2);

    if (cnt1 > cnt2)
    {
        printf("Player 1 wins! \n");
    }
    else if (cnt1 < cnt2)
    {
        printf("Player 2 wins! \n");
    }
    else if (cnt1 == cnt2)
    {
        printf("Tie! \n");
    }
}

int points(string x)
{
    int ln = strlen(x);
    int ans = 0;
    string one = "aeilnorstu";
    string two = "dg";
    string three = "bcmp";
    string four = "fhvwy";

    for (int i = 0; i < ln; i++)
    {
        char a = tolower(x[i]);

        if (compares(a, one) == 0)
        {
            ans++;
        }
        else if (compares(a, two) == 0)
        {
            ans += 2;
        }
        else if (compares(a, three) == 0)
        {
            ans += 3;
        }
        else if (compares(a, four) == 0)
        {
            ans += 4;
        }
        else if (a == 'k')
        {
            ans += 5;
        }
        else if (a == 'j' || a == 'x')
        {
            ans += 8;
        }
        else if (a == 'q' || a == 'z')
        {
            ans += 10;
        }
    }

    return ans;
}

int compares(char x, string y)
{
    int ln = strlen(y);

    for (int i = 0; i < ln; i++)
    {
        if (x == y[i])
        {
            return 0;
        }
    }

    return 1;
}
