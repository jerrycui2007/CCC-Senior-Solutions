# https://dmoj.ca/problem/ccc05s1
t = int(input())

new_phone_numbers = []

for _ in range(t):
    original_phone_number = input()
    new_phone_number = []
    for char in original_phone_number:
        if char in "0123456789":
            new_phone_number.append(char)
        elif char in "ABC":
            new_phone_number.append("2")
        elif char in "DEF":
            new_phone_number.append("3")
        elif char in "GHI":
            new_phone_number.append("4")
        elif char in "JKL":
            new_phone_number.append("5")
        elif char in "MNO":
            new_phone_number.append("6")
        elif char in "PQRS":
            new_phone_number.append("7")
        elif char in "TUV":
            new_phone_number.append("8")
        elif char in "WXYZ":
            new_phone_number.append("9")
    new_phone_number.insert(3, "-")
    new_phone_number.insert(7, "-")
    final_number = ""
    for i in range(12):
        final_number += new_phone_number[i]
    new_phone_numbers.append(final_number)

for number in new_phone_numbers:
    print(number)