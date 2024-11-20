import pygame
import time

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pong")
y1 = 100
y2 = 100

cx = 400
cy = 300


run = True
while run:
    pygame.time.delay(20)
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and y1 > 0:
        y1 -= 10
    if keys[pygame.K_s] and y1<520:
        y1 += 10
    if keys[pygame.K_UP] and y2 > 0:
        y2 -= 10
    if keys[pygame.K_DOWN] and y2 < 520:
        y2 += 10
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(20, y1, 20, 80))
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(760, y2, 20, 80))
    pygame.draw.circle(screen, (255, 255, 255), (cx, cy), 15 )
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        
