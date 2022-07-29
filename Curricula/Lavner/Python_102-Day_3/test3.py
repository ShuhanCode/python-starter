import pygame, sys
from pygame.locals import *
 
pygame.init()
 
WIDTH = 500
HEIGHT = 400
 
running = True
clock = pygame.time.Clock()
 
window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption("Python is cool!")
window.fill((255,255,255))
 
back = pygame.Surface((WIDTH, HEIGHT))
background = back.convert()
background.fill((255, 255, 255))

class Player():
    size = 20


    speed = 250
    move = 0
    movey = 0
    height = 50
    width = 100

    x = WIDTH/2 - size/2
    y = HEIGHT - height

    image = pygame.Surface((width, height)).convert()
    image.fill((0, 255, 255))

player = Player()
 
while running:
    window.blit(background, (0, 0))
    pygame.draw.polygon(window, (0,255,0), ((146, 0), (291, 106), (236, 277), (56,277), (0,106)))
 
    pygame.draw.line(window, (0,0,255), (60,60),(120,60), 4)
    pygame.draw.line(window, (0,0,255), (120,60), (60,120))
    pygame.draw.line(window, (0,0,255), (60,120), (120,120), 4)
 
    basicFont = pygame.font.SysFont(None, 48)
    text = basicFont.render("Python is cool", True, (255, 255, 255), (0,0,255))
    textRect = text.get_rect()
    textRect.centerx = window.get_rect().centerx
    textRect.centery = window.get_rect().centery
    window.blit(text, textRect)

    window.blit(player.image, (player.x, player.y))


    timePassed = clock.tick(30)
    timeSec = timePassed / 1000.0

    player.x += player.move * timeSec
    player.y += player.movey * timeSec 
 
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT:
                player.move = player.speed
            elif event.key == K_LEFT:
                player.move = -player.speed
            elif event.key == K_UP:
                player.movey = -player.speed
            elif event.key == K_DOWN:
                player.movey = player.speed
        elif event.type == KEYUP:
            if event.key == K_LEFT or K_RIGHT:
                player.move = 0
            if event.key == K_UP or K_DOWN:
                player.movey = 0
               
        
pygame.quit()
sys.exit()
