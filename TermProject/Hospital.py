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
import cstr
from PIL import Image, ImageTk

hospital_pw = "5wsKqI6xrBpV5YTufFeyzDKJeU+SGnMJpBz87SPB4sfds/wcAwRU3K1d72Ph5mSLJL+VwfIqeffp4WvfklvOpg=="
pharmacy_pw = "5wsKqI6xrBpV5YTufFeyzDKJeU+SGnMJpBz87SPB4sfds/wcAwRU3K1d72Ph5mSLJL+VwfIqeffp4WvfklvOpg=="

hospital_url = 'http://apis.data.go.kr/B551182/hospInfoService1/getHospBasisList1'
pharmacy_url = 'http://apis.data.go.kr/B551182/pharmacyInfoService/getParmacyBasisList'


class MainWindow:
	def __init__(self):
		self.helpinfo = None
		# 창 기본 설정
		self.width = 500
		self.height = 810
		server.window.title("Hospital")
		server.window.geometry("" + str(self.width) + "x" + str(self.height))		

		frameTitle = Frame(server.window, padx=10, pady=10, bg='#2F455C')
		frameHospital = Frame(server.window, padx=10, pady=10, bg='#2F455C')
		frameEntry = Frame(server.window, padx=10, bg='#2F455C')
		frameResultList = Frame(server.window, padx=10, pady=10, bg='#2F455C')
		frameExtraButtons = Frame(server.window, padx=10, pady=10, bg='#2F455C')
		frameTitle.pack(side='top', fill='x')
		frameHospital.pack(side='top', fill='x')
		frameEntry.pack(side='top', fill='x')
		frameExtraButtons.pack(side='bottom', fill='both', )
		frameResultList.pack(side='bottom', fill='both', expand=True)

		# 로고
		img = (Image.open('Resource/Title.png'))
		titleImage = img.resize((300, 70))
		self.titleImage = ImageTk.PhotoImage(titleImage)
		self.canvas = Canvas(frameTitle, width=480, height=100, bg='#2F455C', relief=RIDGE, borderwidth=5)
		self.canvas.pack()
		self.canvas.create_image(240, 53, anchor='center', image=self.titleImage)

		# 병원 카테고리 - 지역
		self.SIDO = ''
		self.SIGUNGU = ''
		self.UPMYONDONG = ''
		self.listBoxSIDO = Listbox(frameHospital, selectmode='extended', height=10, width=13, highlightthickness=3, highlightbackground='#97A2AE')
		self.listBoxSIGUNGU = Listbox(frameHospital, selectmode='extended', height=10, width=13, highlightthickness=3, highlightbackground='#97A2AE')
		self.listBoxUPMYONDONG = Listbox(frameHospital, selectmode='extended', height=10, width=13, highlightthickness=3, highlightbackground='#97A2AE')
		self.listBoxSIDO.bind('<<ListboxSelect>>', self.SIDOSelect)
		self.listBoxSIGUNGU.bind('<<ListboxSelect>>', self.SIGUNGUSelect)
		self.listBoxUPMYONDONG.bind('<<ListboxSelect>>', self.UPMYONDONGSelect)
		self.listBoxSIDO.grid(row=0, column=0, padx=10)
		self.listBoxSIGUNGU.grid(row=0, column=1, padx=10)
		self.listBoxUPMYONDONG.grid(row=0, column=2, padx=10)

		# 병원 카테고리 - 병원 종류
		frameSubs = Frame(frameHospital, padx=10, pady=10, bg='#2F455C')
		frameSubs.grid(row=0, column=3)

		self.comboBoxHospitalCategory = ttk.Combobox(frameSubs, font=("나눔고딕코딩", 13), width=10, values=list(CLCD.keys()))
		self.comboBoxsubject = ttk.Combobox(frameSubs, font=("나눔고딕코딩", 13), width=10, values=list(DGSBJTCD.keys()))
		self.comboBoxHospitalCategory.pack(side='top', fill='both', pady=20)
		self.comboBoxsubject.pack(side='top', fill='both', pady=20)
		self.comboBoxHospitalCategory.current(0)
		self.comboBoxsubject.current(0)

		# 병원 - 이름
		frameNameSearch = Frame(frameEntry, padx=10, pady=10, bg='#2F455C')
		frameNameSearch.pack(side='left')
		self.entryHospitalName = Entry(frameNameSearch, font=("나눔고딕코딩", 13), width=25, borderwidth=5)
		self.entryHospitalName.insert(0, "병원 명 입력")
		self.entryHospitalName.bind('<Button-1>', self.EntryClick)
		self.entryHospitalName.pack(anchor='center')


		# 병원 - 검색 버튼
		frameSearch = Frame(frameEntry, padx=15, pady=10, width=250, bg='#2F455C')
		frameSearch.pack()
		self.buttonSearch = Button(frameSearch, font=("나눔고딕코딩", 13), text="검색", width=6, height=2, relief=RIDGE, borderwidth=5, bg='#97A2AE', command=self.pressedSearch)
		self.buttonSearch.pack()

		# 결과창
		self.listboxHospital = Listbox(frameResultList, selectmode='extended', width=30, highlightthickness=3, highlightbackground='#97A2AE')
		self.listboxHospital.bind('<<ListboxSelect>>', self.hospitalSelect)
		self.listboxPharmacy = Listbox(frameResultList, selectmode='extended', width=30, highlightthickness=3, highlightbackground='#97A2AE')
		self.listboxPharmacy.bind('<<ListboxSelect>>', self.pharmacySelect)
		self.listboxHospital.pack(side='left', fill='both', padx=10)
		self.listboxPharmacy.pack(side='right', fill='both', padx=10)

		# 버튼들
		frameLeftRight = Frame(frameExtraButtons, bg='#2F455C')
		frameEmailMap = Frame(frameExtraButtons, bg='#2F455C')
		frameLeftRight.pack(side='left', expand=True)
		frameEmailMap.pack(side='right', expand=True)
		px = 25

		self.leftImage = PhotoImage(file='Resource/Left.png')
		self.rightImage = PhotoImage(file='Resource/Right.png')
		self.emailPhoto = PhotoImage(file='Resource/Email.png')
		self.mapphoto = PhotoImage(file='Resource/Map.png')

		# 좌우 버튼
		self.buttonGoPerv = Button(frameLeftRight, image=self.leftImage, relief=RIDGE, borderwidth=5, bg='#97A2AE', command=self.pressedPrev)
		self.buttonGoNext = Button(frameLeftRight, image=self.rightImage, relief=RIDGE, borderwidth=5, bg='#97A2AE', command=self.pressedNext)
		self.buttonGoPerv.pack(side='left', padx=px)
		self.buttonGoNext.pack(side='right', padx=px)
		self.page = 1

		# 이메일, 지도 버튼
		self.buttonEmailSendButton = Button(frameEmailMap, image=self.emailPhoto, relief=RIDGE, borderwidth=5, bg='#97A2AE', command=self.pressedEmail)
		self.buttonMap = Button(frameEmailMap, image=self.mapphoto, relief=RIDGE, borderwidth=5, bg='#97A2AE', command=self.pressedMap)
		self.buttonEmailSendButton.pack(side='left', padx=px)
		self.buttonMap.pack(side='right', padx=px)


		self.hospitalList = []
		self.pharmacyList = []

		self.lastSelectHospitalIdx = -1
		self.select = 0
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
			if self.select == 1:
				Mail.popupInput(self.hospitalList[self.lastSelectHospitalIdx], self.pharmacyList)
			else:
				Mail.popupInput(self.hospitalList, self.pharmacyList)
	

