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

class Score:
    def __init__(self, win, color, font, score):
        self.win = win
        self.color = color
        self.font = font
        self.score = score
        self.build()

    def build(self):
        self.text = font.render(str(self.score), False, white, None)
    
    def get_width(self):
        return self.text.get_rect().width

    def add_point(self):
        self.score += 1

# Functions

def full_build():

    win.fill(black)

    player1.build()
    player2.build()

    ball.build()

    player1_score.build()
    win.blit(player1_score.text, (BASE//15 - player1_score.get_width(), 20))

    player2_score.build()
    win.blit(player2_score.text, ((BASE - BASE//15) - player2_score.get_width(), 20))
    
    text = font.render("PONG", False, white, None)
    win.blit(text, (BASE/2 - (text.get_rect().width / 2), 20))

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

player1 = Player(win, white, 20, y1, 10, player_height, VEL)
player2 = Player(win, white, BASE - 35, y2, 10, player_height, VEL)

player1_score = Score(win, white, font, 0)
player2_score = Score(win, white, font, 0)



running = True
while running:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                player1_score.add_point()
            if event.key == pygame.K_2:
                player2_score.add_point()
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

    if up1 and player1.playerY > 0:
        player1.move_up()
    if down1 and player1.playerY < WINDOW_HEIGHT - player_height:
        player1.move_down()

    if up2 and player2.playerY > 0:
        player2.move_up()
    if down2 and player2.playerY < WINDOW_HEIGHT - player_height:
        player2.move_down()

    full_build()

    pygame.display.update()
    
pygame.quit()