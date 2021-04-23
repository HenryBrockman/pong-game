import pygame
from math import ceil, floor

pygame.init()

base = 750
window_width = base
window_height = int(base * 0.8)

# set window and style
win = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Pong!")

# set colors

black = (0, 0, 0)
white = (250, 250, 250)

# build title
font = pygame.font.SysFont('Bit5x3.tff', 32)

p1_score = 0
p2_score = 0

# build rectangle

player1 = pygame.draw.rect(win, white, (20, (ceil(window_height/2)) - ceil(window_height/6), 10, ceil(window_height/6)))
player2 = pygame.draw.rect(win, white, (base - 20, (ceil(window_height/2)) - ceil(window_height/6), 10, ceil(window_height/6)))

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

    
    
    text = font.render("PONG", False, white, None)
    win.blit(text, (window_width/2 - (text.get_rect().width / 2), 20))

    p1_score_text = font.render(str(p1_score), False, white, None)
    win.blit(p1_score_text, (ceil(base/15) - (p1_score_text.get_rect().width), 20))

    p2_score_text = font.render(str(p2_score), False, white, None)
    win.blit(p2_score_text, ((base - (ceil(base/15))) - (p2_score_text.get_rect().width), 20))

    pygame.display.update()

pygame.quit()