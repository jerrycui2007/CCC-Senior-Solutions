# https://dmoj.ca/problem/ccc06s1
mother = input()
father = input()

possible_baby_genes = {char: False for char in "abcdeABCDE"}
for char in "abcde":
    if char.upper() in mother or char.upper() in father:
        possible_baby_genes[char.upper()] = True
    if char.lower() in mother and char.lower() in father:
        possible_baby_genes[char.lower()] = True

babies = int(input())
for _ in range(babies):
    baby_genes = input()
    possible = True

    for gene in baby_genes:
        if not possible_baby_genes.get(gene, False):
            possible = False
            break

    if possible:
        print("Possible baby.")
    else:
        print("Not their baby!")
