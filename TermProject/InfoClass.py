
class Hospital:
	def __init__(self) -> None:
		#<addr>서울특별시 중랑구 신내로 156 (신내동)</addr>
		self.addr = ''
		#<clCd>11</clCd>
		self.clCd = ''
		#<clCdNm>종합병원</clCdNm>
		self.cldNm = ''
		#<telno>02-2276-7000</telno>
		self.telno = ''
		#<XPos>127.0978309</XPos> #<YPos>37.6132762</YPos>
		self.pos = ()
		#<yadmNm>서울특별시서울의료원</yadmNm>
		self.yadmNm = ''

	def getInfo(self, item):
		self.addr = item.find("addr")
		self.clCd = item.find("clCd")
		self.clCdNm = item.find("clCdNm")
		self.telno = item.find("telno")
		self.yadmNm = item.find("yadmNm")
		x = item.find('XPos')		
		y = item.find('YPos')		

		if self.addr is None: self.addr = ''
		else: self.addr = self.addr.text
		if self.clCd is None: self.clCd = ''
		else: self.clCd = self.clCd.text
		if self.clCdNm is None: self.clCdNm = ''
		else: self.clCdNm = self.clCdNm.text
		if self.telno is None: self.telno = ''
		else: self.telno = self.telno.text
		if self.yadmNm is None: self.yadmNm = ''
		else: self.yadmNm = self.yadmNm.text

		if x is None or y is None:
			x = '-1'
			y = '-1'
			self.pos = (x, y)
		else:
			self.pos = (x.text, y.text)


class Pharmacy:
	def __init__(self) -> None:
		# <addr>서울특별시 중랑구 봉화산로 215 1층 (신내동)</addr>
		self.addr = ''
		# <telno>02-3422-3097</telno>
		self.telno = ''
		# <XPos>127.0965492</XPos># <YPos>37.6076585</YPos>
		self.pos = ()
		# <yadmNm>온누리건강약국</yadmNm>
		self.yadmNm = ''
		# <distance>.5478450769582605437588497466708942455</distance>
		self.distance = ''


	def getInfo(self, item):
		self.addr = item.find("addr")
		self.telno = item.find("telno")
		self.yadmNm = item.find("yadmNm")
		x = item.find('XPos')		
		y = item.find('YPos')
		self.distance = item.find("distance")		

		if self.addr is None: self.addr = ''
		else: self.addr = self.addr.text
		if self.telno is None: self.telno = ''
		else: self.telno = self.telno.text
		if self.yadmNm is None: self.yadmNm = ''
		else: self.yadmNm = self.yadmNm.text
		if self.distance is None : self.distance = 9999999
		else: self.distance = float(self.distance.text)

		if x is None or y is None:
			x = '-1'
			y = '-1'
			self.pos = (x, y)
		else:
			self.pos = (x.text, y.text)
