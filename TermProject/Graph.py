from tkinter import *
import Server as server

class Graph:
    def __init__(self, hospitalList):
        self.hospitalList = hospitalList
        self.barnum = 0

        server.gwindow = Toplevel(server.window)
        server.gwindow.geometry("1200x400+600+450")
        server.gwindow.title("병원 종류 분포도")

        w = Canvas(server.gwindow, width = 1000, height=300, bg='green') 
        w.place(relx=.5, rely=.5,anchor= CENTER)

        # 데이터 분류
        hospitalNum = {'상급종합' : 0, '종합병원' : 0, '병원' : 0, '요양병원' : 0, '정신병원' : 0, '의원' : 0, '치과병원' : 0, '치과의원' : 0, '조산원' : 0, '보건소' : 0, '보건지소' : 0, '보건진료소' : 0, '보건의료원' : 0, '한방병원' : 0, '한의원' : 0}
        for hospital in self.hospitalList:
            hospitalNum[hospital.clCdNm] += 1

        Graph.drawGraph(self, w, hospitalNum, 1000, 300)        
        

    def drawGraph(self, canvas, data, canvasWidth, canvasHeight):
        canvas.delete('hospital')

        if not len(data):
            canvas.create_text(canvasWidth/2,(canvasHeight/2), text="No Data", tags="hospital") 
            return

        nData = 15
        nMax = max(data.values())
        nMin = min(data.values())

        canvas.create_rectangle(0, 0, canvasWidth, canvasHeight, fill='white', tag="hospital")

        if nMax == 0: # devide by zero 방지
            nMax=1

        rectWidth = (canvasWidth // nData) # 데이터 1개의 폭. 
        bottom = canvasHeight - 20 # bar의 bottom 위치 
        maxheight = canvasHeight - 40 # bar의 최대 높이

        for key in data: # 그래프 색깔
            if nMax == data[key]: 
                color="red"
            elif nMin == data[key]: 
                color='blue'
            else: 
                color="grey"
            
            curHeight = maxheight * data[key] / nMax
            top = bottom - curHeight # bar의 top 위치
            left = self.barnum * rectWidth # bar의 left 위치
            right = (self.barnum + 1) * rectWidth # bar의 right 위치

            # 그래프 그리기
            canvas.create_rectangle(left, top, right, bottom, fill=color, tag="hospital", activefill='yellow')
            
            canvas.create_text((left+right)//2, top-10, text=data[key], tags="hospital")
            canvas.create_text((left+right)//2, bottom+10, text=key, tags="hospital")
            self.barnum += 1

