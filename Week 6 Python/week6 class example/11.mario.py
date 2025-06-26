import cs50


while True:
    try:
        y =cs50.getint("give me numer ") #doing this to show the concept of name spacing (make sure to chat gpt the definition nto get it better)
        x = int(input("give me number again"))
    except ValueError:
        print("you didnt give me number ")
    if x == 0:
        print("you give me zero why ")
    else:
        break

for _ in range(x):
    print("#")




