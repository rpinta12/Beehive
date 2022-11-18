import pygame
import inputStuff
pygame.init()

#-------------------------------------INITIAL SETUP
stage = "start screen"

width = 800
height = 600

#github test


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('HONEY ADVENTURES')


#-------------------------------------LEVELS, WORLD, AND MAP-----------------------------------
#----------------VARIABLES
#Text/Images for Start Screen
fontStartScreen = pygame.font.Font('freesansbold.ttf', 60)
textStartScreen1 = fontStartScreen.render('Welcome to the Beehive', True, 'black', 'yellow')
textStartScreen2 = fontStartScreen.render('Press 1 To Start', True, 'black', 'yellow')
#Text/Images For End Screen
textEndScreen1 = fontStartScreen.render('GAME OVER', True, 'black', 'yellow')
textEndScreen2 = fontStartScreen.render('Press 1 To RESTART', True, 'black', 'yellow')

#Text/Images/Rects for Main game window(background, walls, score,...)
backgroundImage = pygame.image.load("pics/background.png")
backgroundImage = pygame.transform.scale(backgroundImage,(800,600))


#----------------Functions
def drawStartScreen(screen):
	screen.blit(textStartScreen1,(60,200))
	screen.blit(textStartScreen2, (100, 300))

def drawBackground(screen):
    screen.blit(backgroundImage,(0,0))
	
def drawEndScreen(screen):
    screen.blit(textEndScreen1,(150,200))
    screen.blit(textEndScreen2, (30, 300))

#-------------------------------------PLAYER-----------------------------------
#----------------VARIABLES
playerImage = pygame.image.load("pics/hero.png")
playerImage = pygame.transform.scale(playerImage,(80,60)).convert_alpha()
playerImage = pygame.transform.flip(playerImage,True,False)
player = playerImage.get_rect(topleft = (200,200))
playerSpeed = 3
playerVelX = 0
playerVelY = 0
playerHealth = 5


#----------------Functions
def drawPlayer(screen):
    screen.blit(playerImage,player)
def updatePlayer():
    #any variable you change from above need to be referenced as global here
    global playerVelX, playerVelX, playerHealth
    if (inputStuff.inputs["UP"]):
        playerVelY = -playerSpeed
    elif(inputStuff.inputs["DOWN"]):
        playerVelY = playerSpeed
    else:
        playerVelY = 0
    player.y += playerVelY

    if (inputStuff.inputs["LEFT"]):
        playerVelX = -playerSpeed
    elif(inputStuff.inputs["RIGHT"]):
        playerVelX = playerSpeed
    else:
        playerVelX = 0
    player.x += playerVelX





#-------------------------------------ENEMY-----------------------------------
#----------------VARIABLES



#----------------Functions





#-------------------------------------COLLECTIBLES-----------------------------------
#----------------VARIABLES



#----------------Functions





