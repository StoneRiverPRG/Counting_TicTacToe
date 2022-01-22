# https://www.codingame.com/multiplayer/bot-programming/counting-tictactoe

# Counting TicTacToe Wood 3 League

import sys
import math

# Get greater count of three in a row!


# game loop
while True:
    # opponent_row: The coordinates of your opponent's last move
    opponent_row, opponent_col = [int(i) for i in input().split()]
    valid_action_count = int(input())  # the number of possible actions for your next move
    for i in range(valid_action_count):
        # row: The coordinates of a possible next move
        row, col = [int(j) for j in input().split()]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # <row> <column>
    print("0 0")
