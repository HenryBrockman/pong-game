import pygame
from math import ceil, floor

pygame.init()

base = 750
window_width = base
window_height = int(base * 0.8)

vel = 20

# set window and style
win = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Pong!")

# set colors

black = (0, 0, 0)
white = (250, 250, 250)

# build title
font = pygame.font.SysFont('Bit5x5.tff', 32)

p1_score = 0
p2_score = 0

# build rectangle

y1 = (ceil(window_height/2)) - ceil(window_height/6)
y2 = (ceil(window_height/2)) - ceil(window_height/6)

# initilize movement booleans

down1 = False
up1 = False

down2 = False
up2 = False

running = True
while running:
    pygame.time.delay(100)
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

    if up1:
        y1 -= vel
        win.fill(black)
    if down1:
        y1 += vel
        win.fill(black)

    if up2:
        y2 -= vel
        win.fill(black)
    if down2:
        y2 += vel
        win.fill(black)




    player1 = pygame.draw.rect(win, white, (20, y1, 10, ceil(window_height/6)))
    player2 = pygame.draw.rect(win, white, (base - 35, y2, 10, ceil(window_height/6)))
    
    text = font.render("PONG", False, white, None)
    win.blit(text, (window_width/2 - (text.get_rect().width / 2), 20))

    p1_score_text = font.render(str(p1_score), False, white, None)
    win.blit(p1_score_text, (ceil(base/15) - (p1_score_text.get_rect().width), 20))

    p2_score_text = font.render(str(p2_score), False, white, None)
    win.blit(p2_score_text, ((base - (ceil(base/15))) - (p2_score_text.get_rect().width), 20))

    pygame.display.update()

pygame.quit()