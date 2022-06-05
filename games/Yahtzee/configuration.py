from dice import *
import math

class Configuration:
    configs = [
        "Category","Ones", "Twos","Threes","Fours","Fives","Sixes",
        "Upper Scores","Upper Bonus(35)","Three of a kind", "Four of a kind", "Full House(25)",
        "Small Straight(30)", "Large Straight(40)", "Yahtzee(50)","Chance","Lower Scores", "Total"
               ]

    @staticmethod
    def getConfigs(self): # 정적 메소드: 객체생성 없이 사용 가능
        return Configuration.configs
    
    @staticmethod
    def score(row, dices): 
        if (row >= 0 and row <= 6):
            return Configuration.Upper(dices,row+1)
        elif (row==8):
            return Configuration.ThreeOfAKind(dices)
        elif (row==9):
            return Configuration.FourOfAKind(dices)
        elif (row==10):
            return Configuration.FullHouse(dices)
        elif (row==11):
            return Configuration.SmallStraight(dices)
        elif (row==12):
            return Configuration.LargeStraight(dices)
        elif (row==13):
            return Configuration.Yahtzee(dices)
        elif (row==14):
            return Configuration.Chance(dices)
        return 0

    def Upper(dices, num):
        cnt = 0
        for i in range(len(dices)):
            if dices[i].getRoll() == num:
                cnt= cnt + num
        return cnt

    def ThreeOfAKind(dices):
        sum = 0
        for i in range(1, 6 + 1):
            cnt = 0
            for j in range(5):
                if i == dices[j].getRoll():
                    cnt += 1
                if cnt >= 3:
                    for a in range(5):
                        sum += dices[a].getRoll()
                    return sum
        return 0

    def FourOfAKind(dices):
        sum = 0
        for i in range(1, 6 + 1):
            cnt = 0
            for j in range(5):
                if i == dices[j].getRoll():
                    cnt += 1
                if cnt >= 4:
                    for a in range(5):
                        sum += dices[a].getRoll()
                    return sum

        return 0

    def FullHouse(dices):
        temp = []
        for i in range(5):
            temp.append(dices[i].getRoll())
        if temp.count(0) == 5:
            return 0
        temp.sort()
        first = False
        second = False
        if temp[0] == temp[1]:
            first = True
            if temp[2] == temp[3] and temp[3] == temp[4]:
                second = True
        if temp[0] == temp[1] and temp[1] == temp[2]:
            first = True
            if temp[3] == temp[4]:
                second = True
        if first and second:
            return 25
        return 0

    def SmallStraight(dices):
        # 1 2 3 4 // 2 3 4 5 /// 3 4 5 6 검사
        # 1 2 2 3 4 // 1 2 3 4 6 // 1 3 4 5 6 // 2 3 4 4 5
        temp = []
        for i in range(5):
            temp.append(dices[i].getRoll())
        temp.sort()
        temp2 = list(set(temp))
        if len(temp2) == 4:
            if temp2[3] - temp2[0] == 3:
                return 30
        # sum2 = 0
        if len(temp2) > 4:
            if temp2[3] - temp2[0] == 3:
                return 30
            if temp2[4] - temp2[1] == 3:
                return 30

        return 0

    def LargeStraight(dices):
        # 1 2 3 4 5 // 2 3 4 5 6 검사
        temp = []
        for i in range(5):
            temp.append(dices[i].getRoll())
        temp.sort()
        temp2 = list(set(temp))
        if len(temp2) > 4:
            if temp2[4] - temp2[0] == 4:
                return 40
        return 0
    
    def Yahtzee(dices):
        temp = []
        for i in range(5):
            temp.append(dices[i].getRoll())
        if temp.count(0) == 5:
            return 0
        num = dices[0].getRoll()
        for i in range(0, 5):
            if num != dices[i].getRoll():
                return 0
            else:
                check = True
        if check:
            return 50

    def Chance(dices):
        sum = 0
        for i in range(len(dices)):
            sum += dices[i].getRoll()
        return sum