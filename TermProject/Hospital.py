from tkinter import *
from tkinter import ttk


class MainWindow:
	def __init__(self):
		# 창 기본 설정
		self.width = 500
		self.height = 700
		self.window = Tk()
		self.window.title("Hospital")
		self.window.geometry("" + str(self.width) + "x" + str(self.height))

		frameTitle = Frame(self.window, padx=10, pady=10,)
		frameHospital = Frame(self.window, padx=10, pady=10)
		frameEntry = Frame(self.window, padx=10, pady=10)
		frameResultList = Frame(self.window, padx=10, pady=10)
		frameTitle.pack(side='top', fill='x')
		frameHospital.pack(side='top', fill='x')
		frameEntry.pack(side='top', fill='x')
		frameResultList.pack(side='bottom', fill='both', expand=True)

		# 로고
		self.canvas = Canvas(frameTitle,  bg = "green", width=480, height=40)
		self.canvas.create_text(240, 20, anchor='center', text='로고', fill='black', font=("나눔고딕코딩", 13))
		self.canvas.pack()

		# 병원 카테고리 - 지역
		self.listBoxSIDO = Listbox(frameHospital, selectmode='extended', height=10, width=13)
		self.listBoxSIGUNGU = Listbox(frameHospital, selectmode='extended', height=10, width=13)
		self.listBoxUPMYONDONG = Listbox(frameHospital, selectmode='extended', height=10, width=13)
		self.listBoxSIDO.grid(row=0, column=0, padx=10)
		self.listBoxSIGUNGU.grid(row=0, column=1, padx=10)
		self.listBoxUPMYONDONG.grid(row=0, column=2, padx=10)

		# 병원 카테고리 - 병원 종류
		frameSubs = Frame(frameHospital, padx=10, pady=10)
		frameSubs.grid(row=0, column=3)

		self.buttonEmailSendButton = Button(frameSubs, font=("나눔고딕코딩", 13), text="이메일")
		self.comboBoxHospitalCategory = ttk.Combobox(frameSubs, font=("나눔고딕코딩", 13), width=10)
		self.comboBoxsubject = ttk.Combobox(frameSubs, font=("나눔고딕코딩", 13), width=10)
		self.buttonEmailSendButton.pack(side='top', fill='both', pady=10)
		self.comboBoxHospitalCategory.pack(side='top', fill='both', pady=20)
		self.comboBoxsubject.pack(side='top', fill='both', pady=20)

		# 병원 - 이름
		Label(frameEntry, font=("나눔고딕코딩", 13), text='병원명').pack(side='left')
		self.entryHospitalName = Entry(frameEntry, font=("나눔고딕코딩", 13), width=15)
		self.entryHospitalName.pack(side='left')

		# 병원 - 위치
		frameSubEntry = Frame(frameEntry, padx=10, pady=10)
		frameSubEntry.pack(side='left', fill='x')

		self.entryPosX = Entry(frameSubEntry, font=("나눔고딕코딩", 13), width=15)
		self.entryPosY = Entry(frameSubEntry, font=("나눔고딕코딩", 13), width=15)
		Label(frameSubEntry, font=("나눔고딕코딩", 13), text='x').grid(row=0, column=0, pady=10)
		Label(frameSubEntry, font=("나눔고딕코딩", 13), text='y').grid(row=1, column=0, pady=10)
		self.entryPosX.grid(row=0, column=1)
		self.entryPosY.grid(row=1, column=1)

		# 병원 - 검색 버튼
		self.buttonSearch = Button(frameEntry, font=("나눔고딕코딩", 13), text="검색")
		self.buttonSearch.pack(side='left', fill='both', padx=10)

		# 병원 - 지도 버튼
		self.buttonMap = Button(frameEntry, font=("나눔고딕코딩", 13), text="지도")
		self.buttonMap.pack(side='left', fill='both', padx=10)

		# 결과창
		self.listboxHospital = Listbox(frameResultList, selectmode='extended', width=30)
		self.listboxPharmacy = Listbox(frameResultList, selectmode='extended', width=30)
		self.listboxHospital.pack(side='left', fill='both', padx=10)
		self.listboxPharmacy.pack(side='right', fill='both', padx=10)

	def mainloop(self):
		self.window.mainloop()




hospital = MainWindow()

hospital.mainloop()