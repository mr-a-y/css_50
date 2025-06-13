#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for(int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int r = image[i][j].rgbtRed;
            int g = image[i][j].rgbtGreen;
            int b = image[i][j].rgbtBlue;
            int ans = (int) round((r + g + b) / 3.0);

            image[i][j].rgbtRed = ans;
            image[i][j].rgbtGreen = ans;
            image[i][j].rgbtBlue = ans;

        }
    }


    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for(int i = 0; i < height; i++)
    {
        int p1 = 0;
        int p2 = width -1;

        while (p1 < p2)
        {
            RGBTRIPLE tmp = image[i][p1];
            image[i][p1] = image[i][p2];
            image[i][p2] = tmp;
            p1++;
            p2--;

        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{

    RGBTRIPLE temp[height][width];

    for(int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            temp[i][j] = image[i][j];
        }

    }


    for(int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
        if ( i == 0)
        {
            if ( j == 0)
            {
                int r_ans = temp[i][j].rgbtRed + temp[i][j + 1].rgbtRed + temp[i + 1][j].rgbtRed + temp[i + 1][j + 1].rgbtRed;
                int g_ans = temp[i][j].rgbtGreen + temp[i][j + 1].rgbtGreen + temp[i + 1][j].rgbtGreen + temp[i + 1][j + 1].rgbtGreen;
                int b_ans = temp[i][j].rgbtBlue + temp[i][j + 1].rgbtBlue + temp[i + 1][j].rgbtBlue + temp[i + 1][j + 1].rgbtBlue;

                r_ans = (int) round(r_ans/4.0);
                g_ans = (int) round(g_ans/4.0);
                b_ans = (int) round(b_ans/4.0);

                image[i][j].rgbtRed = r_ans;
                image[i][j].rgbtGreen = g_ans;
                image[i][j].rgbtBlue = b_ans;
            }
            else if (j == width - 1)
            {
                int r_ans = temp[i][j - 1].rgbtRed + temp[i + 1][j - 1].rgbtRed + temp[i][j].rgbtRed + temp[i + 1][j].rgbtRed;
                int g_ans = temp[i][j - 1].rgbtGreen + temp[i + 1][j - 1].rgbtGreen + temp[i][j].rgbtGreen + temp[i + 1][j].rgbtGreen;
                int b_ans = temp[i][j - 1].rgbtBlue + temp[i + 1 ][j - 1].rgbtBlue + temp[i][j].rgbtBlue + temp[i + 1][j].rgbtBlue;

                r_ans = (int) round(r_ans/4.0);
                g_ans = (int) round(g_ans/4.0);
                b_ans = (int) round(b_ans/4.0);

                image[i][j].rgbtRed = r_ans;
                image[i][j].rgbtGreen = g_ans;
                image[i][j].rgbtBlue = b_ans;
            }
            else
            {

                int r_ans = temp[i][j - 1].rgbtRed + temp[i][j].rgbtRed + temp[i][j + 1].rgbtRed;
                int g_ans = temp[i][j - 1].rgbtGreen + temp[i][j].rgbtGreen + temp[i][j + 1].rgbtGreen;
                int b_ans = temp[i][j - 1].rgbtBlue + temp[i][j].rgbtBlue + temp[i][j + 1].rgbtBlue;

                r_ans = r_ans + temp[i + 1][j - 1].rgbtRed + temp[i + 1][j].rgbtRed + temp[i + 1][j + 1].rgbtRed;
                g_ans = g_ans + temp[i + 1][j - 1].rgbtGreen + temp[i + 1][j].rgbtGreen + temp[i + 1][j + 1].rgbtGreen;
                b_ans = b_ans + temp[i + 1][j - 1].rgbtBlue + temp[i + 1][j].rgbtBlue + temp[i + 1][j + 1].rgbtBlue;

                r_ans = (int) round(r_ans/6.0);
                g_ans = (int) round(g_ans/6.0);
                b_ans = (int) round(b_ans/6.0);

                image[i][j].rgbtRed = r_ans;
                image[i][j].rgbtGreen = g_ans;
                image[i][j].rgbtBlue = b_ans;
            }
        }
        else if (i == height - 1)
        {
            if ( j == 0)
            {
                int r_ans = temp[i][j].rgbtRed + temp[i - 1][j].rgbtRed + temp[i][j + 1].rgbtRed + temp[i - 1][j + 1].rgbtRed;
                int g_ans = temp[i][j].rgbtGreen + temp[i - 1][j].rgbtGreen + temp[i][j + 1].rgbtGreen + temp[i - 1][j + 1].rgbtGreen;
                int b_ans = temp[i][j].rgbtBlue + temp[i - 1][j].rgbtBlue + temp[i][j + 1].rgbtBlue + temp[i - 1][j + 1].rgbtBlue;

                r_ans = (int) round(r_ans/4.0);
                g_ans = (int) round(g_ans/4.0);
                b_ans = (int) round(b_ans/4.0);

                image[i][j].rgbtRed = r_ans;
                image[i][j].rgbtGreen = g_ans;
                image[i][j].rgbtBlue = b_ans;
            }
            else if (j == width - 1)
            {
                int r_ans = temp[i][j].rgbtRed + temp[i - 1][j].rgbtRed + temp[i][j - 1].rgbtRed + temp[i - 1][j - 1].rgbtRed;
                int g_ans = temp[i][j].rgbtGreen + temp[i - 1][j].rgbtGreen + temp[i][j - 1].rgbtGreen + temp[i - 1][j - 1].rgbtGreen;
                int b_ans = temp[i][j].rgbtBlue + temp[i - 1][j].rgbtBlue + temp[i][j - 1].rgbtBlue + temp[i - 1][j - 1].rgbtBlue;

                r_ans = (int) round(r_ans/4.0);
                g_ans = (int) round(g_ans/4.0);
                b_ans = (int) round(b_ans/4.0);

                image[i][j].rgbtRed = r_ans;
                image[i][j].rgbtGreen = g_ans;
                image[i][j].rgbtBlue = b_ans;
            }
            else
            {

                int r_ans = temp[i - 1][j - 1].rgbtRed + temp[i - 1][j].rgbtRed + temp[i - 1][j + 1].rgbtRed;
                int g_ans = temp[i - 1][j - 1].rgbtGreen + temp[i - 1][j].rgbtGreen + temp[i - 1][j + 1].rgbtGreen;
                int b_ans = temp[i - 1][j - 1].rgbtBlue + temp[i - 1][j].rgbtBlue + temp[i - 1][j + 1].rgbtBlue;

                r_ans = r_ans + temp[i][j - 1].rgbtRed + temp[i][j].rgbtRed + temp[i][j + 1].rgbtRed;
                g_ans = g_ans + temp[i][j - 1].rgbtGreen + temp[i][j].rgbtGreen + temp[i][j + 1].rgbtGreen;
                b_ans = b_ans + temp[i][j - 1].rgbtBlue + temp[i][j].rgbtBlue + temp[i][j + 1].rgbtBlue;

                r_ans = (int) round(r_ans/6.0);
                g_ans = (int) round(g_ans/6.0);
                b_ans = (int) round(b_ans/6.0);

                image[i][j].rgbtRed = r_ans;
                image[i][j].rgbtGreen = g_ans;
                image[i][j].rgbtBlue = b_ans;
            }
        }
        else
        {
            if (j == 0)
            {

                int r_ans = temp[i - 1][j].rgbtRed + temp[i][j].rgbtRed + temp[i + 1][j].rgbtRed;
                int g_ans = temp[i - 1][j].rgbtGreen + temp[i][j].rgbtGreen + temp[i + 1][j].rgbtGreen;
                int b_ans = temp[i - 1][j].rgbtBlue + temp[i][j].rgbtBlue + temp[i + 1][j].rgbtBlue;

                r_ans = r_ans + temp[i - 1][j + 1].rgbtRed + temp[i][j + 1].rgbtRed + temp[i + 1][j + 1].rgbtRed;
                g_ans = g_ans + temp[i - 1][j + 1].rgbtGreen + temp[i][j + 1].rgbtGreen + temp[i + 1][j + 1].rgbtGreen;
                b_ans = b_ans + temp[i - 1][j + 1].rgbtBlue + temp[i][j + 1].rgbtBlue + temp[i + 1][j + 1].rgbtBlue;

                r_ans = (int) round(r_ans/6.0);
                g_ans = (int) round(g_ans/6.0);
                b_ans = (int) round(b_ans/6.0);

                image[i][j].rgbtRed = r_ans;
                image[i][j].rgbtGreen = g_ans;
                image[i][j].rgbtBlue = b_ans;
            }
            else if (j == width - 1)
            {

                int r_ans = temp[i - 1][j - 1].rgbtRed + temp[i][j - 1].rgbtRed + temp[i + 1][j - 1].rgbtRed;
                int g_ans = temp[i - 1][j - 1].rgbtGreen + temp[i][j - 1].rgbtGreen + temp[i + 1][j - 1].rgbtGreen;
                int b_ans = temp[i - 1][j - 1].rgbtBlue + temp[i][j - 1].rgbtBlue + temp[i + 1][j - 1].rgbtBlue;

                r_ans = r_ans + temp[i - 1][j].rgbtRed + temp[i][j].rgbtRed + temp[i + 1][j].rgbtRed;
                g_ans = g_ans + temp[i - 1][j].rgbtGreen + temp[i][j].rgbtGreen + temp[i + 1][j].rgbtGreen;
                b_ans = b_ans + temp[i - 1][j].rgbtBlue + temp[i][j].rgbtBlue + temp[i + 1][j].rgbtBlue;

                r_ans = (int) round(r_ans/6.0);
                g_ans = (int) round(g_ans/6.0);
                b_ans = (int) round(b_ans/6.0);

                image[i][j].rgbtRed = r_ans;
                image[i][j].rgbtGreen = g_ans;
                image[i][j].rgbtBlue = b_ans;
            }
            else
            {
                int r_ans = temp[i - 1][j - 1].rgbtRed + temp[i - 1][j].rgbtRed + temp[i - 1][j + 1].rgbtRed;
                int g_ans = temp[i - 1][j - 1].rgbtGreen + temp[i - 1][j].rgbtGreen + temp[i - 1][j + 1].rgbtGreen;
                int b_ans = temp[i - 1][j - 1].rgbtBlue + temp[i - 1][j].rgbtBlue + temp[i - 1][j + 1].rgbtBlue;

                r_ans = r_ans + temp[i][j - 1].rgbtRed + temp[i][j].rgbtRed + temp[i][j + 1].rgbtRed;
                g_ans = g_ans + temp[i][j - 1].rgbtGreen + temp[i][j].rgbtGreen + temp[i][j + 1].rgbtGreen;
                b_ans = b_ans + temp[i][j - 1].rgbtBlue + temp[i][j].rgbtBlue + temp[i][j + 1].rgbtBlue;

                r_ans = r_ans + temp[i + 1][j - 1].rgbtRed + temp[i + 1][j].rgbtRed + temp[i + 1][j + 1].rgbtRed;
                g_ans = g_ans + temp[i + 1][j - 1].rgbtGreen + temp[i + 1][j].rgbtGreen + temp[i + 1][j + 1].rgbtGreen;
                b_ans = b_ans + temp[i + 1][j - 1].rgbtBlue + temp[i + 1][j].rgbtBlue + temp[i + 1][j + 1].rgbtBlue;

                r_ans = (int) round(r_ans/9.0);
                g_ans = (int) round(g_ans/9.0);
                b_ans = (int) round(b_ans/9.0);

                image[i][j].rgbtRed = r_ans;
                image[i][j].rgbtGreen = g_ans;
                image[i][j].rgbtBlue = b_ans;
            }
        }
        }
    }

    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{

    RGBTRIPLE temp[height][width];

    for(int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            temp[i][j] = image[i][j];
        }

    }

    int gx[3][3] = {{-1, 0, 1},{-2, 0, 2},{-1, 0, 1}};
    int gy[3][3] = {{-1, -2, -1},{ 0,  0,  0},{ 1,  2,  1}};





    for(int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int gxr = 0;
            int gxg = 0;
            int gxb = 0;
            int gyr = 0;
            int gyg = 0;
            int gyb = 0;

            for (int i2 = -1; i2 < 2; i2++)
            {
                for (int j2 = -1; j2 < 2; j2++)
                {
                    int ck1 = i + i2;
                    int ck2 = j + j2;

                    if (ck1 >= 0 && ck1 < height && ck2 >= 0 && ck2 < width)
                    {
                        gxr += temp[ck1][ck2].rgbtRed * gx[i2 + 1][j2 + 1];
                        gxg += temp[ck1][ck2].rgbtGreen * gx[i2 + 1][j2 + 1];
                        gxb += temp[ck1][ck2].rgbtBlue * gx[i2 + 1][j2 + 1];

                        gyr += temp[ck1][ck2].rgbtRed * gy[i2 + 1][j2 + 1];
                        gyg += temp[ck1][ck2].rgbtGreen * gy[i2 + 1][j2 + 1];
                        gyb += temp[ck1][ck2].rgbtBlue * gy[i2 + 1][j2 + 1];
                    }


                }
            }




            int ansr = round(sqrt((gxr *gxr) + (gyr *gyr)));
            int ansg = round(sqrt((gxg *gxg) + (gyg *gyg)));
            int ansb = round(sqrt((gxb *gxb) + (gyb *gyb)));

            // for red

            if (ansr >= 255)
            {
                image[i][j].rgbtRed = 255;
            }
            else
            {
                image[i][j].rgbtRed = ansr;
            }

            // for green

            if (ansg >= 255)
            {
                image[i][j].rgbtGreen = 255;
            }
            else
            {
                image[i][j].rgbtGreen = ansg;
            }

            // for blue

            if (ansb >= 255)
            {
                image[i][j].rgbtBlue = 255;
            }
            else
            {
                image[i][j].rgbtBlue = ansb;
            }

        }
    }
    return;
}
