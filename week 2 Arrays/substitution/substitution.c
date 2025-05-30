#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int check(int ln, string text);
string cypher(int ln1, string text, int ln2, string plt);

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("./substitution key \n");
        return 1;
    }
    else
    {
        string text = argv[1];
        int ln = strlen(argv[1]);
        if (strlen(argv[1]) != 26)
        {
            printf("Key must contain 26 characters.\n");
            return 1;
        }
        else
        {
            if (check(ln, text) == 1)
            {
                printf("the key containt a non alphabetical character \n");
                return 1;
            }
            else if (check(ln, text) == 2)
            {
                printf("the key contain a letter given more then ounce \n");
                return 1;
            }
            else
            {
                string plt = get_string("plaintext: ");
                int ln2 = strlen(plt);
                string ans = cypher(ln, text, ln2, plt);

                printf("ciphertext: %s\n", ans);
                return 0;
            }
        }
    }
}

int check(int ln, string text)
{
    int a[26];
    char b = 'a';
    for (int i = 0; i < 26; i++)
    {
        a[i] = 0;
    }

    for (int i = 0; i < 26; i++)
    {
        b = text[i];
        if (!isalpha(b))
        {
            return 1;
        }
        b = tolower(b);

        if (a[(int) b - 97] == 0)
        {
            a[(int) b - 97] = 1;
        }
        else
        {
            return 2;
        }
    }
    return 0;
}

string cypher(int ln1, string text, int ln2, string plt)
{
    char a;
    int index = 0;
    int cap = 0;
    for (int i = 0; i < ln2; i++)
    {

        a = plt[i];
        if (isalpha(a))
        {
            if (islower(a)) // is lower case
            {
                cap = 0;
                index = (int) a;
                index = index - 97;
                char veri = text[index];
                plt[i] = tolower(veri);
            }
            else
            {
                cap = 1;
                index = (int) a;
                index = index - 65;
                char veri = text[index];
                plt[i] = toupper(veri);
            }
        }
    }

    return plt;
}
