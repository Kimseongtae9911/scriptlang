import Server as server
from tkinter import *
from tkinter import ttk
import folium
import webbrowser

pw = "5wsKqI6xrBpV5YTufFeyzDKJeU+SGnMJpBz87SPB4sfds/wcAwRU3K1d72Ph5mSLJL+VwfIqeffp4WvfklvOpg=="

SIDO = {
'서울특별시':	11,
'부산광역시':	21,
'인천광역시':	22,
'대구광역시':	23,
'광주광역시':	24,
'대전광역시':	25,
'울산광역시':	26,
'세종특별자치시':	41,
'경기도':	31,
'강원도':	32,
'충청북도':	33,
'충청남도':	34,
'전라북도':	35,
'전라남도':	36,
'경상북도':	37,
'경상남도':	38,
'제주특별자치도':	39
}

SIGUNGU = {
	"강남구" : 110001,
	"강동구" : 110002,
	"강서구" : 110003,
	"관악구" : 110004,
	"구로구" : 110005,
	"도봉구" : 110006,
	"동대문구" : 110007,
	"동작구" : 110008,
	"마포구" : 110009,
	"서대문구" : 110010,
	"성동구" : 110011,
	"성북구" : 110012,
	"영등포구" : 110013,
	"용산구" : 110014,
	"은평구" : 110015,
	"종로구" : 110016,
	"중구" : 110017,
	"송파구" : 110018,
	"중랑구" : 110019,
	"양천구" : 110020,
	"서초구" : 110021,
	"노원구" : 110022,
	"광진구" : 110023,
	"강북구" : 110024,
	"금천구" : 110025,
	"부산남구" : 210001,
	"부산동구" : 210002,
	"부산동래구" : 210003,
	"부산진구" : 210004,
	"부산북구" : 210005,
	"부산서구" : 210006,
	"부산영도구" : 210007,
	"부산중구" : 210008,
	"부산해운대구" : 210009,
	"부산사하구" : 210010,
	"부산금정구" : 210011,
	"부산강서" : 210012,
	"부산연제" : 210013,
	"부산수영" : 210014,
	"부산사상" : 210015,
	"부산기장" : 210100,
	"인천미추홀구" : 220001,
	"인천동구" : 220002,
	"인천부평구" : 220003,
	"인천중구" : 220004,
	"인천서구" : 220005,
	"인천남동구" : 220006,
	"인천연수구" : 220007,
	"인천계양구" : 220008,
	"인천강화군" : 220100,
	"인천옹진군" : 220200,
	"대구남구" : 230001,
	"대구동구" : 230002,
	"대구북구" : 230003,
	"대구서구" : 230004,
	"대구수성구" : 230005,
	"대구중구" : 230006,
	"대구달서구" : 230007,
	"대구달성군" : 230100,
	"광주동구" : 240001,
	"광주북구" : 240002,
	"광주서구" : 240003,
	"광주광산구" : 240004,
	"광주남구" : 240005,
	"대전유성구" : 250001,
	"대전대덕구" : 250002,
	"대전서구" : 250003,
	"대전동구" : 250004,
	"대전중구" : 250005,
	"울산남구" : 260001,
	"울산동구" : 260002,
	"울산중구" : 260003,
	"울산북구" : 260004,
	"울산울주군" : 260100,
	"가평군" : 310001,
	"강화군" : 310002,
	"양주군" : 310008,
	"양평군" : 310009,
	"여주군" : 310010,
	"연천군" : 310011,
	"옹진군" : 310012,
	"평택군" : 310016,
	"포천군" : 310017,
	"광명시" : 310100,
	"동두천시" : 310200,
	"부천시" : 310300,
	"부천소사" : 310301,
	"부천오정" : 310302,
	"부천원미" : 310303,
	"성남수정" : 310401,
	"성남중원" : 310402,
	"성남분당" : 310403,
	"송탄시" : 310500,
	"수원시" : 310600,
	"수원권선구" : 310601,
	"수원장안구" : 310602,
	"수원팔달구" : 310603,
	"수원영통구" : 310604,
	"안양만안구" : 310701,
	"안양동안구" : 310702,
	"의정부시" : 310800,
	"과천시" : 310900,
	"구리시" : 311000,
	"안산시" : 311100,
	"안산단원구" : 311101,
	"안산상록구" : 311102,
	"평택시" : 311200,
	"하남시" : 311300,
	"군포시" : 311400,
	"남양주시" : 311500,
	"의왕시" : 311600,
	"시흥시" : 311700,
	"오산시" : 311800,
	"고양덕양구" : 311901,
	"고양일산서구" : 311902,
	"고양일산동구	" : 311903,
	"용인시" : 312000,
	"용인기흥구" : 312001,
	"용인수지구" : 312002,
	"용인처인구" : 312003,
	"이천시" : 312100,
	"파주시" : 312200,
	"김포시" : 312300,
	"안성시" : 312400,
	"화성시" : 312500,
	"광주시" : 312600,
	"양주시" : 312700,
	"포천시" : 312800,
	"여주시" : 312900,
	"고성군" : 320001,
	"양구군" : 320004,
	"양양군" : 320005,
	"영월군" : 320006,
	"인제군" : 320008,
	"정선군" : 320009,
	"철원군" : 320010,
	"평창군" : 320012,
	"홍천군" : 320013,
	"화천군" : 320014,
	"횡성군" : 320015,
	"강릉시" : 320100,
	"동해시" : 320200,
	"속초시" : 320300,
	"원주시" : 320400,
	"춘천시" : 320500,
	"태백시" : 320600,
	"삼척시" : 320700,
	"괴산군" : 330001,
	"단양군" : 330002,
	"보은군" : 330003,
	"영동군" : 330004,
	"옥천군" : 330005,
	"음성군" : 330006,
	"제천군" : 330007,
	"진천군" : 330009,
	"청원군" : 330010,
	"증평군" : 330011,
	"청주시" : 330100,
	"청주상당구" : 330101,
	"청주흥덕구" : 330102,
	"청주청원구" : 330103,
	"청주서원구" : 330104,
	"충주시" : 330200,
	"제천시" : 330300,
	"금산군" : 340002,
	"당진군" : 340004,
	"부여군" : 340007,
	"서천군" : 340009,
	"연기군" : 340011,
	"예산군" : 340012,
	"천안군" : 340013,
	"청양군" : 340014,
	"홍성군" : 340015,
	"태안군" : 340016,
	"천안시" : 340200,
	"천안서북구" : 340201,
	"천안동남구" : 340202,
	"공주시" : 340300,
	"보령시" : 340400,
	"아산시" : 340500,
	"서산시" : 340600,
	"논산시" : 340700,
	"계룡시" : 340800,
	"당진시" : 340900,
	"고창군" : 350001,
	"무주군" : 350004,
	"부안군" : 350005,
	"순창군" : 350006,
	"완주군" : 350008,
	"익산군" : 350009,
	"임실군" : 350010,
	"장수군" : 350011,
	"진안군" : 350013,
	"군산시" : 350100,
	"남원시" : 350200,
	"익산시" : 350300,
	"전주시" : 350400,
	"전주완산구" : 350401,
	"전주덕진구" : 350402,
	"정읍시" : 350500,
	"김제시" : 350600,
	"강진군" : 360001,
	"고흥군" : 360002,
	"곡성군" : 360003,
	"구례군" : 360006,
	"담양군" : 360008,
	"무안군" : 360009,
	"보성군" : 360010,
	"신안군" : 360012,
	"영광군" : 360014,
	"영암군" : 360015,
	"완도군" : 360016,
	"장성군" : 360017,
	"장흥군" : 360018,
	"진도군" : 360019,
	"함평군" : 360020,
	"해남군" : 360021,
	"화순군" : 360022,
	"나주시" : 360200,
	"목포시" : 360300,
	"순천시" : 360400,
	"여수시" : 360500,
	"광양시" : 360700,
	"고령군" : 370002,
	"군위군" : 370003,
	"달성군" : 370005,
	"봉화군" : 370007,
	"성주군" : 370010,
	"영덕군" : 370012,
	"영양군" : 370013,
	"영일군" : 370014,
	"예천군" : 370017,
	"울릉군" : 370018,
	"울진군" : 370019,
	"의성군" : 370021,
	"청도군" : 370022,
	"청송군" : 370023,
	"칠곡군" : 370024,
	"경주시" : 370100,
	"구미시" : 370200,
	"김천시" : 370300,
	"안동시" : 370400,
	"영주시" : 370500,
	"영천시" : 370600,
	"포항시" : 370700,
	"포항남구" : 370701,
	"포항북구" : 370702,
	"문경시" : 370800,
	"상주시" : 370900,
	"경산시" : 371000,
	"거창군" : 380002,
	"고성군" : 380003,
	"김해군" : 380004,
	"남해군" : 380005,
	"사천군" : 380007,
	"산청군" : 380008,
	"의령군" : 380011,
	"창원군" : 380012,
	"창녕군" : 380014,
	"하동군" : 380016,
	"함안군" : 380017,
	"함양군" : 380018,
	"합천군" : 380019,
	"김해시" : 380100,
	"마산시" : 380200,
	"사천시" : 380300,
	"진주시" : 380500,
	"진해시" : 380600,
	"창원시" : 380700,
	"창원마산회원구" : 380701,
	"창원마산합포구" : 380702,
	"창원진해구" : 380703,
	"창원의창구" : 380704,
	"창원성산구" : 380705,
	"통영시" : 380800,
	"밀양시" : 380900,
	"거제시" : 381000,
	"양산시" : 381100,
	"남제주군" : 390001,
	"북제주군" : 390002,
	"서귀포시" : 390100,
	"제주시" : 390200,
	"세종시" : 410000
}

