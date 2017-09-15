#!/usr/bin/env python3

import pygame, time
from characters.Mosquito import Mosquito
# GLOBALS
W_WIDTH = 640
W_HEIGHT = 480

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = 0
clock = 0
mainFont = 0
fontTahoma = 0
xOffset = 0
yOffset = 0
appAlive = False
mosquito = Mosquito()
mosquito.x = 100
mosquito.y = 100
bgImage = 0


def initApp():
    """Initialize app"""
    global screen, appAlive, clock, mainFont, bgImage, fontTahoma

    pygame.init()
    pygame.display.set_caption("Blood Frenzy")

    fontTahoma = pygame.font.SysFont('Tahoma', 16, False, False)

    clock = pygame.time.Clock()
    mainFont = pygame.font.SysFont('Tahoma', 16, False, False)
    size = (W_WIDTH, W_HEIGHT)
    screen = pygame.display.set_mode(size)
    bgImage = pygame.image.load("resources/gfx/background.png").convert()
    mosquito.image = pygame.image.load("resources/gfx/mosquito.png").convert()
    screen.fill(BLACK)
    screen.blit(bgImage, (0,0))
    pygame.display.flip()
    appAlive = True

colors = [BLACK, WHITE, RED, GREEN, BLUE]
colorLength = len(colors)
colorIndex = 0
keys_pressed = {
    pygame.K_RIGHT: False, 
    pygame.K_LEFT: False, 
    pygame.K_UP: False, 
    pygame.K_DOWN: False, 
}
TIME_MODIFIER = 0.2

initApp()
while appAlive:
    screen.fill(BLACK)
    screen.blit(bgImage, (0,0))
    time = clock.get_time()*TIME_MODIFIER
#    print("Frame time: %s"%time)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            appAlive = False
        elif event.type == pygame.KEYDOWN:
            if event.key in keys_pressed:
                keys_pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            if event.key in keys_pressed:
                keys_pressed[event.key] = False
        if keys_pressed[pygame.K_RIGHT]:
            mosquito.acc_x = 1
        elif keys_pressed[pygame.K_LEFT]:
            mosquito.acc_x = -1
        else:
            mosquito.acc_x = 0

        if keys_pressed[pygame.K_UP]:
            mosquito.acc_y = -1
        elif keys_pressed[pygame.K_DOWN]:
            mosquito.acc_y = 1
        else:
            mosquito.acc_y = 0
        
    mosquito.updateForTime(time)
    screen.blit(mosquito.image, (mosquito.x,mosquito.y))
    #InfoText = fontTahoma.render("DBG: Y: " + str(yOffset) + " X: " + str(xOffset), True, BLACK)
    # screen.blit(InfoText, [W_WIDTH - 132, W_HEIGHT - 30])
    
    pygame.display.flip()
    clock.tick()

pygame.quit()
