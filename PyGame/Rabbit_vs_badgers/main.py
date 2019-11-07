#Importing required libraries
import math
import random
import pygame
from pygame.locals import *

#Initializing the game
pygame.init()
height, width = 480, 640
screen = pygame.display.set_mode((width, height)) #setting dimensions for the screen
pygame.mixer.init() #Initializing audio

#Setting key response functionality
keys = [False, False, False, False] #initial state of WASD keys in that order
player_position = [150,240] #initial player position

#Shooting
accuracy = [0,0] #Player accuracy -> [Shots fired, Shots that hit the targets]
arrows = []

#Enemies
badtimer=100
badtimer1=0
badguys=[[640,100]]
healthvalue=194

#Loading images
player = pygame.image.load("C:/Personal/Codes/Github/Games/PyGame/Rabbit_vs_badgers/resources/images/dude.png")
grass = pygame.image.load("C:/Personal/Codes/Github/Games/PyGame/Rabbit_vs_badgers/resources/images/grass.png")
castle = pygame.image.load("C:/Personal/Codes/Github/Games/PyGame/Rabbit_vs_badgers/resources/images/castle.png")
arrow = pygame.image.load("C:/Personal/Codes/Github/Games/PyGame/Rabbit_vs_badgers/resources/images/bullet.png")

badguyimg1 = pygame.image.load("C:/Personal/Codes/Github/Games/PyGame/Rabbit_vs_badgers/resources/images/badguy.png")
badguyimg=badguyimg1

healthbar = pygame.image.load("C:/Personal/Codes/Github/Games/PyGame/Rabbit_vs_badgers/resources/images/healthbar.png")
health = pygame.image.load("C:/Personal/Codes/Github/Games/PyGame/Rabbit_vs_badgers/resources/images/health.png")

gameover = pygame.image.load("C:/Personal/Codes/Github/Games/PyGame/Rabbit_vs_badgers/resources/images/gameover.png")
youwin = pygame.image.load("C:/Personal/Codes/Github/Games/PyGame/Rabbit_vs_badgers/resources/images/youwin.png")

#Loading Audio
hit = pygame.mixer.Sound("C:/Personal/Codes/Github/Games/PyGame/Rabbit_vs_badgers/resources/audio/explode.wav")
enemy = pygame.mixer.Sound("C:/Personal/Codes/Github/Games/PyGame/Rabbit_vs_badgers/resources/audio/enemy.wav")
shoot = pygame.mixer.Sound("C:/Personal/Codes/Github/Games/PyGame/Rabbit_vs_badgers/resources/audio/shoot.wav")
hit.set_volume(0.05)
enemy.set_volume(0.05)
shoot.set_volume(0.05)
pygame.mixer.music.load('C:/Personal/Codes/Github/Games/PyGame/Rabbit_vs_badgers/resources/audio/moonlight.wav')
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.25)

#Game loop
running = 1
exitcode = 0
while running:
    badtimer-=1
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

    #Arrows
    for bullet in arrows:
        index=0
        velx=math.cos(bullet[0])*10
        vely=math.sin(bullet[0])*10
        bullet[1]+=velx
        bullet[2]+=vely
        if bullet[1]<-64 or bullet[1]>640 or bullet[2]<-64 or bullet[2]>480:
            arrows.pop(index)
        index+=1
        for projectile in arrows:
            arrow1 = pygame.transform.rotate(arrow, 360-projectile[0]*57.29)
            screen.blit(arrow1, (projectile[1], projectile[2]))

    #Enemies
    if badtimer==0:
        badguys.append([640, random.randint(50,430)])
        badtimer=100-(badtimer1*2)
        if badtimer1>=35:
            badtimer1=35
        else:
            badtimer1+=5
    index=0
    for badguy in badguys:
        if badguy[0]<-64:
            badguys.pop(index)
        badguy[0]-=7
        #Castle attack
        badrect=pygame.Rect(badguyimg.get_rect())
        badrect.top=badguy[1]
        badrect.left=badguy[0]
        if badrect.left<64:
            hit.play()
            healthvalue -= random.randint(5,20)
            badguys.pop(index)
        index1=0
        for bullet in arrows:
            bullrect=pygame.Rect(arrow.get_rect())
            bullrect.left=bullet[1]
            bullrect.top=bullet[2]
            if badrect.colliderect(bullrect):
                enemy.play()
                accuracy[0]+=1
                badguys.pop(index)
                arrows.pop(index1)
            index1+=1
        #Next enemy
        index+=1
    for badguy in badguys:
        screen.blit(badguyimg, badguy)

    #Game timer display
    font = pygame.font.Font(None, 24)
    survivedtext = font.render(str((90000-pygame.time.get_ticks())/60000)+":"+str((90000-pygame.time.get_ticks())/1000%60).zfill(2), True, (0,0,0))
    textRect = survivedtext.get_rect()
    textRect.topright=[635,5]
    screen.blit(survivedtext, textRect)


    #Health Bar
    screen.blit(healthbar, (5,5))
    for health1 in range(healthvalue):
        screen.blit(health, (health1+8,8))

    
    
    #Updating screen
    pygame.display.flip()
    
    #Event loop
    for event in pygame.event.get():
        #Check if the event is the X button 
        if event.type==pygame.QUIT:
            #if True, quit game
            pygame.quit() 
            exit(0)
        
        #WASD key responses for movement
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

        #Firing functionality
        if event.type==pygame.MOUSEBUTTONDOWN:
            shoot.play()
            position=pygame.mouse.get_pos()
            accuracy[1]+=1
            arrows.append([math.atan2(position[1]-(player_position1[1]+32),position[0]-(player_position1[0]+26)),player_position1[0]+32,player_position1[1]+32])

    #Player movements using WASD keys
        #Limiting displays so that player does not go off the screen
    #W
    if keys[0]:
        player_position[1] -= 5
        if player_position[1] <25:
            player_position[1] = 25
    #S
    elif keys[2]:
        player_position[1] += 5
        if player_position[1] >450:
            player_position[1] = 450
    #A
    if keys[1]:
        player_position[0] -= 5
        if player_position[0] <130:
            player_position[0] = 130
    #D
    elif keys[3]:
        player_position[0] += 5
        if player_position[0] >600:
            player_position[0] = 600

    #Win/Lose check
    if pygame.time.get_ticks()>=90000:
        running=0
        exitcode=1
    if healthvalue<=0:
        running=0
        exitcode=0
    if accuracy[1]!=0:
        accuracyScore=accuracy[0]*1.0/accuracy[1]*100
    else:
        accuracyScore=0

# 11 - Win/lose display        
if exitcode==0:
    pygame.font.init()
    font = pygame.font.Font(None, 24)
    text = font.render("Accuracy: "+str(accuracyScore)+"%", True, (255,0,0))
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery+24
    screen.blit(gameover, (0,0))
    screen.blit(text, textRect)
else:
    pygame.font.init()
    font = pygame.font.Font(None, 24)
    text = font.render("Accuracy: "+str(accuracyScore)+"%", True, (0,255,0))
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery+24
    screen.blit(youwin, (0,0))
    screen.blit(text, textRect)
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    pygame.display.flip()
