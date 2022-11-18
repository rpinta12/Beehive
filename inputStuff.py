'''
This file holds all the values that we can use as inputs
numbers are only true for one cycle of the while loop in main
These can be used for a single press action
All other inputs stay true until released

'''

import pygame,sys,os
pygame.init()

inputs = {"LEFT":False,
          "DOWN":False,
          "RIGHT":False,
          "UP":False,
          "SPACE":False,
          "R":False,
          "Z":False,
          "SHIFT":False,
          "1":False,
          "2":False,
          "3":False,}



def updateInputs():
    global inputs
    inputs["1"] = False
    inputs["2"] = False
    inputs["3"] = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                inputs["LEFT"] = True
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                inputs["DOWN"] = True
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                inputs["RIGHT"] = True
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                inputs["UP"] = True
            if event.key == pygame.K_SPACE:
                inputs["SPACE"] = True
            if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                inputs["SHIFT"] = True
            if event.key == pygame.K_r:
                inputs["R"] = True
            if event.key == pygame.K_1:
                inputs["1"] = True
            if event.key == pygame.K_2:
                inputs["2"] = True
            if event.key == pygame.K_3:
                inputs["3"] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                inputs["LEFT"] = False
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                inputs["DOWN"] = False
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                inputs["RIGHT"] = False
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                inputs["UP"] = False
            if event.key == pygame.K_SPACE:
                inputs["SPACE"] = False
            if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                inputs["SHIFT"] = False
            if event.key == pygame.K_r:
                inputs["R"] = False

