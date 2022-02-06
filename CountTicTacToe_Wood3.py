# https://www.codingame.com/multiplayer/bot-programming/counting-tictactoe

# Counting TicTacToe Wood 3 League
# Get greater count of three in a row!

""" Counting TicTacToe [summary]

Todo:


"""
# TODO: #1 class化
# ToDo: 2ゲーム目入ったときの検出、初期化
# ToDo: inputまとめられる？
# ToDo: 先攻後攻flag

import sys
import math
from enum import Enum, auto

# マスの状態
class BoardState(Enum):
    """BoardState [summary]

    Args:
        Enum ([type]): [description]
    """
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
            num_three = self.Check_Lines(True)
            print(f"Lines = {num_three}",file=sys.stderr)

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

    # TODO: #14 row , colがboard list の範囲内かチェックする
    # (row, col)がBLANKならTrue
    def can_put_hand(self, row, col):
        # row と col がboard list の範囲内か確認
        if not (0 <= row < self.playboard.size) and (0 <= col < self.playboard.size):
            print("row or col is out of list.", file=sys.stderr)
            return False
        return True if self.playboard.board[row][col] == BoardState.BLANK else False

    # TODO #8 : 3lineをカウントする.Player or AI?

    # check three continuous value
    def Check_Lines(self, player=True):
        num_three = 0
        continuous = 0
        hand = BoardState.PLAYER if player else BoardState.AI
        b_size = self.playboard.size

        # check horizen lines
        num_horizen = 0
        for hrzn in self.playboard.board:
            for mark in hrzn:
                if mark == hand:
                    continuous += 1
                    if continuous >= 3:
                        num_horizen += 1
                else:
                    continuous = 0
            continuous = 0

        # check vertical lines
        num_vertical = 0
        continuous = 0
        for i in range(self.playboard.size):
            for vert in self.playboard.board:
                mark = vert[i]
                if mark == hand:
                    continuous += 1
                    if continuous >= 3:
                        num_vertical += 1
                else:
                    continuous = 0
            continuous = 0

        # check diagonal(#1) lines
        num_diagonal1 = 0
        continuous = 0
        for c in range(b_size * 2 - 3):
            for i in range(c + 1):
                if i > (b_size - 1) or (c - i) > (b_size - 1) or (c - i) < 0:
                    continue
                mark = self.playboard.board[0 + i][c - i]
                if mark == hand:
                    continuous += 1
                    if continuous >= 3:
                        num_diagonal1 += 1
                else:
                    continuous = 0
            continuous = 0

        # check diagonal(#2) lines
        num_diagonal2 = 0
        continuous = 0
        for c in range(b_size * 2 - 3):
            for i in range(c + 1):
                if (b_size - 1 - i) < 0 or (c - i) > (b_size - 1) or (c - i) < 0:
                    continue
                mark = self.playboard.board[(b_size - 1) - i][c - i]
                if mark == hand:
                    continuous += 1
                    if continuous >= 3:
                        num_diagonal2 += 1
                else:
                    continuous = 0
            continuous = 0
        num_three = num_horizen + num_vertical + num_diagonal1 + num_diagonal2

        return num_three

    # TODO #16 : チェックステイト機能追加、ゲームリセット機能追加する
    def check_state(self):
        pass

    # TODO : 評価関数
    def evaluate(self, position):
        """evaluate [summary]

        Args:
            position ([type]): [description]

        Returns:
            [type]: [description]
        """

        return 10

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