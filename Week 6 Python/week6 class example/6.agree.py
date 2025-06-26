

a = input("do you agree  ").lower() # chaining method

#no need for () in if statment
#the "||" operator is "or"
#the in operator is used to check if a is in the list


if  a == "ye" or a == "y" or a == "yes" :
    print("ok")
elif a in ["no","n"]:
    print("why say no ") 

