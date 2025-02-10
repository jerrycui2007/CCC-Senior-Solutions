# https://dmoj.ca/problem/ccc02s1
pink_cost = int(input())
green_cost = int(input())
red_cost = int(input())
orange_cost = int(input())

money_target = int(input())

possible_combinations = []
minimum_tickets_sold = 999999999999999

for pinks_sold in range(money_target // pink_cost + 1):
    for greens_sold in range((money_target - pinks_sold) // green_cost + 1):
        for reds_sold in range((money_target - pinks_sold - greens_sold) // red_cost + 1):
            for oranges_sold in range((money_target - pinks_sold - greens_sold - reds_sold) // orange_cost + 1):
                if pinks_sold * pink_cost + greens_sold * green_cost + reds_sold * red_cost + oranges_sold * orange_cost == money_target:
                    possible_combinations.append([pinks_sold, greens_sold, reds_sold, oranges_sold])
                    if pinks_sold + greens_sold + reds_sold + oranges_sold < minimum_tickets_sold:
                        minimum_tickets_sold = pinks_sold + greens_sold + reds_sold + oranges_sold

for combination in possible_combinations:
    print("# of PINK is {0} # of GREEN is {1} # of RED is {2} # of ORANGE is {3}".format(combination[0], combination[1], combination[2], combination[3]))

print("Total combinations is {0}.".format(len(possible_combinations)))
print("Minimum number of tickets to print is {0}.".format(minimum_tickets_sold))