UPMYONDONG = { # 법정동 행정동 확인 필요함
	"강남구" : ['압구정동', '신사동', '청담동', '논현동', '삼성동', '역삼동', '대치동', '도곡동', '개포동', '일원동', '수서동', '자곡동', '율현동', '세곡동'],
	"강동구" : ['강일동', '고덕동', '길동', '둔천동', '명일동', '상일동', '성내동', '암사동', '천호동'],
	"강서구" : ['가양동', '개화동', '공항동', '과해동', '내발산동', '등촌동', '마곡동', '방화동', '염창동', '오곡동', '오쇠동', '외발산동', '화곡동'],
	"관악구" : ['남현동', '봉천동', '신림동'],
	"구로구" : ['가리봉동', '개봉동', '고척동', '구로동', '궁동', '신도림동', '오류동', '온수동', '천왕동', '항동'],
	"도봉구" : ['쌍문동', '방학동', '창동', '도봉동'],
	"동대문구" : ['답십리동', '신설동', '용두동', '이문동', '장안동', '전농동', '제기동', '청량리동' , '회기동', '휘경동'],
	"동작구" : ['노량진동', '대방동', '동작동', '본동', '사당동', '상도동', '신대방동', '흑석동'],
	"마포구" : ['공덕동', '아현동', '도화동', '용강동', '대흥동', '염리동', '신수동', '서강동', '서교동', '합정동', '망원동', '연남동', '성산동', '중동', '상암동'],
	"서대문구" : ['충현동'],
	"성동구" : [],
	"성북구" : [],
	"영등포구" : [],
	"용산구" : [],
	"은평구" : [],
	"종로구" : [],
	"중구" : [],
	"송파구" : [],
	"중랑구" : [],
	"양천구" : [],
	"서초구" : [],
	"노원구" : [],
	"광진구" : [],
	"강북구" : [],
	"금천구" : [],
	"부산남구" : [],
	"부산동구" : [],
	"부산동래구" : [],
	"부산진구" :[],
	"부산북구" : [],
	"부산서구" : [],
	"부산영도구" : [],
	"부산중구" : [],
	"부산해운대구" : [],
	"부산사하구" : [],
	"부산금정구" : [],
	"부산강서" : [],
	"부산연제" : [],
	"부산수영" : [],
	"부산사상" : [],
	"부산기장" : [],
	"인천미추홀구" : [],
	"인천동구" : [],
	"인천부평구" : [],
	"인천중구" : [],
	"인천서구" : [],
	"인천남동구" : [],
	"인천연수구" : [],
	"인천계양구" : [],
	"인천강화군" : [],
	"인천옹진군" : [],
	"대구남구" : [],
	"대구동구" : [],
	"대구북구" : [],
	"대구서구" : [],
	"대구수성구" : [],
	"대구중구" : [],
	"대구달서구" : [],
	"대구달성군" : [],
	"광주동구" : [],
	"광주북구" : [],
	"광주서구" : [],
	"광주광산구" : [],
	"광주남구" : [],
	"대전유성구" : [],
	"대전대덕구" : [],
	"대전서구" : [],
	"대전동구" : [],
	"대전중구" : [],
	"울산남구" : [],
	"울산동구" : [],
	"울산중구" : [],
	"울산북구" :[],
	"울산울주군" : [],
	"가평군" : [],
	"강화군" : [],
	"양주군" : [],
	"양평군" : [],
	"여주군" : [],
	"연천군" : [],
	"옹진군" : [],
	"평택군" : [],
	"포천군" : [],
	"광명시" : [],
	"동두천시" : [],
	"부천시" : [],
	"부천소사" : [],
	"부천오정" : [],
	"부천원미" : [],
	"성남수정" : [],
	"성남중원" : [],
	"성남분당" : [],
	"송탄시" : [],
	"수원시" : [],
	"수원권선구" : [],
	"수원장안구" : [],
	"수원팔달구" : [],
	"수원영통구" : [],
	"안양만안구" : [],
	"안양동안구" : [],
	"의정부시" : [],
	"과천시" : [],
	"구리시" : [],
	"안산시" : [],
	"안산단원구" : [],
	"안산상록구" : [],
	"평택시" : [],
	"하남시" : [],
	"군포시" : [],
	"남양주시" : [],
	"의왕시" : [],
	"시흥시" : [],
	"오산시" : [],
	"고양덕양구" : [],
	"고양일산서구" : [],
	"고양일산동구" : [],
	"용인시" : [],
	"용인기흥구" : [],
	"용인수지구" : [],
	"용인처인구" : [],
	"이천시" : [] ,
"파주시" : [] ,
"김포시" : [] ,
"안성시" : [] ,
"화성시" : [] ,
"광주시" : [] ,
"양주시" : [] ,
"포천시" : [] ,
"여주시" : [] ,
"고성군" : [] ,
"양구군" : [] ,
"양양군" : [] ,
"영월군" : [] ,
"인제군" : [] ,
"정선군" : [] ,
"철원군" : [] ,
"평창군" : [] ,
"홍천군" : [] ,
"화천군" : [] ,
"횡성군" : [] ,
"강릉시" : [] ,
"동해시" : [] ,
"속초시" : [] ,
"원주시" : [] ,
"춘천시" : [] ,
"태백시" : [] ,
"삼척시" : [] ,
"괴산군" : [] ,
"단양군" : [] ,
"보은군" : [] ,
"영동군" : [] ,
"옥천군" : [] ,
"음성군" : [] ,
"제천군" : [] ,
"진천군" : [] ,
"청원군" : [] ,
"증평군" : [] ,
"청주시" : [] ,
"청주상당구" : [],
"청주흥덕구" : [],
"청주청원구" : [],
"청주서원구" : [],
"충주시" : [],
"제천시" : [],
"금산군" : [],
"당진군" : [],
"부여군" : [],
"서천군" : [],
"연기군" : [],
"예산군" : [],
"천안군" : [],
"청양군" : [],
"홍성군" : [],
"태안군" : [],
"천안시" : [],
"천안서북구" : [],
"천안동남구" : [],
"공주시" : [],
"보령시" : [],
"아산시" : [],
"서산시" : [],
"논산시" : [],
"계룡시" : [],
"당진시" : [],
"고창군" : [],
"무주군" : [],
"부안군" : [],
"순창군" : [],
"완주군" : [],
"익산군" : [],
"임실군" : [],
"장수군" : [],
"진안군" : [],
"군산시" : [],
"남원시" : [],
"익산시" : [],
"전주시" : [],
"전주완산구" : [],
"전주덕진구" : [],
"정읍시" : [],
"김제시" : [],
"강진군" : [],
"고흥군" : [],
"곡성군" : [],
"구례군" : [],
"담양군" : [],
"무안군" : [],
"보성군" : [],
"신안군" : [],
"영광군" : [],
"영암군" : [],
"완도군" : [],
"장성군" : [],
"장흥군" : [],
"진도군" : [],
"함평군" : [],
"해남군" : [],
"화순군" : [],
"나주시" : [],
"목포시" : [],
"순천시" : [],
"여수시" : [],
"광양시" : [],
"고령군" : [],
"군위군" : [],
"달성군" : [],
"봉화군" : [],
"성주군" : [],
"영덕군" : [],
"영양군" : [],
"영일군" : [],
"예천군" : [],
"울릉군" : [],
"울진군" : [],
"의성군" : [],
"청도군" : [],
"청송군" : [],
"칠곡군" : [],
"경주시" : [],
"구미시" : [],
"김천시" : [],
"안동시" : [],
"영주시" : [],
"영천시" : [],
"포항시" : [],
"포항남구" : [],
"포항북구" : [],
"문경시" : [],
"상주시" : [],
"경산시" : [],
"거창군" : [],
"고성군" : [],
"김해군" : [],
"남해군" : [],
"사천군" : [],
"산청군" : [],
"의령군" : [],
"창원군" : [],
"창녕군" : [],
"하동군" : [],
"함안군" : [],
"함양군" : [],
"합천군" : [],
"김해시" : [],
"마산시" : [],
"사천시" : [],
"진주시" : [],
"진해시" : [],
"창원시" : [],
"창원마산회원구" : [],
"창원마산합포구" : [],
"창원진해구" : [],
"창원의창구" : [],
"창원성산구" : [],
"통영시" : [],
"밀양시" : [],
"거제시" : [],
"양산시" : [],
"남제주군" : [],
"북제주군" : [],
"서귀포시" : [],
"제주시" : [],
"세종시" : []
}

