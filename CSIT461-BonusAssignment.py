# CSIT 461- Intro to AI/Knowledge Engineering
# Shahin Mehdipour Ataee
# SUNY Fredonia
# Spring 2026

# Bonus Assignment- The 1000-Queens Problem
# Aaron Burkett
# 4/8/2026

import random

SIZE = 1000 # <-- Edit to change N size
MAX_STEPS = 1000000
PRINT_LIMIT = 20  # Used to save space in the console

def print_board(board, limit=PRINT_LIMIT):
    print("\n--- Board Preview ---")
    for row in range(min(limit, len(board))):
        line = []
        for col in range(len(board)):
            if board[row] == col:
                line.append('Q')
            else:
                line.append('-')

        # Count number of conflicts
        conflicts = count_conflicts_fast(board, row, board[row])
        print(' '.join(line[:limit]) + (" ..." if len(board) > limit else "") + f" : {conflicts}")
    print()

def initialize_counts(board):
    col_counts = [0] * SIZE
    diag1_counts = [0] * (2 * SIZE)  # r - c offset
    diag2_counts = [0] * (2 * SIZE)  # r + c

    for r in range(SIZE):
        c = board[r]
        col_counts[c] += 1
        diag1_counts[r - c + SIZE] += 1
        diag2_counts[r + c] += 1

    return col_counts, diag1_counts, diag2_counts


def count_conflicts_fast(board, row, col):
    c = col
    return (
        col_counts[c] +
        diag1_counts[row - c + SIZE] +
        diag2_counts[row + c] - 3  # Subtract Self
    )


def move_queen(board, row, new_col):
    old_col = board[row]

    # Remove the old position
    col_counts[old_col] -= 1
    diag1_counts[row - old_col + SIZE] -= 1
    diag2_counts[row + old_col] -= 1

    # Add the new position
    board[row] = new_col
    col_counts[new_col] += 1
    diag1_counts[row - new_col + SIZE] += 1
    diag2_counts[row + new_col] += 1


def min_conflicts():
    global col_counts, diag1_counts, diag2_counts

    # Initial a random board
    board = [random.randint(0, SIZE - 1) for _ in range(SIZE)]
    col_counts, diag1_counts, diag2_counts = initialize_counts(board)

    for step in range(MAX_STEPS):

        # print(f"\nStep {step}")

        conflicted = [
            r for r in range(SIZE)
            if count_conflicts_fast(board, r, board[r]) > 0
        ]

        # print(f"Conflicted count: {len(conflicted)}")

        if not conflicted:
            print(f"\n Solution found in {step} steps!")
            return board

        row = random.choice(conflicted)

        # print(f"Selected row: {row}")

        min_conf = SIZE
        best_cols = []

        for col in range(SIZE):
            conflicts = (
                col_counts[col] +
                diag1_counts[row - col + SIZE] +
                diag2_counts[row + col]
            )

            if conflicts < min_conf:
                min_conf = conflicts
                best_cols = [col]
            elif conflicts == min_conf:
                best_cols.append(col)

        new_col = random.choice(best_cols)
        move_queen(board, row, new_col)

        # if step % 100 == 0:
        #     print_board(board, limit=10)

    print("\n solution found within step limit.")
    return None

print("Iterative CSP Program started:") # Added to provide clarity that the program is indeed running.

solution = min_conflicts()

if solution:
    print_board(solution, limit=20)
else:
    print("No solution to display.")
