names = ["Yuliia", "David", "Jhon"]

name = input("Name: ")

for n in names:
    if name == n:
        print("Found ")
        break
else:
    print("Not found")  # else can also be used in for loops so that if you dont break out of the loop 
