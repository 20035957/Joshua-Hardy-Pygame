import pygame
import sys
import random

pygame.init()
clock = pygame.time.Clock()
FPS = 60
SCREENSIZE = SCREENWIDTH, SCREENHEIGHT = 1000, 800
screen = pygame.display.set_mode(SCREENSIZE)

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)

player1Image = pygame.image.load("player1.png")
player1XY = [100, 100]
player1ImageSizeXY = [80, 60]
player1Image = pygame.transform.scale(player1Image, player1ImageSizeXY)
fireLock = 0

target1Image = pygame.image.load("target1.png")
target1XY = [500, 500]
target1ImageSizeXY = target1ImageSizeX, target1ImageSizeY = 80, 60
target1Image = pygame.transform.scale(target1Image, target1ImageSizeXY)

pygame.mouse.set_visible(False)
gameState = "running"
while gameState != "exit":

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameState = "exit"
        if event.type == pygame.MOUSEBUTTONDOWN:
            fireLock = 1

        screen.fill(black)
        mousePosition = pygame.mouse.get_pos()
        newXPosition = mousePosition[0] - (player1ImageSizeXY[0] / 2)
        newYPosition = mousePosition[1] - (player1ImageSizeXY[1] / 2)
        player1XY = newXPosition, newYPosition
        player1 = screen.blit(player1Image, player1XY)
        target = screen.blit(target1Image, target1XY)

        if player1.colliderect(target) and fireLock == 1:
            #print("Hit!")
            target1XY[0] = random.randint(0, (SCREENWIDTH - target1ImageSizeX))
            target1XY[1] = random.randint(0, (SCREENHEIGHT - target1ImageSizeY))
            fireLock = 0

    pygame.display.flip()
    clock.tick(FPS)

print("The game has closed")
pygame.quit()
sys.exit()