# 검색 버튼
	def pressedSearch(self):
		self.lastSelectHospitalIdx = 1
		self.select = 0
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
			self.listboxHospital.insert(END, cstr.endOfList())
			self.lastPage = True
		else:
			while self.listboxHospital.size() < 20:
				self.listboxHospital.insert(END, "")
			self.listboxHospital.insert(END, "                    [{:}] ".format(self.lastSelectHospitalIdx))

		# 그래프 출력 + 예외처리
		if self.comboBoxsubject.get() == '선택안함' and self.comboBoxHospitalCategory.get() == '선택안함' and self.hospitalList != []:
			Graph.Graph(self.hospitalList)	

# 지도 버튼 
	def pressedMap(self):
		# 지도에 병원 표시
		# 선택한 것이 있다면 선택한 병원과 약국만 표시
		# 없다면 리스트의 모든 병원 표시

		i = 0

		if self.hospitalList == []:
			tkinter.messagebox.showinfo('오류', '검색을 먼저 해주세요')
			return

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

		MainWindow.SortSIGUNGU(self)

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

		MainWindow.SortUPMYONDONG(self)


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

		for i,pharmacy in enumerate(self.pharmacyList):
			self.listboxPharmacy.insert(END, "[{:}]: ".format(i + 1) + pharmacy.yadmNm)

		self.select = 1

