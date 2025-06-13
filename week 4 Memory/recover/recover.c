#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{

    if (argc != 2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }

    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("could not open file.\n");
        return 1;
    }

    uint8_t buffer[512];
    int counter = 0;
    FILE *image = NULL;
    char filename[8];

    while (fread(buffer, 1, 512, input) == 512)
    {
        sprintf(filename, "%03i.jpg", counter);

        if ((buffer[0] == 0xff) && (buffer[1] == 0xd8) && (buffer[2] == 0xff) &&
            ((buffer[3] & 0xf0) == 0xe0))
        {
            if (image != NULL)
            {
                fclose(image);
            }

            image = fopen(filename, "w");
            if (image == NULL)
            {
                printf("could not create file.\n");
                return 1;
            }
            fwrite(buffer, 1, 512, image);
            counter++;
        }
        else if (counter > 0)
        {
            fwrite(buffer, 1, 512, image);
        }
    }
    fclose(input);
    if (image != NULL)
    {
        fclose(image);
    }
}
