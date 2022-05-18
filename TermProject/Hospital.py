from tkinter import *

class MainWindow:
	def __init__(self):
		# 창 기본 설정
		self.width = 500
		self.height = 700
		self.window = Tk()
		self.window.title("Hospital")
		self.window.geometry("" + str(self.width) + "x" + str(self.height))

		frameTitle = Frame(self.window, padx=10, pady=10, bg='#ff0000')
		frameTitle.pack(side='top', fill='x')
		frameLists = Frame(self.window, padx=10, pady=10, bg='#00ff00')
		frameLists.pack(side='top', fill='x')
		frameEntry = Frame(self.window, padx=10, pady=10, bg='#0000ff')
		frameEntry.pack(side='top', fill='x')
		frameList = Frame(self.window, padx=10, pady=10, bg='#ffff00')
		frameList.pack(side='bottom', fill='both', expand=True)

		# 로고
		self.canvas = Canvas(frameTitle,  bg = "green", width = 480, height = 40)
		self.canvas.create_text(240, 20, anchor='center', text='로고', fill='black', font=("나눔고딕코딩", 13))
		self.canvas.pack()

		# 리스트박스
		self.listBoxSIDO = Listbox(frameLists, selectmode='extended', height=10)
		self.listBoxSIDO.pack(side='left', expand=True, padx=10, fill='y')
		self.listBoxSIGUNGU = Listbox(frameLists, selectmode='extended', height=10)
		self.listBoxSIGUNGU.pack(side='right', expand=True, padx=10, fill='y')
		self.listBoxUPMYONDONG = Listbox(frameLists, selectmode='extended', height=10)
		self.listBoxUPMYONDONG.pack(side='right', expand=True, padx=10, fill='y')

		sendEmail = Button(frameLists, font=("나눔고딕코딩", 13) ,text='이메일')
		sendEmail.pack(side='right', padx=10, fill='y')
		sendEmail = Button(frameLists, font=("나눔고딕코딩", 13) ,text='이메일')
		sendEmail.pack(side='right', padx=10, fill='y')

	def mainloop(self):
		self.window.mainloop()




hospital = MainWindow()

hospital.mainloop()