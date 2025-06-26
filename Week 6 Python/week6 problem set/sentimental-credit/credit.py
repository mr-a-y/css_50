

credit = input("Number : ")
ln = len(credit)
degit = int(credit[:2])
check = 0
count = 10
for _ in range(ln):
    if _ == 0:
        check = int(credit) % count
    elif _ % 2 == 1:
        temp = (int(credit) % count) // (count // 10)
        if temp < 5:
            check += temp * 2
        else:
            check += temp * 2 - 9
    else:
        temp = (int(credit) % count) // (count / 10)
        check += temp
    count *= 10

check %= 10

if ln == 15 and (degit == 34 or degit == 37) and check == 0:
    print("AMEX")
elif ln == 16 and (degit >= 51 and degit <= 55) and check == 0:
    print("MASTERCARD")
elif (ln == 13 or ln == 16) and (degit >= 40 and degit <= 49) and check == 0:
    print("VISA")
else:
    print("INVALID")



