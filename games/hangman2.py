import math
import random
from tkinter import * # Import tkinter

finish = 0
nCorrectChar = 0
nMissedLetters = 0

class Hangman:
    def __init__(self):
        infile = open("games/hangman.txt", "r")
        self.words = infile.read().split()
        self.guessWord = self.words[random.randint(0, len(self.words) - 1)]
        self.hiddenWord = ['*' for _ in range(len(self.guessWord))]
        self.missedWord = []
        infile.close()
        self.draw()

    def guess(self, letter):
        global nMissedLetters, nCorrectChar, finish

        if letter in self.missedWord:
            return
        elif letter in self.hiddenWord:
            return
        elif letter in self.guessWord:
            for i in range(len(self.guessWord)):
                if self.guessWord[i] == letter:
                    self.hiddenWord[i] = letter
                    nCorrectChar += 1
                    if nCorrectChar == len(self.guessWord):
                        finish = 1
        else:
            self.missedWord.append(letter)
            nMissedLetters += 1
            if nMissedLetters == 7:
                finish = 2

        self.draw()
        
    def reset(self):
        global finish, nMissedLetters, nCorrectChar
        self.missedWord.clear()
        self.hiddenWord.clear()
        self.guessWord = self.words[random.randint(0, len(self.words) - 1)]
        self.hiddenWord = ['*' for _ in range(len(self.guessWord))]
        finish = 0
        nMissedLetters = 0
        nCorrectChar = 0
        self.draw()

    def draw(self):
        canvas.delete("hangman")

        if finish == 0:     # 추측
            canvas.create_text(200, 190, text = '단어 추측: ' + ''.join(self.hiddenWord), tags = 'hangman')
            if nMissedLetters > 0:
                canvas.create_text(200, 210, text = '틀린 글자: ' + ''.join(self.missedWord), tags = 'hangman')
        elif finish == 1:   # 정답
            canvas.create_text(200, 190, text = self.guessWord + ' 맞았습니다', tags = 'hangman')
            canvas.create_text(200, 210, text = '게임을 계속하려면 ENTER를 누르세요', tags = 'hangman')
        else:               # 오답
            canvas.create_text(200, 190, text = '정답: ' + self.guessWord, tags = 'hangman')
            canvas.create_text(200, 210, text = '게임을 계속하려면 ENTER를 누르세요', tags = 'hangman')

        # 인자 : (x1,y1)=topleft, (x2,y2)=bottomright, start=오른쪽이 0도(반시계방향), extent=start부터 몇도까지인지
        #    style='pieslice'|'chord'|'arc'
        canvas.create_arc(20, 200, 100, 240, start = 0, extent = 180, style='chord', tags = "hangman") # Draw the base
        canvas.create_line(60, 200, 60, 20, tags = "hangman")  # Draw the pole
        canvas.create_line(60, 20, 160, 20, tags = "hangman") # Draw the hanger
        
        radius = 20 # 반지름
        if nMissedLetters > 0:
            canvas.create_line(160, 20, 160, 40, tags = "hangman") # Draw the hanger

        # Draw the circle
        if nMissedLetters > 1:
            canvas.create_oval(140, 40, 180, 80, tags = "hangman") # Draw the hanger

        if nMissedLetters > 2:
            canvas.create_line(160, 80, 160, 140, tags = "hangman") # Draw the hanger

        # Draw the left arm (중심(160,60)에서 45도 움직인 지점의 x좌표는 cos로, y좌표는 sin으로 얻기)
        x1 = 160 - radius * math.cos(math.radians(45))
        y1 = 60 + radius * math.sin(math.radians(45))
        x2 = 160 - (radius+60) * math.cos(math.radians(45))
        y2 = 60 + (radius+60) * math.sin(math.radians(45))

        if nMissedLetters > 3:
            canvas.create_line(x1, y1, x2, y2, tags = "hangman")

        x3 = 160 + radius * math.cos(math.radians(-45))
        y3 = 60 - radius * math.sin(math.radians(-45))
        x4 = 160 + (radius+60) * math.cos(math.radians(-45))
        y4 = 60 - (radius+60) * math.sin(math.radians(-45))
        if nMissedLetters > 4:
            canvas.create_line(x3, y3, x4, y4, tags = "hangman")
        
        x2 = 160 - (radius+40) * math.cos(math.radians(45))
        y2 = 140 + (radius+40) * math.sin(math.radians(45))

        if nMissedLetters > 5:
            canvas.create_line(160, 140, x2, y2, tags = "hangman")

        x4 = 160 + (radius+40) * math.cos(math.radians(-45))
        y4 = 140 - (radius+40) * math.sin(math.radians(-45))

        if nMissedLetters > 6:
            canvas.create_line(160, 140, x4, y4, tags = "hangman")


window = Tk() # Create a window
window.title("행맨") # Set a title

def processKeyEvent(event):  
    global hangman, nMissedLetters
    if event.char >= 'a' and event.char <= 'z':
        if nMissedLetters < 7:
            hangman.guess(event.char)
    elif event.keycode == 13:
        if finish == 1 or finish == 2:
            hangman.reset()

canvas = Canvas(window, bg = "white", width = 400, height = 280)
canvas.pack()

hangman = Hangman()

canvas.bind("<Key>", processKeyEvent)
canvas.focus_set()

window.mainloop() # Create an event loop
