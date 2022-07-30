from cgitb import grey
import pygame
pygame.init()

W,H = 600,400
sc = pygame.display.set_mode((600,400))
pygame.display.set_caption("PyGame №1")

WHITE = (255,255,255)
BLUE = (0,0,255)
GREEN = (0,255,0)
pygame.draw.rect(sc, WHITE, (10,10,50,100), 2)
pygame.draw.line(sc, GREEN, (200,20), (350,50))
pygame.draw.aaline(sc, GREEN, (200, 40), (359,70))
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()



