#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// preferences[i][j] is number of voters who prefer i over j
int preferences[MAX][MAX];

// locked[i][j] means i is locked in over j
bool locked[MAX][MAX];

// Each pair has a winner, loser
typedef struct
{
    int winner;
    int loser;
} pair;

// Array of candidates
string candidates[MAX];
pair pairs[MAX * (MAX - 1) / 2];

int pair_count;
int candidate_count;

// Function prototypes
bool vote(int rank, string name, int ranks[]);
void record_preferences(int ranks[]);
void add_pairs(void);
void sort_pairs(void);
void lock_pairs(void);
void print_winner(void);
int check(int x, int y);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: tideman [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i] = argv[i + 1];
    }

    // Clear graph of locked in pairs
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            locked[i][j] = false;
        }
    }

    pair_count = 0;
    int voter_count = get_int("Number of voters: ");

    // Query for votes
    for (int i = 0; i < voter_count; i++)
    {
        // ranks[i] is voter's ith preference
        int ranks[candidate_count];

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            if (!vote(j, name, ranks))
            {
                printf("Invalid vote.\n");
                return 3;
            }
        }

        record_preferences(ranks);

        printf("\n");
    }

    add_pairs();
    sort_pairs();
    lock_pairs();
    print_winner();
    return 0;
}

// Update ranks given a new vote
bool vote(int rank, string name, int ranks[])
{
    for (int i = 0; i < candidate_count; i++)
    {
        string temp = candidates[i];
        if (strcmp(temp, name) == 0)
        {
            ranks[rank] = i;
            return true;
        }
    }

    return false;
}

// Update preferences given one voter's ranks
void record_preferences(int ranks[])
{
    for (int i = 0; i < candidate_count; i++)
    {
        int tmp1 = ranks[i];

        for (int j = i + 1; j < candidate_count; j++)
        {
            int tmp2 = ranks[j];
            preferences[tmp1][tmp2]++;
        }
    }
}

// Record pairs of candidates where one is preferred over the other
void add_pairs(void)
{
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = i + 1; j < candidate_count; j++)
        {
            int tmp1 = preferences[i][j];
            int tmp2 = preferences[j][i];

            if (tmp1 > tmp2)
            {
                pairs[pair_count].winner = i;
                pairs[pair_count].loser = j;
                pair_count++;
            }
            else if (tmp2 > tmp1)
            {
                pairs[pair_count].winner = j;
                pairs[pair_count].loser = i;
                pair_count++;
            }
        }
    }
}

// Sort pairs in decreasing order by strength of victory
void sort_pairs(void)
{

    for (int i = 0; i < pair_count - 1; i++)
    {
        int cnt = 0;
        for (int j = 0; j < pair_count - 1 - i; j++)
        {
            int tmp1 = preferences[pairs[j].winner][pairs[j].loser] -
                       preferences[pairs[j].loser][pairs[j].winner];
            int tmp2 = preferences[pairs[j + 1].winner][pairs[j + 1].loser] -
                       preferences[pairs[j + 1].loser][pairs[j + 1].winner];
            if (tmp1 < tmp2)
            {
                int winner = pairs[j].winner;
                int loser = pairs[j].loser;

                pairs[j].winner = pairs[j + 1].winner;
                pairs[j].loser = pairs[j + 1].loser;

                pairs[j + 1].winner = winner;
                pairs[j + 1].loser = loser;

                cnt++;
            }
        }

        if (cnt == 0)
        {
            break;
        }
    }
}

// Lock pairs into the candidate graph in order, without creating cycles
void lock_pairs(void)
{
    for (int i = 0; i < pair_count; i++)
    {
        int x = pairs[i].winner;
        int y = pairs[i].loser;

        if (check(x, y) == 0)
        {
            locked[x][y] = true;
        }
    }
}

// Print the winner of the election
void print_winner(void)
{
    for (int i = 0; i < candidate_count; i++)
    {
        int temp = 70;
        for (int j = 0; j < candidate_count; j++)
        {
            if (locked[j][i] == true)
            {
                temp = 0;
                break;
            }
        }
        if (temp != 0)
        {
            printf("%s\n", candidates[i]);
            return;
        }
    }
}

// this the recursive function to find if there is a cycle or not;
int check(int x, int y)
{
    if (x == y)
    {
        return 1;
    }

    for (int i = 0; i < candidate_count; i++)
    {
        if (locked[y][i] == true)
        {
            if (check(x, i) == 1)
            {
                return 1;
            }
        }
    }
    return 0;
}
