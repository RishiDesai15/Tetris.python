import random
from Block_Rishi import Block
from  Gameboard_Rishi import gameboardheight
from  Gameboard_Rishi import gameboardwidth
import pygame

BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,191,255)
YELLOW = (255,255,0)
MAGENTA = (255,0,255)
TURQUOISE = (0,206,209)
ORANGE = (255,165,0)
MAROON = (128,0,0)



ZSHAPE=[[(gameboardwidth/2)-1,0],[(gameboardwidth/2)-2,0],[(gameboardwidth/2)-1,1],[gameboardwidth/2, 1]]
SSHAPE=[[(gameboardwidth/2)-1,0],[gameboardwidth/2,0],[(gameboardwidth/2)-2,1],[(gameboardwidth/2)-1,1]]
LINESHAPE=[[(gameboardwidth/2)-1,0],[(gameboardwidth/2)-2,0],[(gameboardwidth/2),0],[(gameboardwidth/2)+1,0]]
SQUARESHAPE=[[(gameboardwidth/2)-1,0],[gameboardwidth/2,0],[gameboardwidth/2,1],[(gameboardwidth/2)-1,1]]
LSHAPE=[[(gameboardwidth/2)-1,1],[(gameboardwidth/2)-1,0],[(gameboardwidth/2)-1,2],[(gameboardwidth/2),2]]
JSHAPE=[[(gameboardwidth/2),1],[gameboardwidth/2,0],[(gameboardwidth/2),2],[(gameboardwidth/2)-1,2]]
TSHAPE=[[(gameboardwidth/2)-1,1],[(gameboardwidth/2)-1,0],[(gameboardwidth/2),1],[(gameboardwidth/2)-2,1]]
FIVELINESHAPE=[[(gameboardwidth/2)-1,0],[(gameboardwidth/2)-2,0],[(gameboardwidth/2),0],[(gameboardwidth/2)+1,0],[(gameboardwidth/2)+2,0]]
RECTSHAPE=[[(gameboardwidth/2)-1,0],[gameboardwidth/2,0],[gameboardwidth/2,1],[(gameboardwidth/2)-1,1],[(gameboardwidth/2)-1,2],[gameboardwidth/2,2]]

ALLSHAPES = [ZSHAPE,SSHAPE,LINESHAPE,SQUARESHAPE,LSHAPE,JSHAPE,TSHAPE,FIVELINESHAPE,RECTSHAPE]
ALLCOLOURS = [WHITE,GREEN,RED,BLUE,YELLOW,MAGENTA,TURQUOISE,ORANGE,MAROON]

