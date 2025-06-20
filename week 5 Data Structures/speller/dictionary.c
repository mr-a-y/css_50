// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>


#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 19683;

// Hash table
node *table[N];

// word counter
static unsigned int word_count = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO

    int index = hash(word);
    int l = strlen(word);
    char temp[l+1];

    for (int i = 0; i < l; i++) {
        temp[i] = tolower(word[i]);
    }
    temp[l] = '\0';

    for (node *ptr = table[index] ; ptr != NULL ; ptr = ptr->next )
    {
        if (strcmp(ptr->word, temp) == 0)
        {
            return true;
        }
    }


    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    if (strlen(word) > 2)
    {
        if (isalpha(word[0]))
        {
            if (word[1] == '\'')
            {
                return ((toupper(word[0]) - 'A') * 27  + 27) * 27  + (toupper(word[2]) - 'A');
            }
            else if (word[2] == '\'')
            {
                return ((toupper(word[0]) - 'A') * 27  + (toupper(word[1]) - 'A')) * 27  + 27;
            }
            else
            {
                return ((toupper(word[0]) - 'A') * 27  + (toupper(word[1]) - 'A')) * 27  + (toupper(word[2]) - 'A') ;
            }
        }
        else
        {
            return 0;
        }
    }
    else if (strlen(word) == 2)
    {
        if (isalpha(word[0]))
        {
            if (word[1] == '\'')
            {
                return (toupper(word[0]) - 'A') * 27  + 27;
            }
            else
            {
                return ((toupper(word[0]) - 'A') * 27 ) + (toupper(word[1]) - 'A');
            }
        }
        else
        {
            return 0;
        }
    }

    else
    {
        if (isalpha(word[0]))
        {
            return (toupper(word[0]) - 'A');
        }
        else
        {
            return 0;
        }
    }
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    FILE *dict = fopen(dictionary, "r");

    if (dict == NULL)
    {
        return false;
    }

    char word[LENGTH + 1];
    while (fscanf(dict, "%s", word) != EOF)
    {
        word_count++;
        node * n = malloc (sizeof (node));

        if (n == NULL)
        {
            fclose(dict);
            return false;
        }

        strcpy(n->word, word);
        n->next =NULL;

        unsigned int i = hash(word);

        if (table[i] == NULL)
        {
            table[i] = n;
        }
        else
        {
            n->next = table[i];
            table[i] = n;
        }
    }

    fclose(dict);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return word_count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    node *n = NULL;

    for (int i = 0; i < N; i++)
    {
        n = table[i];
        while (n!=NULL)
        {
            node *tmp = n->next;
            free(n);
            n = tmp;
        }
        table[i] = NULL;
    }

    return true;
}
