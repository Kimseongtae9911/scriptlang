from tkinter import *

class Cell:
    def __init__(self):
        window = Tk()
        window.title("TicTacTo")

        self.Xturn = True
        self.end = False

        frame = Frame(window)
        frame.pack()

        self.imageX = PhotoImage(file="games/x.gif")
        self.imageO = PhotoImage(file="games/o.gif")
        self.imageE = PhotoImage(file="games/empty.gif")

        self.cells = []
        for r in range(3):
            self.cells.append([])
            for c in range(3):
                self.cells[r].append(Button(frame, image=self.imageE, text=' ', command=lambda row = r, col = c : self.pressed(row, col)))
                self.cells[r][c].grid(row = r, column = c)
        
        self.text = StringVar()
        self.text.set("Player X Turn")
        Label(window, textvariable=self.text).pack()

        Button(window, text="Restart", command=self.refresh).pack()

        window.mainloop()

    def check(self):
        for i in range(3):
            ch = self.cells[i][0]["text"]
            if ch != ' ' and ch == self.cells[i][1]["text"] and ch == self.cells[i][2]["text"]:
                return ch
            
            ch = self.cells[0][i]["text"]
            if ch != ' ' and ch == self.cells[1][i]["text"] and ch == self.cells[2][i]["text"]:
                return ch
            
        ch = self.cells[1][1]["text"]
        if ch != ' ' and ch == self.cells[0][0]["text"] and ch == self.cells[2][2]["text"]:
            return ch
        if ch != ' ' and ch == self.cells[0][2]["text"] and ch == self.cells[2][0]["text"]:
            return ch
        
        for row in range(3):
            for col in range(3):
                if self.cells[row][col]["text"] == ' ':
                    return ' '
        
        return '='

    def pressed(self, row, col):
        if not self.end and self.cells[row][col]["text"] == ' ':
            if self.Xturn:
                self.cells[row][col]["image"] = self.imageX
                self.cells[row][col]["text"] = 'X'
            else:
                self.cells[row][col]["image"] = self.imageO
                self.cells[row][col]["text"] = 'O'
            self.Xturn = not self.Xturn

            ch = self.check()
            if ch == '=':
                self.text.set("Draw")
            elif ch != ' ':
                self.text.set("Player " + ch + " Win")
                self.done = True
            elif self.Xturn:
                self.text.set("Player X Turn")
            else:
                self.text.set("Player O Turn")

    def refresh(self):
        self.Xturn = True
        self.end = False
        self.text.set("Player O Turn")

        for row in range(3):
            for col in range(3):
                self.cells[row][col]["image"] = self.imageE
                self.cells[row][col]["text"] = ' '

if __name__ == '__main__':
    Cell()