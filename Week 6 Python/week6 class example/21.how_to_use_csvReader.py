

# to load list of dicts from csv
stats = []
with open(path, newline='', encoding='utf-8') as f:
    # newline = '' is to make reader know when to end row Without it,
        # on Windows Python might turn \n into \r\n (or vice-versa)
        # and the CSV reader could get confused,
        # thinking you have blank rows.
    # encoding='utf-8' is how the encoding of the file done
    reader = csv.DictReader(f)
    for row in reader:
        stats.append({
            "name":           row["name"],
            "word_count":     int(row["word_count"]),
            "letter_count":   int(row["letter_count"]),
            "sentence_count": int(row["sentence_count"]),
        })

# to load all file in string
with open("yourfile.csv", "r", encoding="utf-8") as f:
        # no need for adding newline = "" due to reading all file 
        whole_text = f.read()
