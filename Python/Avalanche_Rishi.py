import pygame
import time
from Gameboard_Rishi import GameBoard
from Gameboard_Rishi import gameboardheight
from Shape_Rishi import Shape


BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255,255,0)
MAGENTA = (255,0,255)
TURQUOISE = (0,206,209)

if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()
    slowtimedelay=0
    size = (1350, 650)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Avalanche - By Scott King")
    myfont=pygame.font.Font('comicbd.ttf',30)
    hsfont=pygame.font.Font('comicbd.ttf',20)
    shape = Shape(TURQUOISE,False)
    shape2 = Shape(TURQUOISE,True)
    nextshape = Shape(TURQUOISE,False)
    nextshape2 = Shape(TURQUOISE,True)
    gameboard = GameBoard(WHITE,shape.blocklist[0].size)
    gameboard2 = GameBoard(WHITE,shape.blocklist[0].size)
    shape.setgameboard(gameboard)
    shape2.setgameboard(gameboard2)
    nextshape.setgameboard(gameboard)
    nextshape2.setgameboard(gameboard2)
    pygame.mixer.music.load('AvalancheBGM.mp3')
    delay = 0
    delay2 = 0
    delaycount = 3
    pygame.mixer.music.play(-1)
    namelist=[0 for y in range (5)]
    scorelist=[0 for y in range (5)]
    hsfile=open("highscore.txt","r")
    prepare2Player = False
    for i in range(5):
        namelist[i]=hsfile.readline().rstrip('\n')
    for i in range(5):
        scorelist[i]=hsfile.readline().rstrip('\n')
    hsfile.close()
    name=""
    done = False
    started=False
    player2=False

def drawscreen2():
    time.sleep(0.1)
    screen.fill(BLACK)
    shape2.draw(screen)
    nextshape2.drawnextshape2(screen)
    gameboard2.draw2(screen)
    scoretext = myfont.render("Score:" + str(gameboard2.score), 1, WHITE)
    screen.blit(scoretext, (1000, 400))
    linestext = myfont.render("Linescleared:" + str(gameboard2.numoflines), 1, WHITE)
    screen.blit(linestext, (1000, 350))
    leveltext = myfont.render("Level:" + str(gameboard2.level), 1, WHITE)
    screen.blit(leveltext, (1000, 300))
    nextshapetext = myfont.render("Next:", 1, WHITE)
    screen.blit(nextshapetext, (1050, 50))
    pygame.draw.rect(screen, TURQUOISE, [1050, 100, 6 * shape2.blocklist[0].size, 6 * shape2.blocklist[0].size], 1)

    shape.draw(screen)
    nextshape.drawnextshape(screen)
    gameboard.draw(screen)
    scoretext = myfont.render("Score:" + str(gameboard.score), 1, WHITE)
    screen.blit(scoretext, (350, 400))
    linestext = myfont.render("Linescleared:" + str(gameboard.numoflines), 1, WHITE)
    screen.blit(linestext, (350, 350))
    leveltext = myfont.render("Level:" + str(gameboard.level), 1, WHITE)
    screen.blit(leveltext, (350, 300))
    nextshapetext = myfont.render("Next:", 1, WHITE)
    screen.blit(nextshapetext, (400, 50))
    pygame.draw.rect(screen, TURQUOISE, [400, 100, 6 * shape.blocklist[0].size, 6 * shape.blocklist[0].size], 1)
    pygame.display.flip()


