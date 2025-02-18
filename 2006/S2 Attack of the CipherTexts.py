# https://dmoj.ca/problem/ccc06s2
cipher = {char: "." for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ "}
plaintext = input()
ciphertext = input()

remaining_plaintext = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ ")
remaining_ciphertext = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ ")

for i in range(min(len(plaintext), len(ciphertext))):
    cipher[ciphertext[i]] = plaintext[i]

    if plaintext[i] in remaining_plaintext:
        remaining_plaintext.remove(plaintext[i])
    if ciphertext[i] in remaining_ciphertext:
        remaining_ciphertext.remove(ciphertext[i])

if len(remaining_plaintext) == 1 and len(remaining_ciphertext) == 1:
    cipher[remaining_ciphertext.pop()] = remaining_plaintext.pop()

message = input()

for char in message:
    print(cipher[char], end="")
print()