# 약국 이름 선택
	def pharmacySelect(self, event):
		if not self.listboxPharmacy.curselection():
			return

		cur = self.listboxPharmacy.curselection()[0]
		print(cur)
		print(self.pharmacyList[cur].distance)
		pass
	
# 시군구 정렬
	def SortSIGUNGU(self):
		si = []
		gun = []
		gu = []
		rest = []
		for data in range(self.listBoxSIGUNGU.size()):
			if self.listBoxSIGUNGU.get(data)[-1] == '시':
				si.append(self.listBoxSIGUNGU.get(data))		
			elif self.listBoxSIGUNGU.get(data)[-1] == '군':
				gun.append(self.listBoxSIGUNGU.get(data))
			elif self.listBoxSIGUNGU.get(data)[-1] == '구':
				gu.append(self.listBoxSIGUNGU.get(data))
			else:
				rest.append(self.listBoxSIGUNGU.get(data))
		si.sort()
		gun.sort()
		gu.sort()
		rest.sort()

		self.listBoxSIGUNGU.delete(0, END)
		for data in si:
			self.listBoxSIGUNGU.insert(END, data)
		for data in gun:
			self.listBoxSIGUNGU.insert(END, data)
		for data in gu:
			self.listBoxSIGUNGU.insert(END, data)
		for data in rest:
			self.listBoxSIGUNGU.insert(END, data)

# 읍면동 정렬
	def SortUPMYONDONG(self):
		# 동 가 읍 면
		dong = []
		ga = []
		up = []
		myon = []
		rest = []
		for data in range(self.listBoxUPMYONDONG.size()):
			if self.listBoxUPMYONDONG.get(data)[-1] == '읍':
				up.append(self.listBoxUPMYONDONG.get(data))
			elif self.listBoxUPMYONDONG.get(data)[-1] == '면':
				myon.append(self.listBoxUPMYONDONG.get(data))
			elif self.listBoxUPMYONDONG.get(data)[-1] == '동':
				dong.append(self.listBoxUPMYONDONG.get(data))
			elif self.listBoxUPMYONDONG.get(data)[-1] == '가':
				ga.append(self.listBoxUPMYONDONG.get(data))
			else:
				rest.append(self.listBoxUPMYONDONG.get(data))

		dong.sort()
		ga.sort()
		up.sort()
		myon.sort()
		rest.sort()
		self.listBoxUPMYONDONG.delete(0, END)
		for data in up:
			self.listBoxUPMYONDONG.insert(END, data)
		for data in myon:
			self.listBoxUPMYONDONG.insert(END, data)
		for data in dong:
			self.listBoxUPMYONDONG.insert(END, data)
		for data in ga:
			self.listBoxUPMYONDONG.insert(END, data)
		for data in rest:
			self.listBoxUPMYONDONG.insert(END, data)
		

def search(url, key, page='1', numOfRows='20', sidoCd='', sgguCd='', emdongNm='', yadmNm='', zipCd='', clCd='', dgsbjtCd='', xPos='', yPos='', radius=''):
	# 병원을 검색한다
	import requests
	if yadmNm == '병원 명 입력':
		yadmNm = ''
	params = {
		'serviceKey' : key, 'pageNo' : page, 'numOfRows' : numOfRows, 'sidoCd' : sidoCd, 
		'sgguCd' : sgguCd, 'emdongNm' : emdongNm, 'yadmNm' : yadmNm, 'zipCd' : zipCd, 
		'clCd' : clCd, 'dgsbjtCd' : dgsbjtCd, 'xPos' : xPos, 'yPos' : yPos, 'radius' : radius }

	return requests.get(url, params=params)


if __name__ == '__main__':
	hospital = MainWindow()
	hospital.mainloop()


