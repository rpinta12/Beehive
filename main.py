import sys, pygame, os
import inputStuff
import game

pygame.init()
clock = pygame.time.Clock()


while True:
	#this draws a purple screen to reset the screen.  
	pygame.draw.rect(game.screen,'purple',pygame.Rect(0,0,800,600))
	if(game.stage == "start screen"):
		pass
	elif(game.stage == "level1"):
		pass
	elif(game.stage == "end screen"):
		pass

	
	clock.tick(60)
	inputStuff.updateInputs()
	pygame.display.update()
