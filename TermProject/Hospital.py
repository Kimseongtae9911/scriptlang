import Server as server
from tkinter import *
from tkinter import ttk
from locationDict import *
from InfoClass import *
import folium
import webbrowser


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
		frameEntry = Frame(server.window, padx=10, pady=10)
		frameResultList = Frame(server.window, padx=10, pady=10)
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

		self.emailPhoto = PhotoImage(file='TermProject/Resource/Email.png')
		self.buttonEmailSendButton = Button(frameSubs, image=self.emailPhoto, command=self.pressedEmail)
		self.comboBoxHospitalCategory = ttk.Combobox(frameSubs, font=("나눔고딕코딩", 13), width=10, values=list(ZIPCODE.keys()))
		self.comboBoxsubject = ttk.Combobox(frameSubs, font=("나눔고딕코딩", 13), width=10, values=list(CLCODE.keys()))
		self.buttonEmailSendButton.pack(side='top', fill='both', pady=10)
		self.comboBoxHospitalCategory.pack(side='top', fill='both', pady=20)
		self.comboBoxsubject.pack(side='top', fill='both', pady=20)
		self.comboBoxHospitalCategory.current(0)
		self.comboBoxsubject.current(0)

		# 병원 - 위치
		frameSubEntry = Frame(frameEntry, padx=10, pady=10)
		frameSubEntry.pack(side='left', fill='x')

		self.entryPosX = Entry(frameSubEntry, font=("나눔고딕코딩", 13), width=15)
		self.entryPosY = Entry(frameSubEntry, font=("나눔고딕코딩", 13), width=15)
		Label(frameSubEntry, font=("나눔고딕코딩", 13), text='x').grid(row=0, column=0, pady=10)
		Label(frameSubEntry, font=("나눔고딕코딩", 13), text='y').grid(row=1, column=0, pady=10)
		self.entryPosX.grid(row=0, column=1)
		self.entryPosY.grid(row=1, column=1)

		# 병원 - 이름
		Label(frameEntry, font=("나눔고딕코딩", 13), text='병원명').pack(side='left')
		self.entryHospitalName = Entry(frameEntry, font=("나눔고딕코딩", 13), width=15)
		self.entryHospitalName.pack(side='left')

		# 병원 - 검색 버튼
		self.buttonSearch = Button(frameEntry, font=("나눔고딕코딩", 13), text="검색", width=3, height=1, command=self.pressedSearch)
		self.buttonSearch.pack(side='left', fill='both', padx=10)

		# 병원 - 지도 버튼
		self.mapphoto = PhotoImage(file='TermProject/Resource/Map.png')
		self.buttonMap = Button(frameEntry, image=self.mapphoto, command=self.pressedMap)
		self.buttonMap.pack(side='left', fill='both', padx=10)

		# 결과창
		self.listboxHospital = Listbox(frameResultList, selectmode='extended', width=30)
		self.listboxHospital.bind('<<ListboxSelect>>', self.hospitalSelect)
		self.listboxPharmacy = Listbox(frameResultList, selectmode='extended', width=30)
		self.listboxPharmacy.bind('<<ListboxSelect>>', self.pharmacySelect)
		self.listboxHospital.pack(side='left', fill='both', padx=10)
		self.listboxPharmacy.pack(side='right', fill='both', padx=10)

		self.hospitalList = []
		self.pharmacyList = []

		for data in SIDO:
			if data != '':
				self.listBoxSIDO.insert(END, data)

	def mainloop(self):
		server.window.mainloop()


# 이메일 버튼
	def pressedEmail(self):
		from Email import Mail
		if server.puwindow == None:
			Mail.popupInput()
	

