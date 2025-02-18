# https://dmoj.ca/problem/ccc24s2

def is_alternating(s):
    # Count frequency of each character
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1

    for i in range(len(s)):
        # Get current character's status
        current = 'heavy' if freq[s[i]] > 1 else 'light'
        # If not first character, check against previous
        if i > 0:
            previous = 'heavy' if freq[s[i-1]] > 1 else 'light'
            if current == previous:
                return False
    return True


strings, length = map(int, input().split())

for i in range(strings):
    s = input()

    if is_alternating(s):
        print("T")
    else:
        print("F")
