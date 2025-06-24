from cs50 import get_string
ans = get_string("what your name ?")
print("hello " + ans )
print("hello, ", ans ) # default in python print's everything after the , with a a single space in between them
print(f"hello, {ans}") #how to format a string. #the {} is called variable interpelation.


# print(*objects, sep=' ', end='\n', file=None, flush=False)
# *objects means 1 or more objects = "hello" + ans
print("hello " + ans, end="!" ) 
