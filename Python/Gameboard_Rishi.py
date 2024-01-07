import pygame
import random
BLACK=(0,   0,   0)
gameboardwidth=12
gameboardheight=20


class GameBoard():
    def __init__(self,color,blocksize):
        self.boardercolor=color
        self.multiplier=blocksize
        self.score=0
        self.numoflines=0
        self.levelcount=0
        self.level=0
        self.slowtimeon=False
        self.numofslowtime=0
        self.swappieceon=False
        self.numofswappiece=0
        self.activeBoardspot=[[0 for y in range (gameboardheight)]for x in range(gameboardwidth)]
        self.activeBoardcolor=[[0 for y in range (gameboardheight)]for x in range(gameboardwidth)]
        for i in range(gameboardwidth):
            for j in range(gameboardheight):
                self.activeBoardspot[i][j] = False
                self.activeBoardcolor[i][j] = (0,0,0)
    def draw(self,screen):
        pygame.draw.rect(screen, self.boardercolor,[0, 0, gameboardwidth * self.multiplier, gameboardheight * self.multiplier],1)
        for i in range(gameboardwidth):
            for j in range(gameboardheight):
                if self.activeBoardspot[i][j]:
                    pygame.draw.rect(screen,self.activeBoardcolor[i][j],[i*self.multiplier, j*self.multiplier,self.multiplier-1,self.multiplier-1],0)

    def draw2(self, screen):
        pygame.draw.rect(screen, self.boardercolor,[650, 0, gameboardwidth * self.multiplier, gameboardheight * self.multiplier], 1)
        for i in range(gameboardwidth):
            for j in range(gameboardheight):
                if self.activeBoardspot[i][j]:
                    pygame.draw.rect(screen, self.activeBoardcolor[i][j],[i * self.multiplier +650, j * self.multiplier, self.multiplier - 1,self.multiplier - 1], 0)

    def checkloss(self):
        for i in range(gameboardwidth):
            if self.activeBoardspot[i][0]:
                return True
        return False

    def isCompleteLine(self,rowNum):
        for i in range(gameboardwidth):
            if self.activeBoardspot[i][rowNum]== False:
                return False
        return True

    def clearfullRows(self):
        currentlinecount =0
        for i in range(gameboardheight):
            if self.isCompleteLine(i):
                self.score +=100
                self.numoflines +=1
                self.levelcount +=1
                currentlinecount +=1
                if self.levelcount==10:
                    self.level+=1
                    self.levelcount=0
                    self.numofslowtime+=1
                    self.numofswappiece+=1
                for c in range(i,1,-1):
                    for j in range(gameboardwidth):
                        self.activeBoardspot[j][c]=self.activeBoardspot[j][c-1]
                        self.activeBoardcolor[j][c]=self.activeBoardcolor[j][c-1]
                for r in range(gameboardwidth):
                    self.activeBoardspot[r][0]=False
                    self.activeBoardcolor[r][0]=BLACK
        return currentlinecount-1

    def addtrash(self):
        for c in range(gameboardheight-1):
            for j in range(gameboardwidth):
                self.activeBoardspot[j][c]=self.activeBoardspot[j][c+1]
                self.activeBoardcolor[j][c]=self.activeBoardcolor[j][c+1]
        randomremove=random.randrange(12)

        for r in range(gameboardwidth):
            if r != randomremove:

                self.activeBoardspot[r][gameboardheight-1]=True
                self.activeBoardcolor[r][gameboardheight-1]=(255,255,255)
            else:
                self.activeBoardspot[r][gameboardheight-1] = False
                self.activeBoardcolor[r][gameboardheight-1] = BLACK








