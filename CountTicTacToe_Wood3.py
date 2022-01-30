# https://www.codingame.com/multiplayer/bot-programming/counting-tictactoe

# Counting TicTacToe Wood 3 League
# Get greater count of three in a row!

# TODO: #1 class化
# ToDo: 2ゲーム目入ったときの検出、初期化
# ToDo: inputまとめられる？
# ToDo: 先攻後攻flag

import sys
import math
from enum import Enum, auto

# マスの状態
class BoardState(Enum):
    BLANK = auto()
    PLAYER = auto()
    AI = auto()

# ゲームの状態
class GameState(Enum):
    GAME = auto()
    PLAYER_WIN = 'PLAYER_WIN'
    AI_WIN = 'AI_WIN'
    FULL = 'FULL'

class Board():

    def __init__(self):
        # ボードの初期化
        self.size = 10
        self.board = [[BoardState.BLANK for _ in range(self.size)] for _ in range(self.size)]

    # 盤面の表示 OX
    def print_Board(self):
        for row in self.board:
            tmp_str = ""
            for col in row:
                if col == BoardState.BLANK:
                    tmp_str += " "
                elif col == BoardState.PLAYER:
                    tmp_str += "O"
                elif col == BoardState.AI:
                    tmp_str += "X"
            print(tmp_str, file=sys.stderr)
        print("", file=sys.stderr)



class TicTacToe():

    def __init__(self):
        self.playboard = Board()
        # 先攻後攻
        self.my_turn = False
        # ゲーム開始
        self.state = GameState.GAME

    def main(self):
        # game loop
        while True:
            # 情報Input

            # TODO: #11 AI Input関数化する
            # AI Input
            # opponent_row: The coordinates of your opponent's last move
            self.opponent_row, self.opponent_col = [int(i) for i in input().split()]

            # TODO: #12 Player Input候補リスト化する関数つくる
            # 指せる手の候補Input
            self.valid_action_count = int(input())  # the number of possible actions for your next move
            self.valid_actions = []
            for _ in range(self.valid_action_count):
                # row: The coordinates of a possible next move
                row, col = [int(j) for j in input().split()]
                self.valid_actions.append((row, col))

            # Action部分
            # 先攻後攻初期化
            if (self.opponent_row, self.opponent_col) == (-1, -1):
                self.my_turn = True
            else:
                self.put_hand(False, self.opponent_row, self.opponent_col)


            print(self.valid_actions[0][0], self.valid_actions[0][1])
            # Player put_hand
            self.put_hand(True, self.valid_actions[0][0], self.valid_actions[0][1])

            # 盤面表示
            self.display_board()

        """
        while self.state == GameState.GAME:
            if self.my_turn:
                # 先攻
                self.player_input()
            else:
                # 後攻
                self.player_input()
            self.display_board()
        print(self.state)
        """


    #TODO: #2 ボードを表示する
    def display_board(self):
        # クラスBoard内のprint関数でboard表示
        self.playboard.print_Board()

    # TODO: #5 ○ or ×をrow, col に置く.
    # TODO: #6 Player or AIでO X 変える.
    def put_hand(self, player, row, col):
        if player == True:
            hand = BoardState.PLAYER
        else:
            hand = BoardState.AI
        if not self.can_put_hand(row, col):
            print(f"Error can_put_hand {row}, {col}", file=sys.stderr)
            return

        # TODO #7:boardに値を更新
        self.playboard.board[row][col] = hand

    # row, colがBLANKならTrue
    def can_put_hand(self, row, col):
        return True if self.playboard.board[row][col] == BoardState.BLANK else False

    # TODO #8 : 3lineをカウントする.Player or AI?
    def Check_Lines(self, player=True):
        pass

    def check_state(self):
        pass

    # プレイヤーの入力
    def player_input(self):
        while True:
            try:
                value = int(input('please input value'))
                if self.can_put_value(value):
                    self.put_value(value)
                    break
                else:
                    print('do not put')
            except:
                print('attribute error')

    # ターンを交代する
    def change_turn(self):
        self.my_turn = not(self.my_turn)

    # valueに置く
    def put_value(self, value):
        self.board[value] = BoardState.PLAYER if self.my_turn else BoardState.AI
        self.check_state()
        self.change_turn()

    # 勝敗がついているならTrue
    def judge(self, a, b, c):
          return True if a == b == c and a != BoardState.BLANK else False

    # ゲームの状態を更新
    def check_state(self):
        for i in range(3):
            if self.judge(*self.board[i:9:3]) or self.judge(*self.board[3*i:3*i+3]) or self.judge(*self.board[0:9:4]) or self.judge(*self.board[2:7:2]):
                if self.my_turn:
                    self.state = GameState.PLAYER_WIN
                    return
                else:
                    self.state = GameState.AI_WIN
                    return

        if all(BoardState.BLANK != state for state in self.board):
            self.state = GameState.FULL
            return

        self.state = GameState.GAME


tictactoe = TicTacToe()
tictactoe.main()



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