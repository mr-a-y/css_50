

# this is how you create a dictionairy
people = {"ali" :"416", "malak" :"647", "yassine" : "905"}

name = input("give me number")
#how to look in dictionairies values 
if name in people :
    print(f"found you mf here is your number {people[name]}")
else:
    print("you not in this mf ")
