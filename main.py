import pygame
import time

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pong")

def pl1():
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(20, 100, 20, 80))

def pl2():
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(760, 100, 20, 80))
while True:
    pl1()
    pl2()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
    pygame.display.update()

        
