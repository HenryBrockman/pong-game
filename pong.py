import pygame

pygame.init()

window_width = 750
window_height = 600

# set window and style
win = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("PONG!")

running = True
while running:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

pygame.quit()
