# https://dmoj.ca/problem/ccc98s1
test_cases = int(input())

for _ in range(test_cases):
    words = input().split()
    censored_words = ""

    for word in words:
        if len(word) == 4:
            censored_words += "**** "
        else:
            censored_words += word + " "

    print(censored_words[:-1])  # skip last character
