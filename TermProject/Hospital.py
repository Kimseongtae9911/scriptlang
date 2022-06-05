from cmath import exp
import Server as server
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from locationDict import *
from InfoClass import *
import folium
import webbrowser
import Graph


hospital_pw = "5wsKqI6xrBpV5YTufFeyzDKJeU+SGnMJpBz87SPB4sfds/wcAwRU3K1d72Ph5mSLJL+VwfIqeffp4WvfklvOpg=="
pharmacy_pw = "5wsKqI6xrBpV5YTufFeyzDKJeU+SGnMJpBz87SPB4sfds/wcAwRU3K1d72Ph5mSLJL+VwfIqeffp4WvfklvOpg=="

hospital_url = 'http://apis.data.go.kr/B551182/hospInfoService1/getHospBasisList1'
pharmacy_url = 'http://apis.data.go.kr/B551182/pharmacyInfoService/getParmacyBasisList'


class MainWindow:
	def __init__(self):
		# 창 기본 설정
		self.width = 500
		self.height = 700
		server.window.title("Hospital")
		server.window.geometry("" + str(self.width) + "x" + str(self.height))

		frameTitle = Frame(server.window, padx=10, pady=10,)
		frameHospital = Frame(server.window, padx=10, pady=10)
		frameEntry = Frame(server.window, padx=10)
		frameResultList = Frame(server.window, padx=10, pady=10)
		frameExtraButtons = Frame(server.window, padx=10, pady=10)
		frameTitle.pack(side='top', fill='x')
		frameHospital.pack(side='top', fill='x')
		frameEntry.pack(side='top', fill='x')
		frameExtraButtons.pack(side='bottom', fill='both', )
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

		self.comboBoxHospitalCategory = ttk.Combobox(frameSubs, font=("나눔고딕코딩", 13), width=10, values=list(CLCD.keys()))
		self.comboBoxsubject = ttk.Combobox(frameSubs, font=("나눔고딕코딩", 13), width=10, values=list(DGSBJTCD.keys()))
		self.comboBoxHospitalCategory.pack(side='top', fill='both', pady=20)
		self.comboBoxsubject.pack(side='top', fill='both', pady=20)
		self.comboBoxHospitalCategory.current(0)
		self.comboBoxsubject.current(0)

		# 병원 - 이름
		frameNameSearch = Frame(frameEntry, padx=65, pady=10)
		frameNameSearch.pack(side='left')
		self.entryHospitalName = Entry(frameNameSearch, font=("나눔고딕코딩", 13), width=15)
		self.entryHospitalName.insert(0, "병원 명 입력")
		self.entryHospitalName.bind('<Button-1>', self.EntryClick)
		self.entryHospitalName.pack(anchor='center')


		# 병원 - 위치
		#frameSubEntry = Frame(frameEntry, padx=10, pady=10)
		#frameSubEntry.pack(side='left', fill='x')

		#self.entryPosX = Entry(frameSubEntry, font=("나눔고딕코딩", 13), width=15)
		#self.entryPosY = Entry(frameSubEntry, font=("나눔고딕코딩", 13), width=15)
		#Label(frameSubEntry, font=("나눔고딕코딩", 13), text='x').grid(row=0, column=0, pady=10)
		#Label(frameSubEntry, font=("나눔고딕코딩", 13), text='y').grid(row=1, column=0, pady=10)
		#self.entryPosX.grid(row=0, column=1)
		#self.entryPosY.grid(row=1, column=1)

		# 병원 - 검색 버튼
		frameSearch = Frame(frameEntry, padx=10, pady=10, width=250)
		frameSearch.pack()
		self.buttonSearch = Button(frameSearch, font=("나눔고딕코딩", 13), text="검색", width=6, height=2, command=self.pressedSearch)
		self.buttonSearch.pack()

		# 병원 - 지도 버튼


		# 결과창
		self.listboxHospital = Listbox(frameResultList, selectmode='extended', width=30)
		self.listboxHospital.bind('<<ListboxSelect>>', self.hospitalSelect)
		self.listboxPharmacy = Listbox(frameResultList, selectmode='extended', width=30)
		self.listboxPharmacy.bind('<<ListboxSelect>>', self.pharmacySelect)
		self.listboxHospital.pack(side='left', fill='both', padx=10)
		self.listboxPharmacy.pack(side='right', fill='both', padx=10)

		# 버튼들
		frameLeftRight = Frame(frameExtraButtons)
		frameEmailMap = Frame(frameExtraButtons)
		frameLeftRight.pack(side='left', expand=True)
		frameEmailMap.pack(side='right', expand=True)
		px = 25

		self.leftImage = PhotoImage(file='TermProject/Resource/Left.png')
		self.rightImage = PhotoImage(file='TermProject/Resource/Right.png')
		self.emailPhoto = PhotoImage(file='TermProject/Resource/Email.png')
		self.mapphoto = PhotoImage(file='TermProject/Resource/Map.png')

		# 좌우 버튼
		self.buttonGoPerv = Button(frameLeftRight, image=self.leftImage, command=self.pressedPrev)
		self.buttonGoNext = Button(frameLeftRight, image=self.rightImage, command=self.pressedNext)
		self.buttonGoPerv.pack(side='left', padx=px)
		self.buttonGoNext.pack(side='right', padx=px)
		self.page = 1

		# 이메일, 지도 버튼
		self.buttonEmailSendButton = Button(frameEmailMap, image=self.emailPhoto, command=self.pressedEmail)
		self.buttonMap = Button(frameEmailMap, image=self.mapphoto, command=self.pressedMap)
		self.buttonEmailSendButton.pack(side='left', padx=px)
		self.buttonMap.pack(side='right', padx=px)


		self.hospitalList = []
		self.pharmacyList = []

		self.lastSelectHospitalIdx = -1
		self.lastPage = False

		for data in SIDO:
			if data != '':
				self.listBoxSIDO.insert(END, data)

	def mainloop(self):
		server.window.mainloop()

	def EntryClick(self, event):
		self.entryHospitalName.delete(0, END)

