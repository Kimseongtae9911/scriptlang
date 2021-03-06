from tkinter import *
from tkinter import font
from player import *
from dice import *
from configuration import *
import tkinter.messagebox    

class YahtzeeBoard:
    # index들
    UPPERTOTAL = 6 # "Upper Scores" 위치의 index.
    UPPERBONUS = 7 # "Upper Bonus(35)" 위치의 index.
    LOWERTOTAL = 15 # "Lower Scores" 위치의 index.
    TOTAL = 16 # "Total" 위치의 index.

    # 객체 리스트
    dice = []       # Dice() 객체의 리스트.
    diceButtons = [] # 각 주사위를 표현하는 Button 객체의 리스트.
    fields = []     # 각 플레이어별 점수판(카테고리). Button 객체의 2차원 리스트.
                    # 열: 플레이어 (0열=플레이어1, 1열=플레이어2,…)
                    # 17행: upper카테고리6행, upperScore, upperBonus, lower카테고리7행, LowerScore, Total
    players = []    # 플레이어 수 만큼의 Player 인스턴스를 가짐.
    numPlayers = 0  # # 플레이어 수
    player = 0      # players 리스트에서 현재 플레이어의 index.
    round = 0       # 13 라운드 중 몇번째인지 (0~12 사이의 값을 가짐)
    roll = 0        # 각 라운드에서 3번 중 몇번째 굴리기인지 (0~2 사이의 값을 가짐)
    
    # 색깔
    color_btn_bg = 'SystemButtonFace'

    def __init__(self):
        self.InitGame()

    def InitGame(self): #player window 생성하고 최대 10명까지 플레이어 설정
        self.pwindow = Tk()
        self.pwindow.title = "Player Setting"
        self.TempFont = font.Font(size=12, weight='bold', family='Consolas')
        self.label = []
        self.entry = []
        self.label.append(Label(self.pwindow, text="플레이어 수", font=self.TempFont))
        self.label[0].grid(row=0, column=0)

        for i in range(1,11):
            self.label.append( Label(self.pwindow, text='플레이어'+str(i)+' 이름', font=self.TempFont))
            self.label[i].grid(row=i, column=0)
        for i in range(11):
            self.entry.append(Entry(self.pwindow, font=self.TempFont))
            self.entry[i].grid(row=i, column=1)
        Button(self.pwindow, text='Yahtzee 플레이어 설정 완료', font=self.TempFont, command=self.InitAllPlayers).grid(row=11, column=0)

        self.pwindow.mainloop()

    def InitAllPlayers(self): # 플레이어 설정 완료 버튼 누르면 실행
        self.numPlayers = int(self.entry[0].get())
        for i in range(1, self.numPlayers+1):
            self.players.append(Player(str(self.entry[i].get())))
        self.pwindow.destroy()

        self.makeInterface() #Yahtzee 보드판 플레이어 수 만큼 생성

    def makeInterface(self): 
        self.window = Tk("Yahtzee Game")
        self.window.title = "Yahtzee Game"
        self.TempFont = font.Font(size=12, weight='bold', family='Consolas')
        
        for i in range(5): #Dice 객체 5개 생성
            self.dice.append(Dice())
        
        self.rollDice = Button(self.window, text="Roll Dice", font=self.TempFont, command=self.rollDiceListener, bg=self.color_btn_bg) # Roll Dice 버튼
        self.rollDice.grid(row=0, column=0)

        for i in range(5): #dice 버튼 5개 생성
            #각각의 dice 버튼에 대한 이벤트 처리 diceListener 연결
            #람다 함수를 이용하여 diceListener 매개변수 설정하면 하나의 Listener로 해결
            self.diceButtons.append(Button(self.window, text="?", font=self.TempFont, width=8, bg=self.color_btn_bg, command=lambda row=i: self.diceListener(row)))
            self.diceButtons[i].grid(row=i + 1, column=0)

        for i in range(self.TOTAL + 2): # i행 : 점수
            Label(self.window, text=Configuration.configs[i], font=self.TempFont).grid(row=i, column=1)
            for j in range(self.numPlayers): # j열 : 플레이어
                if (i == 0): # 플레이어 이름 표시
                    Label(self.window, text=self.players[j].toString(), font=self.TempFont).grid(row=i, column=2 + j)
                else:
                    if (j==0): #각 행마다 한번씩 리스트 추가, 다중 플레이어 지원
                        self.fields.append(list())
                    #i-1행에 플레이어 개수 만큼 버튼 추가하고 이벤트 Listener 설정, 매개변수 설정
                    self.fields[i-1].append(Button(self.window, text="", font=self.TempFont, width=8, command=lambda row=i-1: self.categoryListener(row)))
                    self.fields[i-1][j].grid(row=i,column=2 + j)
                    # 누를 필요없는 버튼은 disable 시킴
                    if (j != self.player or (i-1) == self.UPPERTOTAL or (i-1) == self.UPPERBONUS or (i-1) == self.LOWERTOTAL or (i-1) == self.TOTAL):
                        self.fields[i-1][j]['state'] = 'disabled'
                        self.fields[i-1][j]['bg'] = 'light gray'

        #상태 메시지 출력
        self.bottomLabel=Label(self.window, text=self.players[self.player].toString() + "차례: Roll Dice 버튼을 누르세요", width=35, font=self.TempFont)
        self.bottomLabel.grid(row=self.TOTAL + 2, column=0, columnspan=2)
        self.window.mainloop()

    def rollDiceListener(self): # 주사위 굴리기 함수
        if self.roll == 0:
            for i in range(5):
                self.diceButtons[i]['state'] = 'normal'

        for i in range(5):
            if (self.diceButtons[i]['bg']!='light gray'):
                self.dice[i].rollDie()
                self.diceButtons[i].configure(text=str(self.dice[i].getRoll()))

        if (self.roll == 0 or self.roll == 1):
            self.roll += 1
            self.rollDice.configure(text="Roll Again")
            self.bottomLabel.configure(text="보관할 주사위 선택 후 Roll Again")

        elif (self.roll==2):
            self.bottomLabel.configure(text="카테고리를 선택하세요")
            self.rollDice['state'] = 'disabled'
            self.rollDice['bg'] = 'light gray'
            self.roll = 0

        sum = 0
        for i in range(self.TOTAL+1):
            if (self.fields[i][self.player]['text'] != '' or i == self.UPPERTOTAL or i == self.UPPERBONUS or i == self.LOWERTOTAL or i == self.TOTAL):
                self.fields[i][self.player]['state'] = 'disabled'
                self.fields[i][self.player]['bg'] = 'light gray'
                pass
            else:
                self.fields[i][self.player]['state'] = 'normal'
                self.fields[i][self.player]['bg'] = self.color_btn_bg
            score = Configuration.score(i, self.dice)

    def diceListener(self, row): # 각 주사위에 해당되는 버튼 클릭 : disable 시키고 배경색을 어둡게 바꿔 표현해 주기.
        self.diceButtons[row]['state'] = 'disabled'
        self.diceButtons[row]['bg'] = 'light gray'

    def categoryListener(self,row):  # 카레고리 버튼 눌렀을 때의 처리.
        score = Configuration.score(row,self.dice) #점수 계산
        index = row
        if (row > 7):
            index = row-2
    
        # 선택한 카테고리 점수 적고 버튼 disable 시킴
        self.players[self.player].setScore(score,index)
        self.players[self.player].setAtUsed(index)
        self.fields[row][self.player].configure(text=str(score))
        self.fields[row][self.player]['state'] = 'disabled'
        self.fields[row][self.player]['bg'] = 'light gray'
    
        # UPPER category가 전부 사용되었으면 UpperScore, UpperBonus 내용 채우기
        if (self.players[self.player].allUpperUsed()):
            self.fields[self.UPPERTOTAL][self.player].configure(text = str(self.players[self.player].getUpperScore()))
            if (self.players[self.player].getUpperScore() > 63):
                self.fields[self.UPPERBONUS][self.player].configure(text="35")#UPPERBONUS=7
            else:
                self.fields[self.UPPERBONUS][self.player].configure(text="0")#UPPERBONUS=7
    
        # LOWER category 전부 사용되었으면 LowerScore 채우기
        if (self.players[self.player].allLowerUsed()):
            self.fields[self.LOWERTOTAL][self.player].configure(text = str(self.players[self.player].getLowerScore()))

        # UPPER category와 LOWER category가 전부 사용되었으면 TOTAL 채우기
        if (self.players[self.player].allUpperUsed() and self.players[self.player].allLowerUsed()):
            self.fields[self.TOTAL][self.player].configure(text = str(self.players[self.player].getTotalScore()))

        #다음 플레이어로 넘어가고 선택할 수 없는 카테고리들은 disable 시킴
        self.player = (self.player + 1) % self.numPlayers
        self.bottomLabel.configure(text=self.players[self.player].toString()+"차례: Roll Dice 버튼을 누르세요")
        for i in range(self.TOTAL+1):
            for j in range(self.numPlayers):
                    self.fields[i][j]['state'] = 'disabled'
                    self.fields[i][j]['bg'] = 'light gray'

        # 라운드 증가 시키고 종료 검사
        if (self.player == 0):
            self.round += 1
        if (self.round == 13):
            self.players.sort(key=lambda x: x.getTotalScore())
            msg = tkinter.messagebox.showinfo('결과', self.players[-1].toString()+'의 승리!')
            if msg == 'ok':
                self.window.destroy()
                self.resetGame()
        
        # 다시 Roll Dice 과 diceButtons 버튼 활성화
        self.roll = 0
        self.rollDice['text'] = 'Roll Dice'
        self.rollDice['state'] = 'normal'
        self.rollDice['bg'] = 'SystemButtonFace'
        for i in range(5): #dice 버튼 5개 생성
            self.diceButtons[i]['text'] = '?'
            self.diceButtons[i]['state'] = 'disabled'
            self.diceButtons[i]['bg'] = self.color_btn_bg
    
    def resetGame(self):
        self.dice.clear()
        self.diceButtons.clear()
        self.fields.clear()
        self.players.clear()
        self.numPlayers = 0
        self.player = 0
        self.round = 0
        self.roll = 0
        self.InitGame()


if __name__ == '__main__':
    YahtzeeBoard()