# https://dmoj.ca/problem/ccc01s1

hand_string = input()
hand = {"Clubs": [], "Diamonds": [], "Hearts": [], "Spades": []}

for char in hand_string:
    if char == "C":
        current_suit = "Clubs"
    elif char == "D":
        current_suit = "Diamonds"
    elif char == "H":
        current_suit = "Hearts"
    elif char == "S":
        current_suit = "Spades"
    else:
        hand[current_suit].append(char)

clubs = ""
clubs_score = 0
for card in hand["Clubs"]:
    clubs += card + " "
    if card == "A":
        clubs_score += 4
    if card == "K":
        clubs_score += 3
    if card == "Q":
        clubs_score += 2
    if card == "J":
        clubs_score += 1
if len(hand["Clubs"]) == 0:
    clubs_score += 3
elif len(hand["Clubs"]) == 1:
    clubs_score += 2
elif len(hand["Clubs"]) == 2:
    clubs_score += 1

diamonds = ""
diamonds_score = 0
for card in hand["Diamonds"]:
    diamonds += card + " "
    if card == "A":
        diamonds_score += 4
    if card == "K":
        diamonds_score += 3
    if card == "Q":
        diamonds_score += 2
    if card == "J":
        diamonds_score += 1
if len(hand["Diamonds"]) == 0:
    diamonds_score += 3
elif len(hand["Diamonds"]) == 1:
    diamonds_score += 2
elif len(hand["Diamonds"]) == 2:
    diamonds_score += 1

hearts = ""
hearts_score = 0
for card in hand["Hearts"]:
    hearts += card + " "
    if card == "A":
        hearts_score += 4
    if card == "K":
        hearts_score += 3
    if card == "Q":
        hearts_score += 2
    if card == "J":
        hearts_score += 1
if len(hand["Hearts"]) == 0:
    hearts_score += 3
elif len(hand["Hearts"]) == 1:
    hearts_score += 2
elif len(hand["Hearts"]) == 2:
    hearts_score += 1

spades = ""
spades_score = 0
for card in hand["Spades"]:
    spades += card + " "
    if card == "A":
        spades_score += 4
    if card == "K":
        spades_score += 3
    if card == "Q":
        spades_score += 2
    if card == "J":
        spades_score += 1
if len(hand["Spades"]) == 0:
    spades_score += 3
elif len(hand["Spades"]) == 1:
    spades_score += 2
elif len(hand["Spades"]) == 2:
    spades_score += 1

print("Cards Dealt  Points")
print("Clubs " + clubs + "  " + str(clubs_score))
print("Diamonds " + diamonds + "  " + str(diamonds_score))
print("Hearts " + hearts + "  " + str(hearts_score))
print("Spades " + spades + "  " + str(spades_score))
print("Total " + str(clubs_score + diamonds_score + hearts_score + spades_score))
