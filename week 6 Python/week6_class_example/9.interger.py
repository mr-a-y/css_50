'''
# this is how you use the try catch for python
# types of exception:
    ValueError = is when trying to put the wrong data type in a variavle like int a = "abc"
    TypeError = when trying to do opperation of the wrong data type like 1 + "1"
    ZeroDivisionError = trying to devide by zero
    Exception = catches all types pf error
# finally block is done at the end no mater what 1

'''
try:
    n = input(" give me number  ")
except ValueError:
    print("why you give me letters ")
except ZeroDivisionError:
    print("you give me nothing ")
else:
    print("you give me number ")
finally:
    print("me go sleep")