# 검색 버튼
	def pressedSearch(self):
		self.listboxHospital.delete(0, END)
		self.listboxPharmacy.delete(0, END)
		if not self.UPMYONDONG:
			# print("error!!!")
			pass

		# 병원을 검색한다
		response = search(url=hospital_url, key=hospital_pw, sidoCd=str(SIDO[self.SIDO] * 10000),
			sgguCd=str(SIGUNGU[self.SIGUNGU]), emdongNm=self.UPMYONDONG, yadmNm=self.entryHospitalName.get(), 
			zipCd=ZIPCODE[self.comboBoxHospitalCategory.get()], clCd=CLCODE[self.comboBoxsubject.get()],
			xPos=self.entryPosX.get(), yPos=self.entryPosY.get())

		self.hospitalList.clear()

		# 리스트에 붙여넣는다
		from xml.etree import ElementTree
		HospitalTree = ElementTree.fromstring(response.content)
		hospitalElememt = HospitalTree.iter("item")
		cnt = 1
		for item in hospitalElememt:
			strTitle = item.find("yadmNm")
			self.listboxHospital.insert(END, "[{:}]: ".format(cnt) + strTitle.text)
			self.hospitalList.append(Hospital())
			self.hospitalList[cnt - 1].getInfo(item)
			cnt += 1


# 지도 버튼 
	def pressedMap(self):
		onlyname = self.listboxHospital.get(0)
		if onlyname == '':
			# empty
			print("empty list, cant map")
			return
		else:
			print('many hospital')
			# 병원 출력
			for i in range(self.listboxHospital.size()):
				posy, posx = self.hospitalList[i].pos
				name = self.hospitalList[i].yadmNm
				if i == 0:
					self.map_osm = folium.Map(location=[posx, posy], zoom_start=15)
	
				# 선택된 병원인가?
				if self.listboxHospital.curselection() and i == self.listboxHospital.curselection()[0]:
					folium.Marker([posx, posy], popup=name, icon=(folium.Icon(color='red'))).add_to(self.map_osm)
				else:
					folium.Marker([posx, posy], popup=name).add_to(self.map_osm)
			
			# 약국 출력
			for i in range(len(self.pharmacyList)):
				if i >= 10: break

				posy, posx = self.pharmacyList[i].pos
				name = self.pharmacyList[i].yadmNm
				folium.Marker([posx, posy], popup=name, icon=(folium.Icon(color='lightgreen'))).add_to(self.map_osm)

		
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
		pass


# 읍면동 선택
	def UPMYONDONGSelect(self, event):
		# 검색 변수 갱신
		if event.widget.curselection():
			self.UPMYONDONG = self.listBoxUPMYONDONG.selection_get()
		pass


# 병원 이름 선택
	def hospitalSelect(self, event):
		# for i in range(self.listboxHospital.size()):
		# 	print(self.listboxHospital.get(i))

		if not self.listboxHospital.curselection():
			print("empty hospital list")
			return
		#print(self.listboxHospital.curselection())
		#print(self.listboxHospital.selection_get())
		self.listboxPharmacy.delete(0, END)
		self.pharmacyList.clear()
		pos = self.hospitalList[self.listboxHospital.curselection()[0]].pos

		# 약국 검색
		response = search(url=pharmacy_url, key=pharmacy_pw, 
			sidoCd=str(SIDO[self.SIDO] * 10000), sgguCd=str(SIGUNGU[self.SIGUNGU]), 
			xPos=pos[0], yPos=pos[1], radius=1000)

		# 리스트에 붙여넣는다
		from xml.etree import ElementTree
		pharmacyTree = ElementTree.fromstring(response.content)
		pharmacyElement = pharmacyTree.iter("item")
		cnt = 0
		for item in pharmacyElement:
			self.pharmacyList.append(Pharmacy())
			self.pharmacyList[cnt].getInfo(item)
			cnt += 1

		self.pharmacyList.sort(key=lambda x : x.distance)

		for i in range(len(self.pharmacyList)):
			if i >= 10:
				break;
			self.listboxPharmacy.insert(END, "[{:}]: ".format(i + 1) + self.pharmacyList[i].yadmNm)


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


def search(url, key, page='	1', numOfRows='1000', sidoCd='', sgguCd='', emdongNm='', yadmNm='', zipCd='', clCd='', dgsbjtCd='', xPos='', yPos='', radius=''):
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

