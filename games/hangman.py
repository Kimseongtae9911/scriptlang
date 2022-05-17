import math
from tkinter import * # Import tkinter
from random import randint

class Hangman:
	def __init__(self):
		self.draw()
		self.level = 0

	def draw(self):
		# 한꺼번에 지울 요소들을 "hangman" tag로 묶어뒀다가 일괄 삭제.
		canvas.delete("hangman")

		# 인자 : (x1,y1)=topleft, (x2,y2)=bottomright, start=오른쪽이 0도(반시계방향), extent=start부터 몇도까지인지
		#    style='pieslice'|'chord'|'arc'
		canvas.create_arc(20, 200, 100, 240, start = 0, extent = 180, style='chord', tags = "hangman") # Draw the base
		canvas.create_line(60, 200, 60, 20, tags = "hangman")  # Draw the pole
		canvas.create_line(60, 20, 160, 20, tags = "hangman") # Draw the hanger
	
	def drawMore(self):
		radius = 20 # 반지름
		if self.level == 0:
			canvas.create_line(160, 20, 160, 40, tags = "hangman") # Draw the hanger
		elif self.level == 1:
			canvas.create_oval(140, 40, 180, 80, tags = "hangman") # Draw the hanger
		elif self.level == 2:
			x1 = 160 - radius * math.cos(math.radians(45))
			y1 = 60 + radius * math.sin(math.radians(45))
			x2 = 160 - (radius+60) * math.cos(math.radians(45))
			y2 = 60 + (radius+60) * math.sin(math.radians(45))
			canvas.create_line(x1, y1, x2, y2, tags = "hangman")
		elif self.level == 3:
			x1 = 160 + radius * math.cos(math.radians(45))
			y1 = 60 + radius * math.sin(math.radians(45))
			x2 = 160 + (radius+60) * math.cos(math.radians(45))
			y2 = 60 + (radius+60) * math.sin(math.radians(45))
			canvas.create_line(x1, y1, x2, y2, tags = "hangman")
		elif self.level == 4:
			canvas.create_line(160, 80, 160, 140, tags = "hangman")
		elif self.level == 5:
			canvas.create_line(160, 140, 140, 180, tags = "hangman")
		elif self.level == 6:
			canvas.create_line(160, 140, 180, 180, tags = "hangman")

		self.level += 1
		return self.level




		
# Initialize words, get the words from a file
infile = open("hangman.txt", "r")
words = infile.read().split()

def init():
	global bDone, wjdekq, currentStr, ch, worngChars
	hangman.draw()
	hangman.level = 0
	
	wjdekq = words[randint(0, len(words) - 1)]
	currentStr = [ '*' for _ in wjdekq ]
	ch = ''
	worngChars = []
	bDone = False

	canvas.delete('wrong')
	canvas.delete('char')
	canvas.delete('end')
	canvas.delete('guess')
	
	print(wjdekq)
	print(currentStr)
	print(worngChars)

	canvas.create_text(250, 150, text="단어추측\n" + "".join(currentStr), font = ("나눔고딕코딩", 13), fill = "black", anchor='center', tag='guess')



wjdekq = words[randint(0, len(words) - 1)]
currentStr = [ '*' for _ in wjdekq ]
ch = ''
worngChars = []
level = 0
bDone = False


window = Tk() # Create a window
window.title("행맨") # Set a title


def processKeyEvent(event):  
	global ch
	if event.char >= 'a' and event.char <= 'z':
		ch = event.char
		canvas.delete('char')
		canvas.create_text(250, 175, text="입력 : " + ch, font = ("나눔고딕코딩", 13), fill = "black", anchor='center', tag='char')
		pass
	elif event.keycode == 13:
		if bDone:
			init()
			return

		canvas.delete('char')
		guessWord()
		pass
	
def guessWord():
	global wjdekq, bDone
	bHit = False
	for idx, c in enumerate(wjdekq):
		if c == ch:
			bHit = True
			currentStr[idx] = ch
	if not bHit:
		if notHit() >= 7:
			# kill or restart game
			bDone = True
			canvas.create_text(250, 230, text="실패!! 엔터키를 눌러 재시작", font = ("나눔고딕코딩", 15), fill = "black", anchor='center', tag='end')
	else:
		canvas.delete('guess')
		canvas.create_text(250, 150, text="단어추측\n" + "".join(currentStr), font = ("나눔고딕코딩", 13), fill = "black", anchor='center', tag='guess')
		if wjdekq == "".join(currentStr):
			bDone = True
			canvas.create_text(250, 230, text="성공!! 엔터키를 눌러 재시작", font = ("나눔고딕코딩", 15), fill = "black", anchor='center', tag='end')


def notHit():
	global level
	if ch in worngChars:
		return 0
	worngChars.append(ch)
	canvas.delete('wrong')
	canvas.create_text(250, 200, text="틀린단어 : " + "".join(worngChars), font = ("나눔고딕코딩", 13), fill = "black", anchor='center', tag='wrong')
	

	return hangman.drawMore()
	pass


width = 400
height = 280    
# 선, 다각형, 원등을 그리기 위한 캔버스를 생성
canvas = Canvas(window, bg = "white", width = width, height = height)
canvas.pack()

hangman = Hangman()

# Bind with <Key> event
canvas.bind("<Key>", processKeyEvent)
# key 입력 받기 위해 canvas가 focus 가지도록 함.
canvas.focus_set()

init()

window.mainloop() # Create an event loop
