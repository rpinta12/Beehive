import sys, pygame, os
import inputStuff
import game

pygame.init()
clock = pygame.time.Clock()


while True:
	#this draws a black screen to reset the screen.  
	pygame.draw.rect(game.screen,'purple',pygame.Rect(0,0,800,600))
	if(game.stage == "start screen"):
		
		game.drawStartScreen(game.screen)


		
		if(inputStuff.inputs["1"]):
			game.stage = "level1"
	elif(game.stage == "level1"):
		game.updatePlayer()
		game.updateEnemies()
		game.updateCollectibles()
		game.drawBackground(game.screen)
		game.drawPlayer(game.screen)
		game.drawEnemies(game.screen)
		game.drawCollectibles(game.screen)

		
		if(inputStuff.inputs["1"]):
			game.stage = "end screen"
	elif(game.stage == "end screen"):
		game.drawEndScreen(game.screen)


		
		if(inputStuff.inputs["1"]):
			
			game.stage = "start screen"


	
	clock.tick(60)
	inputStuff.updateInputs()
	pygame.display.update()
