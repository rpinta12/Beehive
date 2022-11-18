import pygame
pygame.init()

#-------------------------------------INITIAL SETUP
stage = "start screen"

width = 800
height = 600



screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('HONEY ADVENTURES')


#-------------------------------------LEVELS, WORLD, AND MAP
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

#-------------------------------------PLAYER
#----------------VARIABLES



#----------------Functions






#-------------------------------------ENEMY
#----------------VARIABLES



#----------------Functions





#-------------------------------------COLLECTIBLES
#----------------VARIABLES



#----------------Functions