def drawscreen():
    time.sleep(0.1)
    screen.fill(BLACK)
    shape.draw(screen)
    nextshape.drawnextshape(screen)
    gameboard.draw(screen)
    scoretext=myfont.render("Score:"+ str(gameboard.score),1,WHITE)
    screen.blit(scoretext,(350,400))
    linestext=myfont.render("Linescleared:"+str(gameboard.numoflines),1,WHITE)
    screen.blit(linestext,(350,350))
    leveltext=myfont.render("Level:"+str(gameboard.level),1,WHITE)
    screen.blit(leveltext, (350, 300))
    nextshapetext=myfont.render("Next:",1,WHITE)
    screen.blit(nextshapetext,(400,50))
    pygame.draw.rect(screen,TURQUOISE,[400,100,6*shape.blocklist[0].size,6*shape.blocklist[0].size],1)
    poweruptext=myfont.render("Power Ups:",1,WHITE)
    screen.blit(poweruptext,(50,525))
    numberofpowerupstext=myfont.render("x"+str(gameboard.numofslowtime),1,WHITE)
    screen.blit(numberofpowerupstext,(285,525))
    slowtime_image=pygame.image.load("clock.png")
    screen.blit(slowtime_image,(225,515))
    numberofpowerupstext = myfont.render("x" + str(gameboard.numofswappiece), 1,WHITE)
    screen.blit(numberofpowerupstext, (435,525))
    swappiece_image = pygame.image.load("swap.png")
    screen.blit(swappiece_image, (375,515))
    highscoretext=myfont.render("Highscore:",1,WHITE)
    screen.blit(highscoretext,(575,50))
    playernametext=myfont.render("player:"+ name,1,WHITE)
    screen.blit(playernametext,(515,525))
    for i in range(5):
        hsnametext=hsfont.render(str(namelist[i]),1,WHITE)
        hsscoretext=hsfont.render(str(scorelist[i]),1,WHITE)
        screen.blit(hsnametext,(600,i*25+125))
        screen.blit(hsscoretext,(700,i*25+125))
    pygame.draw.rect(screen, TURQUOISE, [575,100,200,400], 1)


    pygame.display.flip()

def keyCheck():
    if event.key == pygame.K_LEFT:
        shape.moveLeft()
    elif event.key == pygame.K_RIGHT:
        shape.moveRight()
    elif event.key == pygame.K_DOWN:
        shape.delayCount = 0
    elif event.key == pygame.K_UP:
        shape.rotateCW()
    elif event.key==pygame.K_SPACE:
        gameboard.score+=(gameboardheight-shape.blocklist[0].gridypos)
        shape.drop()
    elif event.key == pygame.K_n and gameboard.numofslowtime>0 and gameboard.slowtimeon==False:
        gameboard.numofslowtime-=1
        gameboard.slowtimeon=True
    elif event.key == pygame.K_m and gameboard.numofswappiece>0 and gameboard.swappieceon==False:
        gameboard.swappieceon=True
        gameboard.numofswappiece-=1

def keyupCheck():
    if event.key == pygame.K_DOWN:
        shape.delayCount = 3

def keyCheck2():
    if event.key == pygame.K_a:
        shape.moveLeft()
    elif event.key == pygame.K_d:
        shape.moveRight()
    elif event.key == pygame.K_s:
        shape.delayCount = 0
    elif event.key == pygame.K_w:
        shape.rotateCW()
    elif event.key==pygame.K_e:
        gameboard.score+=(gameboardheight-shape.blocklist[0].gridypos)
        shape.drop()

    if event.key == pygame.K_LEFT:
        shape2.moveLeft()
    elif event.key == pygame.K_RIGHT:
        shape2.moveRight()
    elif event.key == pygame.K_DOWN:
        shape2.delayCount = 0
    elif event.key == pygame.K_UP:
        shape2.rotateCW()
    elif event.key == pygame.K_KP0:
        gameboard2.score += (gameboardheight - shape2.blocklist[0].gridypos)
        shape2.drop()

def keyupCheck2():
    if event.key == pygame.K_DOWN:
        shape2.delayCount = 3
    if event.key == pygame. K_s:
        shape.delayCount = 3



def checkhighscore():
    newhighscore=False
    tempnamelist=[0 for y in range(5)]
    tempscorelist=[0 for y in range(5)]
    for i in range(5):
            if gameboard.score >int(scorelist[i]) and newhighscore==False:
                tempscorelist[i]=gameboard.score
                tempnamelist[i]=name
                newhighscore = True
            elif newhighscore==True:
                tempscorelist[i]=scorelist[i-1]
                tempnamelist[i]=namelist[i-1]
            else:
                tempscorelist[i]=scorelist[ -1]
                tempnamelist[i]=namelist[i-1]
    for i in range(5):
        scorelist[i]=tempscorelist[i]
        namelist[i]= tempnamelist[i]
    hsfile=open("highscore.txt","w")
    for i in range(5):
            hsfile.write(str(namelist[i])+'\n')
    for i in range(5):
            hsfile.write(str(scorelist[i]) +'\n')

