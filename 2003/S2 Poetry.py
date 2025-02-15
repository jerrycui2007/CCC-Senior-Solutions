# https://dmoj.ca/problem/ccc03s2
verses = int(input())

output = []


def last_syllable(string):
    last_word = string.split()[-1]
    contains_vowel = False
    for char in ("A", "E", "I", "O", "U"):
        if char in last_word:
            contains_vowel = True

    if not contains_vowel:
        return last_word
    else:
        letters_reversed = []
        for i in range(len(last_word) - 1, -1, -1):
            if last_word[i] in ("A", "E", "I", "O", "U"):
                letters_reversed.append(last_word[i])
                letters_reversed.reverse()
                syllable = ""
                for char in letters_reversed:
                    syllable += char
                return syllable
            else:
                letters_reversed.append(last_word[i])


for _ in range(verses):
    line1 = last_syllable(input().upper())
    line2 = last_syllable(input().upper())
    line3 = last_syllable(input().upper())
    line4 = last_syllable(input().upper())

    if line1 == line2 == line3 == line4:
        print("perfect")
    elif line1 == line2 and line3 == line4:
        print("even")
    elif line1 == line3 and line2 == line4:
        print("cross")
    elif line1 == line4 and line2 == line3:
        print("shell")
    else:
        print("free")