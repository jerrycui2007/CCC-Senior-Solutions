# https://dmoj.ca/problem/ccc97s3


def simulate_tournament(initial_teams: int) -> list[tuple[int, int, int, int]]:
    """Simulate a double knockout tournament and return state after each round.
    
    Args:
        initial_teams: Number of teams at start of tournament
        
    Returns:
        List of tuples (round, undefeated, one_loss, eliminated) for each round
    """
    states = []
    undefeated = initial_teams
    one_loss = eliminated = round_num = 0
    
    # Record initial state
    states.append((round_num, undefeated, one_loss, eliminated))
    
    # Continue until we have a winner (one team with one loss)
    while not (undefeated == 0 and one_loss == 1):
        round_num += 1
        
        if undefeated == 1 and one_loss == 1:
            # Special case: final match between last two teams
            undefeated = 0
            one_loss = 2
        else:
            # Regular round
            # Half of undefeated teams get their first loss
            undefeated_losers = undefeated // 2
            # Half of one-loss teams get eliminated
            new_eliminations = one_loss // 2
            
            # Update counts
            undefeated -= undefeated_losers
            one_loss = one_loss + undefeated_losers - new_eliminations
            eliminated += new_eliminations
        
        states.append((round_num, undefeated, one_loss, eliminated))
    
    return states


def format_state(round_num: int, undefeated: int, one_loss: int, eliminated: int) -> str:
    """Format the tournament state as a string.
    
    Args:
        round_num: Current round number
        undefeated: Number of undefeated teams
        one_loss: Number of teams with one loss
        eliminated: Number of eliminated teams
        
    Returns:
        Formatted string describing the tournament state
    """
    return (f"Round {round_num}: {undefeated} undefeated, "
            f"{one_loss} one-loss, {eliminated} eliminated")


def main() -> None:
    """Process multiple test cases and simulate each tournament."""
    test_cases = int(input())
    
    for i in range(test_cases):
        initial_teams = int(input())
        states = simulate_tournament(initial_teams)
        
        # Print all states
        for state in states:
            print(format_state(*state))
        
        # Print total number of rounds
        print(f"There are {states[-1][0]} rounds.")
        
        # Print newline between test cases (except for last case)
        if i < test_cases - 1:
            print()


if __name__ == "__main__":
    main()

