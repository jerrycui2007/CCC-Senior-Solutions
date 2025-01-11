# https://dmoj.ca/problem/ccc98s4
test_cases = int(input())


def insert_parentheses_left(string, index):
    # Find index to insert the parentheses at
    index -= 2

    if string[index] == ")":
        parentheses_counter = 1
        index -= 1
        while parentheses_counter != 0:
            if string[index] == ")":
                parentheses_counter += 1
            elif string[index] == "(":
                parentheses_counter -= 1
            index -= 1
    else:
        while index >= 0 and string[index] != " ":
            index -= 1

    if index == -1:
        string = "(" + string  # insert at beginning of string
    else:
        string = string[0:index + 1] + "(" + string[index + 1:]

    return string


def insert_parentheses_right(string, index):
    # Find index to insert the parentheses at
    index += 2

    if string[index] == "(":
        parentheses_counter = 1
        index += 1
        while parentheses_counter != 0:
            if string[index] == "(":
                parentheses_counter += 1
            elif string[index] == ")":
                parentheses_counter -= 1
            index += 1
    else:
        while index < len(string) and string[index] != " ":
            index += 1

    if index == len(string):
        string = string + ")"  # insert at end of string
    else:
        string = string[0:index] + ")" + string[index:]

    return string


for i in range(test_cases):
    string = input()

    # Find each X and put brackets around the operation
    index = 0
    while index < len(string):
        while index < len(string) and string[index] != "X":
            index += 1
        if index < len(string):
            string = insert_parentheses_left(string, index)
            string = insert_parentheses_right(string, index + 1)
            index += 2

    # Find each + or - and put brackets around the operation
    index = 0
    while index < len(string):
        while index < len(string) and not (string[index] == "+" or string[index] == "-"):
            index += 1
        if index < len(string):
            string = insert_parentheses_left(string, index)
            string = insert_parentheses_right(string, index + 1)
            index += 2

    print(string[1:len(string) - 1])  # avoid the first and last brackets
    if i != test_cases - 1:  # no newline after last testcase
        print()
