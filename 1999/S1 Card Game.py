# https://dmoj.ca/problem/ccc99s1
# cards = [input() for _ in range(52)]

a_points = 0
b_points = 0

high_cards = {"jack": 1, "queen": 2, "king": 3, "ace": 4}


def will_score(index, cards_to_check):
    if index + cards_to_check > 51:
        return False

    for i in range(index + 1, index + cards_to_check + 1):
        if cards[i] in high_cards:
            return False

    return True


for i in range(52):
    if cards[i] in high_cards and will_score(i, high_cards[cards[i]]):
        score = high_cards[cards[i]]

        if i % 2 == 0:  # Player A's turn
            a_points += score
            print(f"Player A scores {score} point(s).")
        else:  # Player B's turn
            b_points += score
            print(f"Player B scores {score} point(s).")

print(f"Player A: {a_points} point(s).")
print(f"Player B: {b_points} point(s).")