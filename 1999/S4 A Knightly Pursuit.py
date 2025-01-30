from math import inf

test_cases = int(input())

for _ in range(test_cases):
    rows = int(input())
    columns = int(input())

    # Convert input rows to 0-based index where 0 is the top row
    pawn_row = rows - int(input())
    pawn_column = int(input()) - 1  # Convert to 0-based column

    knight_row = rows - int(input())
    knight_column = int(input()) - 1  # Convert to 0-based column

    # Minimum knight moves
    board = [[inf for _ in range(columns)] for _ in range(rows)]
    board[knight_row][knight_column] = 0

    # BFS queue
    queue = [(knight_row, knight_column)]
    while queue:
        y, x = queue.pop(0)

        # Generate all possible knight moves and update the board
        if y > 0 and x > 1:
            if board[y - 1][x - 2] > board[y][x] + 1:
                board[y - 1][x - 2] = board[y][x] + 1
                queue.append((y - 1, x - 2))
        if y > 1 and x > 0:
            if board[y - 2][x - 1] > board[y][x] + 1:
                board[y - 2][x - 1] = board[y][x] + 1
                queue.append((y - 2, x - 1))
        if y > 0 and x < columns - 2:
            if board[y - 1][x + 2] > board[y][x] + 1:
                board[y - 1][x + 2] = board[y][x] + 1
                queue.append((y - 1, x + 2))
        if y > 1 and x < columns - 1:
            if board[y - 2][x + 1] > board[y][x] + 1:
                board[y - 2][x + 1] = board[y][x] + 1
                queue.append((y - 2, x + 1))
        if y < rows - 1 and x > 1:
            if board[y + 1][x - 2] > board[y][x] + 1:
                board[y + 1][x - 2] = board[y][x] + 1
                queue.append((y + 1, x - 2))
        if y < rows - 2 and x > 0:
            if board[y + 2][x - 1] > board[y][x] + 1:
                board[y + 2][x - 1] = board[y][x] + 1
                queue.append((y + 2, x - 1))
        if y < rows - 1 and x < columns - 2:
            if board[y + 1][x + 2] > board[y][x] + 1:
                board[y + 1][x + 2] = board[y][x] + 1
                queue.append((y + 1, x + 2))
        if y < rows - 2 and x < columns - 1:
            if board[y + 2][x + 1] > board[y][x] + 1:
                board[y + 2][x + 1] = board[y][x] + 1
                queue.append((y + 2, x + 1))

    found_win = None
    found_stalemate = None

    # Check each possible turn for win or stalemate
    for turn in range(pawn_row):
        current_pawn_row = pawn_row - turn
        if current_pawn_row < 0:
            break

        # Check for win
        if board[current_pawn_row][pawn_column] <= turn:
            diff = turn - board[current_pawn_row][pawn_column]
            if diff % 2 == 0:
                found_win = turn
                break

        # Check for stalemate condition
        stalemate_row = current_pawn_row - 1
        if stalemate_row >= 0:
            if board[stalemate_row][pawn_column] <= turn:
                diff = turn - board[stalemate_row][pawn_column]
                if diff % 2 == 0 and found_stalemate is None:
                    found_stalemate = turn

    if found_win is not None:
        print(f"Win in {found_win} knight move(s).")
    elif found_stalemate is not None:
        print(f"Stalemate in {found_stalemate} knight move(s).")
    else:
        print(f"Loss in {pawn_row - 1} knight move(s).")