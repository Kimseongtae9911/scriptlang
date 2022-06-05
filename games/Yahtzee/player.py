class Player:
    UPPER = 6 # upper category 6개
    LOWER = 7 # lower category 7개

    def __init__(self,name):
        self.name = name
        itemcount = self.UPPER + self.LOWER
        self.scores = [0 for i in range(itemcount)] #13개category점수
        #13개 category 사용여부
        self.used = [False for i in range(itemcount)]

    def setScore(self, score, index):
        self.scores[index] = score
        self.used[index] = True

    def setAtUsed(self, index):
        self.used[index] = True

    def getUpperScore(self):
        sumnum = sum(self.scores[:self.UPPER])
        if sumnum >= 63:
            sumnum += 35
        return sumnum

    def getLowerScore(self):
        return sum(self.scores[-self.LOWER:])

    def toString(self):
        return self.name

    def allUpperUsed(self): # UPPER category 전부 사용되을 때 True, 그외는 False 반환
        for i in range(self.UPPER):
            if self.used[i] == False:
                return False
        return True

    def allLowerUsed(self): # LOWER category 전부 사용되을 때 True, 그외는 False 반환
        for i in range (self.UPPER, self.UPPER+self.LOWER) :
            if self.used[i] == False:
                return False
        return True

    def getUsed(self):
        return self.used

    def getTotalScore(self):
        return self.getUpperScore()+self.getLowerScore()


