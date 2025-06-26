import re

text = input("Text:")

w_cnt = len(text.split())
s_cnt = text. count(".") + text.count("?") + text.count("!")
l_cnt = letters = sum(1 for ch in text if ch.isalpha())

L = l_cnt / w_cnt * 100
S = s_cnt / w_cnt * 100

index = 0.0588 * L - 0.296 * S - 15.8
grade = round(index)


if index < 1:
        print("Before Grade 1")
elif index >= 16:
        print("Grade 16+")
else:
        print(f"Grade {grade}")



