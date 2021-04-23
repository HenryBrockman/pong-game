# 16
# Imports and Initilization
import pygame
from math import ceil, floor

pygame.init()

# Classes
class Ball:
    def __init__(self, win, color, ballX, ballY, radius):
        self.win = win
        self.color = color
        self.ballX = ballX
        self.ballY = ballY
        self.radius = radius
        self.build()

    def build(self):
        pygame.draw.circle(self.win, self.color, (self.ballX, self.ballY), self.radius)

class Player:
    def __init__(self, win, color, playerX, playerY, rectWidth, rectHeight, vel):
        self.win = win
        self.color = color
        self.playerX = playerX
        self.playerY = playerY
        self.rectWidth = rectWidth
        self.rectHeight = rectHeight
        self.vel = vel
        self.build()
        
    def build(self):
        pygame.draw.rect(self.win, self.color, (self.playerX, self.playerY, self.rectWidth, self.rectHeight))

    def move_up(self):
        self.playerY -= self.vel

    def move_down(self):
        self.playerY += self.vel

# Code

# Set constants

BASE = 750
WINDOW_WIDTH = BASE
WINDOW_HEIGHT = int(BASE * 0.8)

VEL = 10

# set window and style
win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pong!")

# set colors

black = (0, 0, 0)
white = (250, 250, 250)

# build title
font = pygame.font.SysFont('Bit5x5.tff', 32)

p1_score = 0
p2_score = 0

# build rectangle

y1 = (WINDOW_HEIGHT//2) - (WINDOW_HEIGHT//6)/2
y2 = (WINDOW_HEIGHT//2) - (WINDOW_HEIGHT//6)/2

player_height = ceil(WINDOW_HEIGHT/6)

# initilize Booleans

down1 = False
up1 = False

down2 = False
up2 = False

# Initilize Objects

ball = Ball(win, white, WINDOW_WIDTH//2, WINDOW_HEIGHT//2, 14)

player1 = Player(win, white, 20, y1, 10, player_height)
player2 = Player(win, white, BASE - 35, y2, 10, player_height)


running = True
while running:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                p1_score += 1
                win.fill(black)
            if event.key == pygame.K_2:
                p2_score += 1
                win.fill(black)

            if event.key == pygame.K_w:
                up1 = True
            if event.key == pygame.K_s:
                down1 = True

            if event.key == pygame.K_UP:
                up2 = True
            if event.key == pygame.K_DOWN:
                down2 = True

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_w:
                up1 = False
            if event.key == pygame.K_s:
                down1 = False

            if event.key == pygame.K_UP:
                up2 = False
            if event.key == pygame.K_DOWN:
                down2 = False

    # if up1 and y1 > 0:
    #     y1 -= VEL
    #     win.fill(black)
    # if down1 and y1 < WINDOW_HEIGHT - player_height:
    #     y1 += VEL
    #     win.fill(black)

    # if up2 and y2 > 0:
    #     y2 -= VEL
    #     win.fill(black)
    # if down2 and y2 < WINDOW_HEIGHT - player_height:
    #     y2 += VEL
    #     win.fill(black)

    if up1 and y1 > 0:
        player1.move_up()
    if down1 and y1 < WINDOW_HEIGHT - player_height:
        player1.move_down()

    if up2 and y2 > 0:
        player2.move_up()
    if down2 and y2 < WINDOW_HEIGHT - player_height:
        player2.move_down()


    win.fill(black)

    player1.build()
    player2.build()

    ball.build()

    p1_score_text = font.render(str(p1_score), False, white, None)
    win.blit(p1_score_text, (ceil(BASE/15) - (p1_score_text.get_rect().width), 20))

    p2_score_text = font.render(str(p2_score), False, white, None)
    win.blit(p2_score_text, ((BASE - (ceil(BASE/15))) - (p2_score_text.get_rect().width), 20))

    # player1 = pygame.draw.rect(win, white, (20, y1, 10, player_height))
    # player2 = pygame.draw.rect(win, white, (BASE - 35, y2, 10, player_height))
    
    # text = font.render("PONG", False, white, None)
    # win.blit(text, (BASE/2 - (text.get_rect().width / 2), 20))

    # p1_score_text = font.render(str(p1_score), False, white, None)
    # win.blit(p1_score_text, (ceil(BASE/15) - (p1_score_text.get_rect().width), 20))

    # p2_score_text = font.render(str(p2_score), False, white, None)
    # win.blit(p2_score_text, ((BASE - (ceil(BASE/15))) - (p2_score_text.get_rect().width), 20))

    pygame.display.update()

pygame.quit()