ZIPCODE = {
	'종합병원' : 2010,
	'병원' : 2030,
	'요양병원': 2040,
	'치과' : 2050,
	'한방' : 2060,
	'의원' : 2070,
	'보건기관' : 2080,
	'조산원' : 2090
}

CLCODE = {
	'일반의' : '00',
	'내과' : '01',
	'신경과' : '02',
	'정신건강의학과' : '03',
	'외과' : '04',
	'정형외과' : '05',
	'신경외과' : '06',
	'흉부외과' : '07',
	'성형외과' : '08',
	'마취통증의학과' : '09',
	'산부인과' : '10',
	'소아청소년과' : '11',
	'안과' : '12',
	'이비인후과' : '13',
	'피부과' : '14',
	'비뇨의학과' : '15',
	'영상의학과' : '16',
	'방사선종양학과' : '17',
	'병리과' : '18',
	'진단검사의학과' : '19',
	'결핵과' : '20',
	'재활의학과' : '21',
	'핵의학과' : '22',
	'가정의학과' : '23',
	'응급의학과' : '24',
	'직업환경의학과' : '25',
	'예방의학과' : '26',
	'구강악안면외과' : '50',
	'치과보철과' : '51',
	'치과교정과' : '52',
	'소아치과' : '53',
	'치주과' : '54',
	'치과보존과' : '55',
	'구강내과' : '56',
	'영상치의학과' : '57',
	'구강병리과' : '58',
	'예방치과' : '59',
	'통합치의학과' : '61',
	'한방내과' : '80',
	'한방부인과' : '81',
	'한방소아과' : '82',
	'한방안이비인후피부과' : '83',
	'한방신경정신과' : '84',
	'침구과' : '85',
	'한방재활의학과' : '86',
	'사상체질과' : '87',
	'한방응급' : '88'
}


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

		self.buttonEmailSendButton = Button(frameSubs, font=("나눔고딕코딩", 13), text="이메일", command=self.pressedEmail)
		self.comboBoxHospitalCategory = ttk.Combobox(frameSubs, font=("나눔고딕코딩", 13), width=10, values=list(ZIPCODE.keys()))
		self.comboBoxsubject = ttk.Combobox(frameSubs, font=("나눔고딕코딩", 13), width=10, values=list(CLCODE.keys()))
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
		self.buttonSearch = Button(frameEntry, font=("나눔고딕코딩", 13), text="검색", width=3, height=1, command=self.pressedSearch)
		self.buttonSearch.pack(side='left', fill='both', padx=10)

		# 병원 - 지도 버튼
		self.mapphoto = PhotoImage(file='TermProject/Resource/Map.png')
		self.buttonMap = Button(frameEntry, image=self.mapphoto, command=self.pressedMap)
		self.buttonMap.pack(side='left', fill='both', padx=10)

		# 결과창
		self.listboxHospital = Listbox(frameResultList, selectmode='extended', width=30)
		self.listboxPharmacy = Listbox(frameResultList, selectmode='extended', width=30)
		self.listboxHospital.pack(side='left', fill='both', padx=10)
		self.listboxPharmacy.pack(side='right', fill='both', padx=10)

		self.HospitalTree = None

	def mainloop(self):
		server.window.mainloop()

	def pressedEmail(self):
		from Email import Mail
		if server.puwindow == None:
			Mail.popupInput()
	
	def pressedSearch(self):
		self.listboxHospital.delete(0, END)
		print("asdf", self.comboBoxHospitalCategory.get())
		if not self.UPMYONDONG:
			# print("error!!!")
			pass
		# print("search :", self.SIDO, self.SIGUNGU, self.UPMYONDONG)
		# 병원을 검색한다
		import requests
		url = 'http://apis.data.go.kr/B551182/hospInfoService1/getHospBasisList1'
		params = {
			'serviceKey' : pw, 'pageNo' : '1', 'numOfRows' : '10', 'sidoCd' : str(SIDO[self.SIDO] * 10000), 
			'sgguCd' : str(SIGUNGU[self.SIGUNGU]), 'emdongNm' : self.UPMYONDONG, 'yadmNm' : self.entryHospitalName.get(), 'zipCd' : '', 
			'clCd' : '', 'dgsbjtCd' : '', 'xPos' : self.entryPosX.get(), 'yPos' : self.entryPosY.get(), 'radius' : '' }
		response = requests.get(url, params=params)
		# print(response.content)		


		# 리스트에 붙여넣는다
		from xml.etree import ElementTree
		self.HospitalTree = ElementTree.fromstring(response.content)
		hospitalElememt = self.HospitalTree.iter("item")
		for item in hospitalElememt:
			strTitle = item.find("yadmNm")
			self.listboxHospital.insert(END, strTitle.text)


	def pressedMap(self):
		self.map_osm = folium.Map(location=[37.3402849, 126.7313189], zoom_start=13)

		folium.Marker([37.3402849, 126.7313189], popup='한국공학대학교').add_to(self.map_osm)
		self.map_osm.save('osm.html')
		webbrowser.open_new('osm.html')

	def SIDOSelect(self, event):
		# 검색 변수 갱신
		if event.widget.curselection():
			self.SIDO = self.listBoxSIDO.selection_get()
			self.SIGUNGU = ''
			self.UPMYONDONG = ''
			print(self.SIDO, SIDO[self.SIDO])

		# 시군구, 읍면동 리스트박스 비우기
		self.listBoxSIGUNGU.delete(0, END)
		self.listBoxUPMYONDONG.delete(0, END)
		
		# 시군구 리스트박스 갱신
		for data in SIGUNGU:
			if SIDO[self.SIDO] == SIGUNGU[data] // 10000:
				self.listBoxSIGUNGU.insert(END, data)

	def SIGUNGUSelect(self, event):
		# 검색 변수 갱신
		if event.widget.curselection():
			self.SIGUNGU = self.listBoxSIGUNGU.selection_get()
			self.UPMYONDONG = ''

		# 읍면동 리스트박스 비우기
		self.listBoxUPMYONDONG.delete(0, END)

		# 읍면동 리스트박스 갱신
		pass


	def UPMYONDONGSelect(self, event):
		# 검색 변수 갱신
		if event.widget.curselection():
			self.UPMYONDONG = self.listBoxUPMYONDONG.selection_get()
		pass

	def testSetting(self):
		for data in SIDO:
			self.listBoxSIDO.insert(END, data)


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
