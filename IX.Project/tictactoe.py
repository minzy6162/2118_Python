import tkinter

from tictactoe_game_engine import TictactoeGameEngine

class Tictactoe:
    def __init__(self):
        self.game_engine = TictactoeGameEngine()


    def play(self):
        print(self.game_engine)#show board
        #무한반복
        while True:
            #input row, col
            row = int(input('row : '))
            col = int(input('col: '))
            #set
            self.game_engine.set(row, col)
            #show board
            print(self.game_engine)
            #check_winner 승패가 결정나면, break
            winner = self.game_engine.check_winner()
            if winner != None:
                break

        #결과 출력
        if winner == 'O':
            print('O 이김')
        elif winner == 'X':
            print('X 이김')
        elif winner == 'd':
            print('무승부')

class TictactoeGUI:
    def __init__(self):
        self.game_engine = TictactoeGameEngine()
        self.init_ui()

    def init_ui(self):
        self.CANVAS_SIZE = 300
        self.root = tkinter.Tk()
        self.root.title('틱 택 토')
        self.root.geometry(str(self.CANVAS_SIZE) + 'x' + str(self.CANVAS_SIZE)) #'300x300'
        self.canvas = tkinter.Canvas(self.root, bg = 'white', width = self.CANVAS_SIZE, height = self.CANVAS_SIZE)
        self.canvas.pack()

        #{'O': PhotoImage객채, 'X': PhotoImage 객체}
        self.images = {}#dict()
        self.images['O'] = tkinter.PhotoImage(file='O.gif')
        self.images['X'] = tkinter.PhotoImage(file='X.gif')

        self.canvas.bind('<Button-1>', self.click_handler)

    def click_handler(self, event):
        x = event.x
        y = event.y

        #클릭 처리 => 말을 놓는다.
        col = x // 100+1
        row = y // 100+1
        self.game_engine.set(row, col)
        #show board
        print(self.game_engine)
        winner = self.game_engine.check_winner()
        #결과 보여주기
        if winner == 'O':
            print('O 이김')
        elif winner == 'X':
            print('X 이김')
        elif winner == 'd':
            print('무승부')
        self.canvas.create_image(x, y, anchor="nw", image=self.images['0'])

    def play(self):
        self.canvas.create_image(0, 0, anchor='nw',  image=self.images['O'])
        self.canvas.create_image(200, 200, anchor='nw',  image=self.images['X'])
        self.root.mainloop()

if __name__ == '__main__':
    #ttt = Tictactoe()
    ttt = TictactoeGUI()
    ttt.play()