# http://dmoj.ca/problem/ccc04s2
yodellers, rounds = map(int, input().split())
scores = [0] * yodellers
worst_ranks = [0] * yodellers

for _ in range(rounds):
    current_round = list(map(int, input().split()))
    for i in range(yodellers):
        scores[i] += current_round[i]

    # Calculate ranks
    ranks = [sum(1 for y in scores if y > x) + 1 for x in scores]

    # Update worst ranks
    for i in range(yodellers):
        if ranks[i] > worst_ranks[i]:
            worst_ranks[i] = ranks[i]

max_score = max(scores)
top_indices = [i for i, score in enumerate(scores) if score == max_score]
top_indices.sort(key=lambda x: x + 1)  # Sort by contestant number (1-based)

for i in top_indices:
    print(f"Yodeller {i + 1} is the TopYodeller: score {scores[i]}, worst rank {worst_ranks[i]}")
