# https://dmoj.ca/problem/ccc99s5
# Solution TLE in Python, but would work in C

def solve(digit, letter):
    """
    Recursive solution

    :param digit:  current digit we are testing
    :param letter: which letter we are testing (index)
    """
    if letter == max - 1:  # all the letters have been assigned a value
        values[unique_characters[letter]] = digit

        # invalid state
        if (values[word1[-1]] + values[word2[-1]]) % 10 != values[word3[-1]]:
            return

        word1_index = len(word1) - 1
        word2_index = len(word2) - 1
        word3_index = len(word3) - 1
        carryover = 0

        while word1_index >= 0 or word2_index >= 0 or word3_index >= 0:
            w1 = 0
            w2 = 0
            w3 = 0

            if word1_index >= 0:
                w1 = values[word1[word1_index]]

            if word2_index >= 0:
                w2 = values[word2[word2_index]]

            if word3_index >= 0:
                w3 = values[word3[word3_index]]

            # check if addition matches
            if (((w1 + w2) % 10) + carryover) % 10 != w3:
                return

            # calculate carry over
            carryover = (w1 + w2 + carryover) // 10

            word1_index -= 1
            word2_index -= 1
            word3_index -= 1

        # Still here means it is the correct answer
        result1 = "".join(str(values[ch]) for ch in word1)
        result2 = "".join(str(values[ch]) for ch in word2)
        result3 = "".join(str(values[ch]) for ch in word3)
        print(result1)
        print(result2)
        print(result3)
        print()


    else:
        # Set the digit for the current letter
        values[unique_characters[letter]] = digit
        used_digits[digit] = True  # mark digit as used

        if unique_characters[letter + 1] == word1[0] or unique_characters[letter + 1] == word2[0] or unique_characters[letter + 1] == word3[0]:  # if first letter
            for i in range(1, 10):
                if not used_digits[i]:
                    solve(i, letter + 1)
        else:
            for i in range(10):
                if not used_digits[i]:
                    solve(i, letter + 1)
        used_digits[digit] = False


test_cases = int(input())

for _ in range(test_cases):
    word1 = input()
    word2 = input()
    word3 = input()

    # convert the set into a string
    unique_characters = "".join(sorted(set(word1 + word2 + word3)))

    max = len(unique_characters)
    used_digits = [False for _ in range(10)]

    values = {}

    # first letter cannot be 0
    if (unique_characters[0] == word1[0]) or (unique_characters[0] == word2[0]) or (unique_characters[0] == word3[0]):
        for i in range(1, 10):
            solve(i, 0)
    else:
        for i in range(10):
            solve(i, 0)


