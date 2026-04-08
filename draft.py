import random

SIZE = 1000
MAX_STEPS = 1000000


def queen_attack(r1, c1, r2, c2):
    # same column or diagonal
    return (c1 == c2) or (abs(r1 - r2) == abs(c1 - c2))


def count_conflicts(board, row, col):
    conflicts = 0
    for r in range(len(board)):
        if r != row:
            if queen_attack(row, col, r, board[r]):
                conflicts += 1
    return conflicts


def random_init():
    # board[row] = column
    return [random.randint(0, SIZE - 1) for _ in range(SIZE)]


def min_conflicts():
    board = random_init()

    for step in range(MAX_STEPS):
        # Find conflicted queens
        conflicted = []
        for row in range(SIZE):
            if count_conflicts(board, row, board[row]) > 0:
                conflicted.append(row)

        # If no conflicts → solution found
        if not conflicted:
            print(f"Solution found in {step} steps!")
            return board

        # Pick random conflicted queen
        row = random.choice(conflicted)

        # Find best column (min conflicts)
        min_conf = SIZE
        best_cols = []

        for col in range(SIZE):
            conflicts = count_conflicts(board, row, col)

            if conflicts < min_conf:
                min_conf = conflicts
                best_cols = [col]
            elif conflicts == min_conf:
                best_cols.append(col)

        # Move queen to best column (break ties randomly)
        board[row] = random.choice(best_cols)

    print("No solution found within step limit.")
    return None


def print_solution(board):
    if board is None:
        print("No solution.")
        return

    # Print only first 20 rows for readability
    for i in range(min(20, SIZE)):
        print(f"Row {i} -> Column {board[i]}")


# Run
solution = min_conflicts()
print_solution(solution)
