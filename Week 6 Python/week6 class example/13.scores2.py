from cs50 import get_int #importing the get_int function from the cs50 library

scores = []

for _ in range(3):
    score = get_int("Scores: ")
    scores.append(score) # how to add something to a list
    #scores = scores + [score] or scores += [score]  # another way to append a list 

averages = sum(scores) / len(scores)

print(f" Averages : {averages}")
