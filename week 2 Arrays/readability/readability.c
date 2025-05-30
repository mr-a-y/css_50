#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>
#include <math.h>


int main(void)
{
    string text = get_string("Text: ");
    float w_cnt = 1; // word count of the whole text.
    float l_cnt = 0; // letter count
    float s_cnt = 0; // sentence count
    int cnt = 0; // while counter


    char let = text[cnt];

    do
    {
        let = text[cnt];

        if (let == 33 || let == 46 || let == 63)
        {
            s_cnt++;
        }

        else if (let == ' ')
        {
            w_cnt++;
        }
        else if (let > 64 && let < 91)
        {
            l_cnt++;
        }
        else if (let > 96 && let < 123)
        {
            l_cnt++;
        }



        cnt++;

    }
    while (let != '\0');

    float L = (l_cnt / w_cnt) * 100;
    float S = (s_cnt / w_cnt) * 100;

    double index = 0.0588 * L - 0.296 * S - 15.8;

    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        index = round(index);
        printf("Grade %i\n",(int)index);

    }




}
