x  = int(input("give me second number "))
y = int(input("give second number"))


#trunctation isnt a issue in python unlike c where it would give the lowerbound of the int
ans1 = x / y

# if you want trunction you can use the "//" instead of "/" for division and you will recieve such results
ans2 = x//y

print(ans1)
print(ans2)

#however theres still floating-point imprecision
#also this is how you print to a floating point value of 50
#interger overflow isnt a issue due to pythn does realloc for you 
print(f"{ans1:.50f}")