while not started:
    titlescreen_image = pygame.image.load("Backdrop.png")
    pleasetypeyournametext = myfont.render("Please Type Your Name", 1, WHITE)
    screen.blit(pleasetypeyournametext, (230, 200))

    nametext = myfont.render(name, 1, WHITE)
    screen.blit(nametext, (300, 250))
    pygame.display.flip()
    screen.blit(titlescreen_image, (130, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                prepare2Player = not prepare2Player
            if prepare2Player == False:
                player2text = myfont.render("Player 2 Mode", 1, WHITE)
                screen.blit(player2text, (230, 300))
                if event.key >= 33 and event.key <= 126 and len(name) < 10:
                    name = name + chr(event.key)
                if event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                if event.key == pygame.K_RETURN:
                    if name=="":
                        name = "Player 1"
                    started=True
            else:
                player2text = myfont.render("Player 2 Mode", 1, BLUE)
                screen.blit(player2text, (230, 300))

                if event.key == pygame.K_RETURN:
                    player2 = True
                    started = True




if player2==False:
    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            elif event.type == pygame.KEYUP:
                keyupCheck()
            elif event.type == pygame.KEYDOWN:
                keyCheck()


        delay +=1
        if delay>=shape.delayCount:
            shape.falling()
            delay=0
        if shape.active==False:
            gameboard.clearfullRows()
            shape=nextshape
            nextshape=Shape(TURQUOISE,False)
            nextshape.setgameboard(gameboard)
        if gameboard.checkloss():
            checkhighscore()
            slowtimedelay=0
            gameboard=GameBoard(WHITE,shape.blocklist[0].size)
            shape=Shape(BLUE,False)
            shape.setgameboard(gameboard)
            nextshape=Shape(TURQUOISE,False)
            nextshape.setgameboard(gameboard)
        if gameboard.slowtimeon:
            slowtimedelay+=1
            if slowtimedelay>50:
                slowtimedelay=0
                gameboard.slowtime=False
        if gameboard.swappieceon:
            shape=nextshape
            nextshape=Shape(BLUE)
            gameboard.swappieceon=False
        drawscreen()
        time.sleep(0.11-gameboard.level*0.01 + gameboard.slowtimeon*0.1)

else:
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            elif event.type == pygame.KEYDOWN:
                keyCheck2()
            elif event.type == pygame.KEYUP:
                keyupCheck2()

        delay += 1
        if delay >= shape.delayCount:
            shape.falling()
            delay = 0
        delay2 += 1
        if delay2 >= shape2.delayCount:
            shape2.falling()
            delay2 = 0
        if shape.active == False:
            trashrows=gameboard.clearfullRows()
            for i in range(trashrows):
                gameboard2.addtrash()
            shape = nextshape
            nextshape = Shape(TURQUOISE, False)
            nextshape.setgameboard(gameboard)
        if gameboard.checkloss():
            gameboard = GameBoard(WHITE, shape.blocklist[0].size)
            shape = nextshape
            shape.setgameboard(gameboard)
            nextshape = Shape(TURQUOISE,False)
            nextshape.setgameboard(gameboard)
        if shape2.active == False:
            trashrows=gameboard2.clearfullRows()
            for i in range(trashrows):
                gameboard.addtrash()
            shape2 = nextshape2
            nextshape2 = Shape(TURQUOISE, True)
            nextshape2.setgameboard(gameboard2)
        if gameboard2.checkloss():
            gameboard2 = GameBoard(WHITE, shape.blocklist[0].size)
            shape2 = nextshape2
            shape2.setgameboard(gameboard2)
            nextshape2 = Shape(TURQUOISE,True)
            nextshape2.setgameboard(gameboard2)
        drawscreen2()
        time.sleep(0.11 - gameboard.level * 0.01 + gameboard.slowtimeon * 0.1)
