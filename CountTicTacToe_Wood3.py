# https://www.codingame.com/multiplayer/bot-programming/counting-tictactoe

# Counting TicTacToe Wood 3 League

# TODO: #1 class化
# TODO: node


import sys
import math

# Get greater count of three in a row!


# game loop
while True:
    # opponent_row: The coordinates of your opponent's last move
    opponent_row, opponent_col = [int(i) for i in input().split()]
    valid_action_count = int(input())  # the number of possible actions for your next move
    valid_actions = []
    for i in range(valid_action_count):
        # row: The coordinates of a possible next move
        row, col = [int(j) for j in input().split()]
        valid_actions.append((row, col))
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # <row> <column>
    print(f"{valid_actions[0][0]} {valid_actions[0][1]}")



"""
# MinMax 疑似コード
function MIN_MAX(position:局面, depth:integer): integer
begin
  if depth=0 then return STATIC_VALUE(position); {読み深さに達した}
  positionを展開→すべての子ノードをchildren[]に。子ノードの数をwに。
  if w=0 then return STATIC_VALUE(position); {終局}

  if positionは自分の局面 then begin
    max := -∞;
    for i:=1 to w do begin
      score = MIN_MAX( children[i], depth-1);
      if(score>max) max := score;
    end;
    return max;
  end else begin{positionは相手の局面}
    min := ∞;
    for i:=1 to w do begin
      score = MIN_MAX( children[i], depth-1);
      if(score<min) min := score;
    end;
    return min;
  end;
end;
"""