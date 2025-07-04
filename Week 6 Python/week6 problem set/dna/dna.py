import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("wrong number of files")
        sys.exit(1)
    else:
        database_path = sys.argv[1]
        dna_path = sys.argv[2]


    # TODO: Read database file into a variable
    database = []
    header = []
    with open(database_path, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        header = reader.fieldnames

        for _ in reader:
            temp = {}
            for i in header:
                temp.update({i :_[i] })
            database.append(temp)


    # TODO: Read DNA sequence file into a variable
    with open(dna_path, "r", encoding = "utf-8") as file:
        dna = file.read()


    # TODO: Find longest match of each STR in DNA sequence
    match = {}
    for _ in header:
        match.update({_ : str(longest_match(sequence = dna, subsequence = _))})

    # TODO: Check database for matching profiles


    for _ in database:
        temp1 = _.copy()
        temp2 = match.copy()
        temp1.pop("name",None)
        temp2.pop("name",None)
        if temp1 == temp2:
            print(f"{_["name"]}")
            break
    else:
        print("No match")
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
