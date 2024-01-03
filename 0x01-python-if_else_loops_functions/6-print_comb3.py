#!/usr/bin/python3

for digit in range(10):
    for digit2 in range(digit + 1, 10):
        if digit != 0 or digit2 != 1:
            print(f"{digit:02d}, {digit2:02d}", end="\n" if digit == 8 and digit2 == 9 else ", ")
