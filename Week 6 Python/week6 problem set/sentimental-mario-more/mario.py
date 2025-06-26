import cs50 as np

h = np.get_int("Height: ")

while h <= 0 or h > 8:
    h = np.get_int("Height: ")


for i in range(1, h + 1, 1):
    temp = (" " * (h - i)) + ("#" * i) + ("  ") + ("#" * i)
    print(temp)