# prev
	def pressedPrev(self):
		if self.listboxHospital.size():
			# 재검색
			self.lastSelectHospitalIdx -= 1
			if self.lastSelectHospitalIdx <= 0:
				self.lastSelectHospitalIdx = 1
			self.hospitalSearch()

# next
	def pressedNext(self):
		if self.listboxHospital.size() and not self.lastPage:
			self.lastSelectHospitalIdx += 1
			self.hospitalSearch()

# 이메일 버튼
	def pressedEmail(self):
		from Email import Mail

		# 검색하지 않고 이메일 버튼 누를 경우 예외처리
		if self.hospitalList == []:
			tkinter.messagebox.showinfo('오류', '검색을 먼저 해주세요')
			return
		
		if server.puwindow == None:
			if self.lastSelectHospitalIdx >= 0:
				Mail.popupInput(self.hospitalList[self.lastSelectHospitalIdx], self.pharmacyList)
			else:
				Mail.popupInput(self.hospitalList, self.pharmacyList)
	

# 검색 버튼
	def pressedSearch(self):
		self.lastSelectHospitalIdx = 1
		self.hospitalSearch()
		
# 진짜 검색
	def hospitalSearch(self):
		self.listboxHospital.delete(0, END)
		self.listboxPharmacy.delete(0, END)
		if not self.UPMYONDONG:
			# print("error!!!")
			pass

		self.lastPage = False
		
		# 병원을 검색한다
		response = search(url=hospital_url, key=hospital_pw, sidoCd=str(SIDO[self.SIDO] * 10000),
			sgguCd=str(SIGUNGU[self.SIGUNGU]), emdongNm=self.UPMYONDONG, yadmNm=self.entryHospitalName.get(), 
			clCd=CLCD[self.comboBoxHospitalCategory.get()], dgsbjtCd=DGSBJTCD[self.comboBoxsubject.get()], page=str(self.lastSelectHospitalIdx))

		self.hospitalList.clear()

		# 리스트에 붙여넣는다
		from xml.etree import ElementTree
		HospitalTree = ElementTree.fromstring(response.content)
		hospitalElememt = HospitalTree.iter("item")
		cnt = 1
		for item in hospitalElememt:
			strTitle = item.find("yadmNm")
			self.listboxHospital.insert(END, "[{:}]: ".format(cnt) + strTitle.text)
			cnt += 1
			hospital = Hospital()
			hospital.getInfo(item)
			self.hospitalList.append(hospital)		
		
		# 비어있다면
		if not self.listboxHospital.size():
			self.listboxHospital.insert(END, "마지막 입니다.")
			self.lastPage = True

		# 그래프 출력 + 예외처리
		if self.comboBoxsubject.get() == '선택안함' and self.comboBoxHospitalCategory.get() == '선택안함' and self.hospitalList != []:
			Graph.Graph(self.hospitalList)	

# 지도 버튼 
	def pressedMap(self):
		# 지도에 병원 표시
		# 선택한 것이 있다면 선택한 병원과 약국만 표시
		# 없다면 리스트의 모든 병원 표시

		i = 0

		# 병원을 선택안했을 때
		if self.listboxHospital.curselection() == ():
			for hospital in self.hospitalList:
				name = hospital.yadmNm
				posy, posx = hospital.pos
				# 좌표없는 병원들 예외처리
				if posx == -1 or posy == -1:
					continue

				if i == 0:
					self.map_osm = folium.Map(location=[posx, posy], zoom_start=13)
					i += 1
				
				icon = 'plus'
				folium.Marker([posx, posy], popup=name, icon=folium.Icon(icon=icon)).add_to(self.map_osm)
		
		# 병원을 선택했을때
		else:
			if self.lastSelectHospitalIdx >= 0:
				name = self.hospitalList[self.lastSelectHospitalIdx].yadmNm
				posy, posx = self.hospitalList[self.lastSelectHospitalIdx].pos
				color = 'red'
				icon = 'plus'
				self.map_osm = folium.Map(location=[posx, posy], zoom_start=20)
				folium.Marker([posx, posy], popup=name, icon=folium.Icon(color=color, icon=icon)).add_to(self.map_osm)
				
			# 지도에 약국 표시
			for pharmacy in self.pharmacyList:
				name = pharmacy.yadmNm
				posy, posx = pharmacy.pos
				if posx == -1 or posy == -1:	# 좌표없는 약국들 예외처리
					continue
				else:
					icon = 'flag'
					folium.Marker([posx, posy], popup=name, icon=folium.Icon(icon=icon)).add_to(self.map_osm)

		self.map_osm.save('osm.html')
		webbrowser.open_new('osm.html')


