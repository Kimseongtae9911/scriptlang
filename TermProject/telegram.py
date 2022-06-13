from math import dist
import time
import sqlite3
from urllib import response
import telepot
from pprint import pprint
from urllib.request import urlopen

# import Hospital as main
from InfoClass import Hospital
from InfoClass import Pharmacy
from locationDict import *

bot = telepot.Bot("5595829384:AAGCIPcSZZG5MD62bvve8GAd3X7g6CTBgYE")

bot.sendMessage("5460751414", "hello")

hospital_pw = "5wsKqI6xrBpV5YTufFeyzDKJeU+SGnMJpBz87SPB4sfds/wcAwRU3K1d72Ph5mSLJL+VwfIqeffp4WvfklvOpg=="
pharmacy_pw = "5wsKqI6xrBpV5YTufFeyzDKJeU+SGnMJpBz87SPB4sfds/wcAwRU3K1d72Ph5mSLJL+VwfIqeffp4WvfklvOpg=="

hospital_url = 'http://apis.data.go.kr/B551182/hospInfoService1/getHospBasisList1'
pharmacy_url = 'http://apis.data.go.kr/B551182/pharmacyInfoService/getParmacyBasisList'

def findSIGUNGU(umd):
	for key, val in UPMYONDONG.items():
		if umd in val:
			return key
	return None


def handle(msg): 
	content_type, chat_type, chat_id = telepot.glance(msg)
	if content_type != 'text': 
		sendMessage(chat_id, '난 텍스트 이외의 메시지는 처리하지 못해요.') 
		return
	
	text = msg['text'] 
	args = text.split(' ')

	if len(args) != 2:
		sendMessage(chat_id, '''모르는 명령어입니다.\n
		[동(읍면) 병원명]을 입력해주세요
		예시) 정왕동 시화병원.''')
		return
	
	sigungu = findSIGUNGU(args[0])

	if sigungu is None:
		sendMessage(chat_id, '알 수 없는 동 입니다. \n다시 입력해주세요')
		return

	sggcd = SIGUNGU[sigungu]
	sdcd = (sggcd // 10000) * 10000

	res = searchHospital(args[0], args[1], str(sdcd), str(sggcd))

	if len(res) <= 0:
		sendMessage(chat_id, '알 수 없는 병원 이름 입니다. \n다시 입력해주세요')
		return

	respond = "============병원 정보============\n"
	for hos in res:
		respond += "병원 명 : " + hos.yadmNm + ', ' + hos.yadmNm + '\n'
		respond += "주소 : " + hos.addr + '\n'
		respond += "전화번호 : " + hos.telno + '\n\n'

		pharRes = searchPharmacy(args[0], hos.pos[0], hos.pos[1], str(sdcd), str(sggcd))
		if len(pharRes):
			pharRes.sort(key=lambda x : x.distance)
			respond += '---가장 가까운 약국--\n'
			respond += '약국 명  : ' + pharRes[0].yadmNm + '\n'
			respond += '거리 : {0:0.1f}m\n'.format(pharRes[0].distance)
			respond += '================================\n'
			print(pharRes[0].distance)
			
	sendMessage(chat_id, respond)


def searchHospital(dong, hospitalName, sdcd='', sggcd=''):
	response = search(sidoCd=sdcd, sgguCd=sggcd, emdongNm=dong, yadmNm=hospitalName, key=hospital_pw, url=hospital_url)

	from xml.etree import ElementTree
	HospitalTree = ElementTree.fromstring(response.content)
	hospitalElememt = HospitalTree.iter("item")

	hospitalList = []
	for item in hospitalElememt:
		hospital = Hospital()
		hospital.getInfo(item)
		hospitalList.append(hospital)

	return hospitalList
	
def searchPharmacy(dong, posx, posy, sdcd='', sggcd=''):
	response = search(sidoCd=sdcd, sgguCd=sggcd, emdongNm=dong, xPos=posx, yPos=posy, key=pharmacy_pw, url=pharmacy_url, radius=1000, numOfRows=500)
	
	from xml.etree import ElementTree
	HospitalTree = ElementTree.fromstring(response.content)
	hospitalElememt = HospitalTree.iter("item")

	pharmacyList = []
	for item in hospitalElememt:
		pharmacy = Pharmacy()
		pharmacy.getInfo(item)
		pharmacyList.append(pharmacy)

	return pharmacyList


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


def sendMessage(user, msg): 
	try:
		bot.sendMessage(user, msg) 
	except: 
		return

# from noti import bot
bot.message_loop(handle)
print('Listening...') 
while 1: 
	time.sleep(10)
