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
        self.startPosX = ballX
        self.startPosY = ballY
        self.ballX = ballX
        self.ballY = ballY
        self.radius = radius
        self.dX = 0
        self.dY = 0
        self.build()

    def build(self):
        pygame.draw.circle(self.win, self.color, (self.ballX, self.ballY), self.radius)

    def reset(self):
        self.ballX = self.startPosX
        self.ballY = self.startPosY

        self.dX = 0
        self.dY = 0

    def start(self):
        self.dX = 15
        self.dY = 5

    def move(self):
        self.ballX += self.dX
        self.ballY += self.dY

    def player_deflect(self):
        self.dX = -self.dX

    def side_deflect(self):
        self.dY = -self.dY

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
class collision:
    def ball_player1(self, ball, player1):
        if ball.ballY + ball.radius > player1.playerY and ball.ballY - ball.radius < player1.playerY + player1.rectHeight:
            if ball.ballX - ball.radius <= player1.playerX + player1.rectWidth:
                return True
        return False
    def ball_player2(self, ball, player2):
        if ball.ballY + ball.radius > player2.playerY and ball.ballY - ball.radius < player2.playerY + player2.rectHeight:
            if ball.ballX + ball.radius >= player2.playerX:
                return True
        return False

    def ball_side(self, ball, height):
        if ball.ballY - ball.radius <= 0:
            return True

        if ball.ballY - ball.radius >= height:
            return True
        return False
    
    def ball_goal1(self, ball, width):
        if ball.ballX - ball.radius <= 0:
            return True

    def ball_goal2(self, ball, width):
        if ball.ballX - ball.radius >= width:
            return True
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

# initilize Booleans

down1 = False
up1 = False

down2 = False
up2 = False

# Initilize Objects

ball = Ball(win, white, WINDOW_WIDTH//2, WINDOW_HEIGHT//2, 14)

player1 = Player(win, white, 20, (WINDOW_HEIGHT//2) - (WINDOW_HEIGHT//6)/2, 10, WINDOW_HEIGHT//6, VEL)
player2 = Player(win, white, BASE - 35, (WINDOW_HEIGHT//2) - (WINDOW_HEIGHT//6)/2, 10, WINDOW_HEIGHT//6, VEL)

player1_score = Score(win, white, font, 0)
player2_score = Score(win, white, font, 0)

ball_col = collision()

playing = False
running = True
while running:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ball.start()
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

    ball.move()

    if up1 and player1.playerY >= 0:
        player1.move_up()
    if down1 and player1.playerY <= WINDOW_HEIGHT - player1.rectHeight:
        player1.move_down()

    if up2 and player2.playerY >= 0:
        player2.move_up()
    if down2 and player2.playerY <= WINDOW_HEIGHT - player2.rectHeight:
        player2.move_down()

    if ball_col.ball_player1(ball, player1):
        ball.player_deflect()
    if ball_col.ball_player2(ball, player2):
        ball.player_deflect()

    if ball_col.ball_side(ball, WINDOW_HEIGHT):
        ball.side_deflect()

    if ball_col.ball_goal1(ball, WINDOW_WIDTH):
        ball.reset()
        player2_score.add_point()
    if ball_col.ball_goal2(ball, WINDOW_WIDTH):
        ball.reset()
        player1_score.add_point()

    full_build()

    pygame.display.update()

pygame.quit()