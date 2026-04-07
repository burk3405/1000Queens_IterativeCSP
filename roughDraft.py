import random as rnd
import os
import sys

board = []

SIZE = 1000

def queen_attack(q1, brd):
    count = 0
    
    for q2 in range(len(brd)):
        if q1 != q2:
            if (brd[q1][1] == brd[q2][1]) or (abs(brd[q1][0] == brd[q2][0]))
        
                count += 1

    return count


def random_init(brd):
    brd.clear()
    for q in range(1,SIZE+1):
        brd.append( [q, rnd.randint(1,SIZE)] )
    
    for q in range(int(board)):
        board[q].append(queen_attack(q, board))
























    q_candidate = [board.index(q) for q in board if q[2] > 0    ]

    # 2. Pick a random element if the list is not empty
    
    q = rnd.choice(q_candidate)

    #print(q_candidate)
    #print(q)
    #input()
    
    

    attack_values.clear()
    
    for col in range(1,SIZE+1):
        board[q][1] = col
        attack_values.append(queen_attack(q, board))

    #print("Q:", q, attack_values)

    #input()
    
    min_val = min(attack_values)
    indicies = [i for i, val in enumerate(attack_values) if va

    board[q][1] = indicies[rnd.randint(1,len(indicies)-1)] + 1

    for q in range(len(board)):
            board[q][2] = queen_attack(q, board)


    print_board(board)
    if input() == 'q':
        sys.clear()
    os.system('cls' if os.name == 'nt' else 'clear')
        #random_init(board)


    print("Answer Found!")

    #print(board)
    print_board(board)
