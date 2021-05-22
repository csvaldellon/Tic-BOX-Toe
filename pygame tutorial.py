import pygame, sys

pygame.init()
screen = pygame.display.set_mode((576, 1024))
clock = pygame.time.Clock()

bg_surface = pygame.image.load("C:/Users/Val/Downloads/FlappyBird_Python-master/FlappyBird_Python-master/assets/background-day.png")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(bg_surface, (0, 0))
    pygame.display.update()
    clock.tick(120)

