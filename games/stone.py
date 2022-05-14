from tkinter import *


class Cell(Canvas):
	def __init__(self, parent, row, col, width=20, height=20):
		Canvas.__init__(self, parent, width=width, height=height, bg="blue", borderwidth=2)
		self.color = 'white'
		self.row = row
		self.col = col
		self.create_oval(4, 4, 20, 20, fill="white", tags="oval")
		self.bind("<Button-1>", lambda t, r=row, c=col: pressed(r,c))


	def clicked(self):
		if self.color != 'white': return False
			
		self.delete("oval") 
		if turn:
			self.color = 'red'
		else:
			self.color = 'yellow'
		self.create_oval(4, 4, 20, 20, fill=self.color, tags="oval")
		return True


	def refresh(self):
		self.color = 'white'
		self["bg"] = 'blue'
		self.delete("oval") 
		self.create_oval(4, 4, 20, 20, fill="white", tags="oval")


def check():
	for r in range(6):		# 모든 행
		for c in range(4):
			color = cells[r][c].color
			if color != 'white' and color == cells[r][c + 1].color and color == cells[r][c + 2].color and color == cells[r][c + 3].color:
				for i in range(4):
					cells[r][c + i]['bg'] = color
				return color

	for r in range(3):		# 모든 열
		for c in range(7):
			color = cells[r][c].color
			if color != 'white' and color == cells[r + 1][c].color and color == cells[r + 2][c].color and color == cells[r + 3][c].color:
				for i in range(4):
					cells[r + i][c]['bg'] = color
				return color

	for r in range(3):		# 우하단 대각
		for c in range(4):
			color = cells[r][c].color
			if color != 'white' and color == cells[r + 1][c + 1].color and color == cells[r + 2][c + 2].color and color == cells[r + 3][c + 3].color:
				for i in range(4):
					cells[r + i][c + i]['bg'] = color
				return color

	for r in range(3):		# 우상단 대각
		for c in range(3, 7, 1):
			color = cells[r][c].color
			if color != 'white' and color == cells[r + 1][c - 1].color and color == cells[r + 2][c - 2].color and color == cells[r + 3][c - 3].color:
				for i in range(4):
					cells[r + i][c - i]['bg'] = color
				return color

	return 'white'


def pressed(ro, col):
	global done, turn
	print(ro, col)
	if done or cells[ro][col].color != 'white': return
	
	for row in range(5, -1, -1):
		if cells[row][col].color == 'white':
			cells[row][col].clicked()
			turn = not turn

			color = check()

			text = ''
			if color == '@':
				text = '비김'
				done = True
			elif color != 'white':
				text = color + "승리"
				done = True
			else:
				text = '다시시작'
			explaneLabel['text'] = text

			break


def refesh():
	global turn, done

	turn = True
	done = False
	explaneLabel['text'] = "다시시작"
	for r in range(6):
		for c in range(7):
			cells[r][c].refresh()


turn = True
done = False

window = Tk()
window.title("사목게임")
		
frame = Frame(window)
frame.pack()

cells = []
for r in range(6):
	cells.append([])
	for c in range(7):
		cells[r].append(Cell(frame, r, c, 20, 20))
		cells[r][c].grid(row=r, column=c)

explaneLabel = Button(window, text="다시시작", command=refesh)
explaneLabel.pack()

window.mainloop()