class Shape():
    def __init__(self,color, player2):
        self.active = True
        randomNum=random.randrange(9)
        self.color = ALLCOLOURS[randomNum]
        self.shape=ALLSHAPES[randomNum]
        self.numblocks = len(self.shape)
        self.blocklist=[]
        self.player2=player2
        self.delayCount = 3

        for i in range(self.numblocks):
            self.blocklist.append(Block(self.color,self.shape[i][0],self.shape[i][1]))

    def draw(self,screen):
        for i in range(self.numblocks):
            self.blocklist[i].draw(screen,self.player2)

    def setgameboard(self, gameboard):
        self.gameboard=gameboard

    def moveLeft(self):
        blocked= False
        for i in range (self.numblocks):
            if (self.blocklist[i].gridxpos == 0 or  self.gameboard.activeBoardspot[self.blocklist[i].gridxpos-1][self.blocklist[i].gridypos]):
                blocked= True
        if blocked== False:
            for i in range (self.numblocks):
                self.blocklist[i].gridxpos -=1

    def moveRight(self):
        blocked= False
        for i in range (self.numblocks):
            if (self.blocklist[i].gridxpos == gameboardwidth-1 or  self.gameboard.activeBoardspot[self.blocklist[i].gridxpos+1][self.blocklist[i].gridypos]):
                blocked= True
        if blocked== False:
            for i in range(self.numblocks):
                self.blocklist[i].gridxpos +=1

    def moveDown(self):
        blocked = False
        for i in range(self.numblocks):
            if (self.blocklist[i].gridypos == gameboardheight - 1 or  self.gameboard.activeBoardspot[self.blocklist[i].gridxpos][self.blocklist[i].gridypos+1]):
                blocked = True
        if blocked == False:
            for i in range(self.numblocks):
                self.blocklist[i].gridypos += 1

    def moveUp(self):
        blocked = False
        for i in range(self.numblocks):
            if (self.blocklist[i].gridypos == 0 or  self.gameboard.activeBoardspot[self.blocklist[i].gridxpos+1][self.blocklist[i].gridypos]):
                blocked = True
        if blocked == False:
            for i in range(self.numblocks):
                self.blocklist[i].gridypos -= 1

    def rotateCW(self):
        if self.shape!=SQUARESHAPE:
            newBlockx = [0,0,0,0,0,0,0,0]
            newBlocky = [0,0,0,0,0,0,0,0]
            canrotate = True
            for i in range (self.numblocks):
                newBlockx[i]= -(self.blocklist[i].gridypos-self.blocklist[0].gridypos)+self.blocklist[0].gridxpos
                newBlocky[i]= (self.blocklist[i].gridxpos-self.blocklist[0].gridxpos)+self.blocklist[0].gridypos
                if newBlockx[i]<0 or newBlockx[i]>=gameboardwidth:
                    canrotate= False
                elif newBlocky[i]<0 or newBlocky[i]>=gameboardheight:
                    canrotate= False
                elif  self.gameboard.activeBoardspot[newBlockx[i]][newBlocky[i]]:
                    canrotate= False
            if canrotate:
                for i in range(self.numblocks):
                    self.blocklist[i].gridxpos=newBlockx[i]
                    self.blocklist[i].gridypos=newBlocky[i]

    def rotateCC(self):
        if self.shape!=SQUARESHAPE:
            newBlockx = [0,0,0,0,0]
            newBlocky = [0,0,0,0,0]
            canrotate = True
            for i in range (self.numblocks):
                newBlockx[i]= (self.blocklist[i].gridypos-self.blocklist[0].gridypos)+self.blocklist[0].gridxpos
                newBlocky[i]= -(self.blocklist[i].gridxpos-self.blocklist[0].gridxpos)+self.blocklist[0].gridypos
                if newBlockx[i]<0 or newBlockx[i]>=gameboardwidth:
                    canrotate= False
                elif newBlocky[i]<0 or newBlocky[i]>=gameboardheight:
                    canrotate= False
                elif  self.gameboard.activeBoardspot[newBlockx[i]][newBlocky[i]]:
                    canrotate= False
            if canrotate:
                for i in range(self.numblocks):
                    self.blocklist[i].gridxpos=newBlockx[i]
                    self.blocklist[i].gridypos=newBlocky[i]

    def falling(self):
        for i in range(self.numblocks):
            if self.blocklist[i].gridypos==gameboardheight-1 or self.gameboard.activeBoardspot[self.blocklist[i].gridxpos][self.blocklist[i].gridypos+1]:
                self.hitbottom()
        for i in range(self.numblocks):
            if self.active:
                self.blocklist[i].gridypos +=1

    def hitbottom(self):
        for i in range(self.numblocks):
            self.gameboard.activeBoardspot[self.blocklist[i].gridxpos][self.blocklist[i].gridypos] = True
            self.gameboard.activeBoardcolor[self.blocklist[i].gridxpos][self.blocklist[i].gridypos] = self.blocklist[i].colour
        self.active=False



    def drop(self):
        while self.active:
            for i in range(self.numblocks):
                if self.blocklist[i].gridypos==gameboardheight-1 or  self.gameboard.activeBoardspot[self.blocklist[i].gridxpos][self.blocklist[i].gridypos+1]:
                    self.hitbottom()
            for i in range(self.numblocks):
                if self.active:
                    self.blocklist[i].gridypos+=1

    def drawnextshape(self,screen):
        for i in range(self.numblocks):
            pygame.draw.rect(screen,self.blocklist[i].colour,[self.blocklist[i].gridxpos*self.blocklist[i].size+325,self.blocklist[i].gridypos*self.blocklist[i].size+150,self.blocklist[i].size-1,self.blocklist[i].size-1],0)

    def drawnextshape2(self,screen):
        for i in range(self.numblocks):
            pygame.draw.rect(screen,self.blocklist[i].colour,[self.blocklist[i].gridxpos*self.blocklist[i].size+975,self.blocklist[i].gridypos*self.blocklist[i].size+150,self.blocklist[i].size-1,self.blocklist[i].size-1],0)