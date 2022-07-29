import pygame
from pygame.locals import *
import random

pygame.init()

WIDTH = 800
HEIGHT = 600

running = True

screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption("Pongy")

back = pygame.Surface((WIDTH, HEIGHT))
background = back.convert()
background.fill((255,255,255))

class Player():
    x = 0
    y = 0
    speed = 250.0
    move = 0
    score = 0
    height = 76
    width = 10
    image = pygame.Surface((width, height)).convert()
    image.fill((0,0,255))


player1 = Player()
player2 = Player()

player1.x = 10
player1.y = HEIGHT/2 - player1.height/2

player2.x = WIDTH - 10 - player2.width
player2.y = HEIGHT/2 - player2.height/2





while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
    screen.blit(background, (0,0))
    pygame.draw.rect(screen, (255,255,255), Rect((5,5), (WIDTH - 10, HEIGHT - 10)), 2)
    pygame.draw.aaline(screen, (255,255,255), (int(WIDTH/2), 5), ((int(WIDTH/2), HEIGHT - 5)))

    screen.blit(player1.image, (player1.x, player1.y))
    screen.blit(player1.image, (player2.x, player2.y))

    pygame.display.update()
    


pygame.quit()
