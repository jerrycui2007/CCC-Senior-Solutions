# https://dmoj.ca/problem/ccc04s3
rows = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
grid = {row: input().split() for row in rows}

computed = {}
visiting = {}


def evaluate(cell):
    if cell in computed:
        return computed[cell]

    if cell in visiting:
        # Cycle detected: mark cell as undefined.
        computed[cell] = None
        return None

    visiting[cell] = True

    # Extract row and column for the cell.
    row = cell[0]
    col = int(cell[1:])  # Column number (1-indexed)
    expr = grid[row][col - 1]

    # Try to convert the expression to an integer.
    try:
        value = int(expr)
        computed[cell] = value
        del visiting[cell]
        return value
    except ValueError:
        # Otherwise, the expression is a sum of cell references.
        parts = expr.split('+')
        total = 0
        for part in parts:
            val = evaluate(part)
            if val is None:
                computed[cell] = None
                del visiting[cell]
                return None
            total += val
        computed[cell] = total
        del visiting[cell]
        return total


# Evaluate every cell in the grid.
for r in rows:
    for c in range(1, 10):
        cell = r + str(c)
        if cell not in computed:
            evaluate(cell)

# Print
for r in rows:
    row_output = []
    for c in range(1, 10):
        cell = r + str(c)
        if computed[cell] is None:
            row_output.append("*")
        else:
            row_output.append(str(computed[cell]))
    print(" ".join(row_output))

