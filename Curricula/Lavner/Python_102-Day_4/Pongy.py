import pygame
from pygame.locals import *
import random

pygame.init()

WIDTH = 800
HEIGHT = 600

running = True
paused = True
clock = pygame.time.Clock()
font = pygame.font.SysFont("calibri", 40)

screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption("Pong")

back = pygame.Surface((WIDTH, HEIGHT))
background = back.convert()
background.fill((0,0,0))

class Player():
    x = 0
    y = 0
    speed = 250.0
    move = 0
    score = 0
    height = 100
    width = 10
    image = pygame.Surface((width, height)).convert()
    image.fill((0,0,255))

class Ball():
    size = 16
    x = WIDTH/2 - size/2
    y = HEIGHT/2 - size/2
    xMove = 250
    yMove = 250
    image = pygame.Surface((size,size))
    pygame.draw.circle(image, (0,255,0), (int(size/2), int(size/2)), int(size/2))
    image = image.convert()


player1 = Player()
player2 = Player()
ball = Ball()




player1.x = 10
player1.y = HEIGHT/50 - player1.height/50

player2.x = WIDTH - 10 - player2.width
player2.y = HEIGHT/2 - player2.height/2




while running:

    timePassed = clock.tick(30)
    timeSec = timePassed/1000.0

    if not paused:
        player1.y += player1.move * timeSec
        player2.y += player2.move * timeSec
        ball.x += ball.xMove * timeSec
        ball.y += ball.yMove * timeSec

    if player1.y >= HEIGHT - player1.height - 50:
        player1.y =  HEIGHT - player1.height - 50
    elif player1.y <= 50:
        player1.y = 50
    if player2.y >= HEIGHT - player2.height - 10:
        player2.y =  HEIGHT - player2.height - 10
    elif player2.y <= 10:
        player2.y = 10

    if ball.y <= 10.0:
        ball.yMove = -ball.yMove
        ball.y = 10.0
    elif ball.y >= HEIGHT - 10 - ball.size:
        ball.yMove = -ball.yMove
        ball.y = HEIGHT - 10 - ball.size

    if ball.x <= player1.x + player1.width:
        if ball.y + ball.size >= player1.y and ball.y <= player1.y + player1.height:
            ball.xMove = -ball.xMove
            ball.x = player1.x + player1.width + 5
    if ball.x + ball.size >= player2.x:
        if ball.y + ball.size >= player2.y and ball.y <= player2.y + player2.height:
            ball.xMove = -ball.xMove
            ball.x = player2.x - player2.width - 5


    if ball.x < 5.0:
        player2.score += 1
    elif ball.x > WIDTH - 5 - ball.size:
        player1.score += 1
    if ball.x < 5.0 or ball.x > WIDTH - 5 - ball.size:
        ball.x = WIDTH/2 - ball.size/2
        ball.y = HEIGHT/2 - ball.size/2
        player1.y = HEIGHT/2 - player1.height/2
        player2.y = HEIGHT/2 - player2.height/2
        paused = True
    
    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_w:
                player1.move = -player1.speed
            elif event.key == K_s:
                player1.move = player1.speed
            elif event.key == K_UP:
                player2.move = -player2.speed
            elif event.key == K_DOWN:
                player2.move = player2.speed
            elif event.key == K_SPACE:
                paused = False
                ball.xMove = random.randint(100,250)
                ball.yMove = random.randint(100,250)
                if random.randint(0,1) == 0:
                    ball.xMove = -ball.xMove
                if random.randint(0,1) == 0:
                    ball.yMove = -ball.yMove
        elif event.type == KEYUP:
            if event.key == K_w or event.key == K_s:
                player1.move = 0
            elif event.key == K_UP or event.key == K_DOWN:
                player2.move = 0
    
    screen.blit(background, (0,0))
    pygame.draw.rect(screen, (255,255,255), Rect((5,5), (WIDTH - 10, HEIGHT - 10)), 2)
    pygame.draw.aaline(screen, (255,255,255), (int(WIDTH/2), 5), ((int(WIDTH/2), HEIGHT - 5)))

    screen.blit(player1.image, (player1.x, player1.y))
    screen.blit(player1.image, (player2.x, player2.y))
    screen.blit(ball.image, (ball.x, ball.y))
    score1 = font.render(str(player1.score), True, (255,255,255))
    score2 = font.render(str(player2.score), True, (255,255,255))
    screen.blit(score1, (15,15))
    screen.blit(score2, (WIDTH/2 + 15, 15))

    if (paused):
        screen.blit(font.render("Press SPACE to Start Round", True, (255,255,255)), (WIDTH/2 - 210, HEIGHT/2 - 70))
    
    pygame.display.update()
    


pygame.quit()

