import time
import sqlite3
from urllib import response
import telepot
from pprint import pprint
from urllib.request import urlopen
import re
from datetime import date, datetime

import Hospital as main
from InfoClass import Hospital
from TermProject.InfoClass import Pharmacy

bot = telepot.Bot("5595829384:AAGCIPcSZZG5MD62bvve8GAd3X7g6CTBgYE")

bot.sendMessage("5460751414", "hello")

key = '5wsKqI6xrBpV5YTufFeyzDKJeU+SGnMJpBz87SPB4sfds/wcAwRU3K1d72Ph5mSLJL+VwfIqeffp4WvfklvOpg=='



def handle(msg): 
	content_type, chat_type, chat_id = telepot.glance(msg)
	if content_type != 'text': 
		sendMessage(chat_id, '난 텍스트 이외의 메시지는 처리하지 못해요.') 
		return
	
	text = msg['text'] 
	args = text.split(' ')

	if len(args) >= 2 and args[0].endswith("동"):
		res = searchHospital(args[0], args[1])

		if len(res):
			respond = "============병원 정보============\n"
			for hos in res:
				respond += "병원 명 : " + hos.yadmNm + ', ' + hos.yadmNm + '\n'
				respond += "주소 : " + hos.addr + '\n'
				respond += "전화번호 : " + hos.telno + '\n\n'
				respond += '---주변 약국--\n'

			

			sendMessage(chat_id, respond)
		else:
			sendMessage(chat_id, '잘못된 병원명 혹은 동 입니다!')


	else:
		 sendMessage(chat_id, '''모르는 명령어입니다.\n
		[동(읍면) 병원명]을 입력해주세요
		예시) 정왕동 시화병원.''')


def searchHospital(dong, hospitalName):
	response = main.search(sidoCd='', sgguCd='', emdongNm=dong, yadmNm=hospitalName, key=main.hospital_pw, url=main.hospital_url)

	from xml.etree import ElementTree
	HospitalTree = ElementTree.fromstring(response.content)
	hospitalElememt = HospitalTree.iter("item")

	hospitalList = []
	for item in hospitalElememt:
		hospital = Hospital()
		hospital.getInfo(item)
		hospitalList.append(hospital)

	return hospitalList
	
def searchPharmacy(dong, posx, posy):
	response = main.search(emdongNm=dong, xPos=posx, yPos=posy, key=main.pharmacy_pw, url=main.pharmacy_url)

	
	from xml.etree import ElementTree
	HospitalTree = ElementTree.fromstring(response.content)
	hospitalElememt = HospitalTree.iter("item")

	pharmacyList = []
	for item in hospitalElememt:
		hospital = Hospital()
		hospital.getInfo(item)
		pharmacyList.append(hospital)

	return pharmacyList[0]


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
