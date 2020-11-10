class TictactoeGameEngine:
    def __init__(self):
        self.board = list('.' * 9)
        self.current_turn = 'X'

    def get(self, row, col):
        row -= 1
        col -= 1
        return self.board[row * 3 + col]

    def set(self, row, col):
        if self.get(row, col) != '.':
            return

        row -= 1
        col -= 1
        self.board[row * 3 + col] = self.current_turn #현재 놓는 판의 위치
        self.current_turn = 'O' if self.current_turn == 'X' else 'X' #말을 바꾸는 코드

    def check_winner(self): #누가 이겼는지 확인
        #-(가로)
        for i in range(1, 3+1):
            if self.get(i, 1) == self.get(i, 2) == self.get(i, 3) != '.':
                return self.get(i, 1)
        #|(세로)
        for i in range(1, 4):
            if self.get(1, i) == self.get(2, i) == self.get(3, i) != '.':
                return  self.get(1, i)
        #\(왼쪽에서 오른쪽으로 대각선)
        if self.get(1, 1) == self.get(2, 2) == self.get(3, 3) != '.':
            return  self.get(2, 2)
        #/(오른쪽에서 왼쪽으로 대각선)
        if self.get(1, 3) == self.get(2, 2) == self.get(3, 1) != '.':
            return  self.get(2, 2)
        if not '.' in self.board:
            return 'd'  #무승부는 d 리턴 draw: 무승부

    def __str__(self):
        s = ''
        for i, v in enumerate(self.board):#보여지는 
            s += v
            if i % 3 == 2:
                s += '\n'
        return s


if __name__ == '__main__':
    ttt_game_engine = TictactoeGameEngine()
    print(ttt_game_engine)
    print(ttt_game_engine.check_winner())
    ttt_game_engine.set(1, 1)
    print(ttt_game_engine)
    print(ttt_game_engine.check_winner())
    ttt_game_engine.set(2, 1)
    print(ttt_game_engine)
    print(ttt_game_engine.check_winner())
    ttt_game_engine.set(2, 2)
    print(ttt_game_engine)
    print(ttt_game_engine.check_winner())
    ttt_game_engine.set(3, 1)
    print(ttt_game_engine)
    print(ttt_game_engine.check_winner())
    ttt_game_engine.set(3, 3)
    print(ttt_game_engine)
    print(ttt_game_engine.check_winner())