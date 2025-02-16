# https://dmoj.ca/problem/ccc04s1
collections = int(input())


def is_prefix(a, b):
    return b[:len(a)] == a


def is_suffix(a, b):
    return b[len(b) - len(a):] == a


for _ in range(collections):
    words = []
    for _ in range(3):
        words.append(input())

    found = False

    for i in range(3):
        for j in range(3):
            if i != j:
                if is_prefix(words[i], words[j]):
                    found = True
                elif is_suffix(words[i], words[j]):
                    found = True

    if found:
        print("No")
    else:
        print("Yes")
