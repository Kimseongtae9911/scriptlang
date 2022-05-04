from tkinter import *


def check():
	print("check called")
	for i in range(3):
		ch = matrix[i][0]["text"]
		if ch != ' ' and ch == matrix[i][1]["text"] and ch == matrix[i][2]["text"]:		# 행이 같음
			return ch
			
		ch = matrix[0][i]["text"]
		if ch != ' ' and ch == matrix[1][i]["text"] and ch == matrix[2][i]["text"]:		# 열이 같음
			return ch

	ch = matrix[1][1]["text"]
	if ch != ' ' and ch == matrix[0][0]["text"] and ch == matrix[2][2]["text"]:
		return ch
	if ch != ' ' and ch == matrix[0][2]["text"] and ch == matrix[2][0]["text"]:
		return ch

	for r in range(3):
		for c in range(3):
			if matrix[r][c]["text"] == ' ':
				return ' '

	return '@'


def pressed(row, col):
	global bDone, bXturn
	if not bDone and matrix[row][col]['text'] == ' ':
		matrix[row][col]["image"] = imageX 	if bXturn else imageO
		matrix[row][col]['text'] = 'X' 		if bXturn else 'O'

		bXturn = not bXturn

		ch = check()
		if ch == '@':			# draw
			temp = "비김"
		elif ch != ' ':
			temp = ch + "가 이겼습니다"
			bDone = True
		else:
			temp = "플레이어 X 차례" if bXturn else "플레이어 O 차례"

		explaneLabel['text'] = temp


def refresh():
	global bDone, bXturn
	bXturn = True
	bDone = False
	explaneLabel['text'] = "플레이어 X 차례"
	for r in range(3):
		for c in range(3):
			matrix[r][c]["image"] = imageE
			matrix[r][c]["text"] = " "


window = Tk()
window.title("틱택토")

bXturn = True
bDone = False

frame = Frame(window)
frame.pack()

imageX = PhotoImage(file="x.gif")	
imageO = PhotoImage(file="o.gif")
imageE = PhotoImage(file="empty.gif")

# build map
matrix = []
for r in range(3):
	matrix.append([])
	for c in range(3):
		matrix[r].append(Button(frame, image=imageE, text=" ", 
								 command=lambda row=r, col=c: pressed(row, col)))
		matrix[r][c].grid(row = r, column = c)


explaneLabel = Label(window, text="플레이어 X 차례")
explaneLabel.pack()

Button(window, text="다시시작", command=refresh).pack()

window.mainloop()