# 시도 선택
	def SIDOSelect(self, event):
		# 검색 변수 갱신
		if event.widget.curselection():
			self.SIDO = self.listBoxSIDO.selection_get()
			self.SIGUNGU = ''
			self.UPMYONDONG = ''

		# 시군구, 읍면동 리스트박스 비우기
		self.listBoxSIGUNGU.delete(0, END)
		self.listBoxUPMYONDONG.delete(0, END)
		
		# 시군구 리스트박스 갱신
		for data in SIGUNGU:
			if SIDO[self.SIDO] != '' and SIDO[self.SIDO] == SIGUNGU[data] // 10000:
				self.listBoxSIGUNGU.insert(END, data)


# 시군구 선택
	def SIGUNGUSelect(self, event):
		# 검색 변수 갱신
		if event.widget.curselection():
			self.SIGUNGU = self.listBoxSIGUNGU.selection_get()
			self.UPMYONDONG = ''

		# 읍면동 리스트박스 비우기
		self.listBoxUPMYONDONG.delete(0, END)

		# 읍면동 리스트박스 갱신
		for data in UPMYONDONG[self.SIGUNGU]:
			self.listBoxUPMYONDONG.insert(END, data)


# 읍면동 선택
	def UPMYONDONGSelect(self, event):
		# 검색 변수 갱신
		if event.widget.curselection():
			self.UPMYONDONG = self.listBoxUPMYONDONG.selection_get()
		pass


# 병원 이름 선택
	def hospitalSelect(self, event):
		if not self.listboxHospital.curselection():
			print("empty hospital list")
			return
		select = self.listboxHospital.curselection()[0]
		self.lastSelectHospitalIdx = select

		self.pharmacyList.clear()
		self.listboxPharmacy.delete(0, END)
		pos = self.hospitalList[select].pos

		# 약국 검색
		response = search(url=pharmacy_url, key=pharmacy_pw, 
			sidoCd=str(SIDO[self.SIDO] * 10000), sgguCd=str(SIGUNGU[self.SIGUNGU]), 
			xPos=pos[0], yPos=pos[1], radius=1000, numOfRows='500')

		# 리스트에 붙여넣는다
		from xml.etree import ElementTree
		pharmacyTree = ElementTree.fromstring(response.content)
		pharmacyElement = pharmacyTree.iter("item")

		for item in pharmacyElement:
			pharmacy = Pharmacy()
			pharmacy.getInfo(item)
			self.pharmacyList.append(pharmacy)

		self.pharmacyList.sort(key=lambda x : x.distance)

		while len(self.pharmacyList) > 10:
			self.pharmacyList.pop()

		for i, pharmacy in enumerate(self.pharmacyList):
			self.listboxPharmacy.insert(END, "[{:}]: ".format(i + 1) + pharmacy.yadmNm)
		


# 약국 이름 선택
	def pharmacySelect(self, event):
		if not self.listboxPharmacy.curselection():
			return

		cur = self.listboxPharmacy.curselection()[0]
		print(cur)
		print(self.pharmacyList[cur].distance)
		pass

	def testSetting(self):
		self.listBoxSIGUNGU.insert(END, "시흥시")
		self.listBoxSIGUNGU.insert(END, "asdf")
		self.listBoxSIGUNGU.insert(END, "zxcv")

		self.listBoxUPMYONDONG.insert(END, "정왕동")
		self.listBoxUPMYONDONG.insert(END, "456")
		self.listBoxUPMYONDONG.insert(END, "789")
		pass


def search(url, key, page='1', numOfRows='10', sidoCd='', sgguCd='', emdongNm='', yadmNm='', zipCd='', clCd='', dgsbjtCd='', xPos='', yPos='', radius=''):
	# 병원을 검색한다
	import requests
	params = {
		'serviceKey' : key, 'pageNo' : page, 'numOfRows' : numOfRows, 'sidoCd' : sidoCd, 
		'sgguCd' : sgguCd, 'emdongNm' : emdongNm, 'yadmNm' : yadmNm, 'zipCd' : zipCd, 
		'clCd' : clCd, 'dgsbjtCd' : dgsbjtCd, 'xPos' : xPos, 'yPos' : yPos, 'radius' : radius }

	return requests.get(url, params=params)


if __name__ == '__main__':
	hospital = MainWindow()
	hospital.mainloop()


