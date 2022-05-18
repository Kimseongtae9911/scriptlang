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
		self.SIDO = ''
		self.SIGUNGU = ''
		self.UPMYONDONG = ''
		self.listBoxSIDO = Listbox(frameHospital, selectmode='extended', height=10, width=13)
		self.listBoxSIGUNGU = Listbox(frameHospital, selectmode='extended', height=10, width=13)
		self.listBoxUPMYONDONG = Listbox(frameHospital, selectmode='extended', height=10, width=13)
		self.listBoxSIDO.bind('<<ListboxSelect>>', self.SIDOSelect)
		self.listBoxSIGUNGU.bind('<<ListboxSelect>>', self.SIGUNGUSelect)
		self.listBoxUPMYONDONG.bind('<<ListboxSelect>>', self.UPMYONDONGSelect)
		self.listBoxSIDO.grid(row=0, column=0, padx=10)
		self.listBoxSIGUNGU.grid(row=0, column=1, padx=10)
		self.listBoxUPMYONDONG.grid(row=0, column=2, padx=10)

		# 병원 카테고리 - 병원 종류
		frameSubs = Frame(frameHospital, padx=10, pady=10)
		frameSubs.grid(row=0, column=3)

		self.buttonEmailSendButton = Button(frameSubs, font=("나눔고딕코딩", 13), text="이메일", command=self.pressedEmail)
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
		self.buttonSearch = Button(frameEntry, font=("나눔고딕코딩", 13), text="검색", command=self.pressedSearch)
		self.buttonSearch.pack(side='left', fill='both', padx=10)

		# 병원 - 지도 버튼
		self.buttonMap = Button(frameEntry, font=("나눔고딕코딩", 13), text="지도", command=self.pressedMap)
		self.buttonMap.pack(side='left', fill='both', padx=10)

		# 결과창
		self.listboxHospital = Listbox(frameResultList, selectmode='extended', width=30)
		self.listboxPharmacy = Listbox(frameResultList, selectmode='extended', width=30)
		self.listboxHospital.pack(side='left', fill='both', padx=10)
		self.listboxPharmacy.pack(side='right', fill='both', padx=10)

	def mainloop(self):
		self.window.mainloop()

	def pressedEmail(self):
		import Email
		print("email")
		pass
	
	def pressedSearch(self):
		if not self.UPMYONDONG:
			print("error!!!")
			return
		
		print("search :", self.SIDO, self.SIGUNGU, self.UPMYONDONG)
		# 병원을 검색하고 리스트에 붙여넣는다
		

	def pressedMap(self):
		print("map")
		pass

	def SIDOSelect(self, event):
		# 시군구, 읍면동 리스트박스 비우기

		# 시군구 리스트박스 갱신

		# 검색 변수 갱신
		if event.widget.curselection():
			self.SIDO = self.listBoxSIDO.selection_get()
			self.SIGUNGU = ''
			self.UPMYONDONG = ''
		pass

	def SIGUNGUSelect(self, event):
		# 읍면동 리스트박스 비우기

		# 읍면동 리스트박스 갱신

		# 검색 변수 갱신
		if event.widget.curselection():
			self.SIGUNGU = self.listBoxSIGUNGU.selection_get()
			self.UPMYONDONG = ''
		pass

	def UPMYONDONGSelect(self, event):
		# 검색 변수 갱신
		if event.widget.curselection():
			self.UPMYONDONG = self.listBoxUPMYONDONG.selection_get()
		pass

	def testSetting(self):
		self.listBoxSIDO.insert(END, "서울시")
		self.listBoxSIDO.insert(END, "인천시")
		self.listBoxSIDO.insert(END, "경기도")

		self.listBoxSIGUNGU.insert(END, "시흥시")
		self.listBoxSIGUNGU.insert(END, "asdf")
		self.listBoxSIGUNGU.insert(END, "zxcv")

		self.listBoxUPMYONDONG.insert(END, "정왕동")
		self.listBoxUPMYONDONG.insert(END, "456")
		self.listBoxUPMYONDONG.insert(END, "789")
		pass


if __name__ == '__main__':
	hospital = MainWindow()
	hospital.testSetting()
	hospital.mainloop()


