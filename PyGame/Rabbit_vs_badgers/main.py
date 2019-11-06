#Importing required libraries
import math
import pygame
from pygame.locals import *

#Initializing the game
pygame.init()
height, width = 480, 640
screen = pygame.display.set_mode((width, height))

#Setting key response functionality
keys = [False, False, False, False]
player_position = [150,240]

#Loading images
player = pygame.image.load("C:/Personal/Codes/Github/Games/PyGame/Rabbit_vs_badgers/resources/images/dude.png")
grass = pygame.image.load("C:/Personal/Codes/Github/Games/PyGame/Rabbit_vs_badgers/resources/images/grass.png")
castle = pygame.image.load("C:/Personal/Codes/Github/Games/PyGame/Rabbit_vs_badgers/resources/images/castle.png")

#Loop
while 1:
    #Refreshing screen
    screen.fill(0)
    
    #Drawing elements
    #Grass
    for x in range(int(width/grass.get_width())+1):
        for y in range(int(height/grass.get_height())+1):
            screen.blit(grass, (x*100, y*100))
    
    #Player
    position = pygame.mouse.get_pos()
    angle = math.atan2(position[1]-(player_position[1]+32),position[0]-(player_position[0]+26))
    player_rotation = pygame.transform.rotate(player, 360-angle*57.29)
    player_position1 = (player_position[0]-player_rotation.get_rect().width/2, player_position[1]-player_rotation.get_rect().height/2)
    screen.blit(player_rotation, player_position1)

    #Castle
    screen.blit(castle, (0,30))
    screen.blit(castle, (0,135))
    screen.blit(castle, (0,240))
    screen.blit(castle, (0,345))
    #Updating screen
    pygame.display.flip()
    #Event loop
    for event in pygame.event.get():
        #Check if the event is the X button 
        if event.type==pygame.QUIT:
            #if True, quit game
            pygame.quit() 
            exit(0)
        
        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                keys[0] = True
            if event.key == K_a:
                keys[1] = True
            if event.key == K_s:
                keys[2] = True
            if event.key == K_d:
                keys[3] = True
        if event.type == pygame.KEYUP:
            if event.key == K_w:
                keys[0] = False
            if event.key == K_a:
                keys[1] = False
            if event.key == K_s:
                keys[2] = False
            if event.key == K_d:
                keys[3] = False

    if keys[0]:
        player_position[1] -= 5
    elif keys[2]:
        player_position[1] += 5
    if keys[1]:
        player_position[0] -= 5
    elif keys[3]:
        player_position[0] += 5