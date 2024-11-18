import pygame
import time

pygame.init()

screen = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Snake")

def drawGrid():
    for i in range(10):
        for j in range(10):
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(i *50, j*50, 50, 50), 1)
            pygame.display.update()
        pygame.display.update()
    pygame.display.update()

def drawSnake():
    for i in range(10):
        for j in range(10):
            pygame.draw.rect(screen, (0, 255, 0), pygame.)
    
        
    
    


        

while True:
    # drawGrid()
    moveCube()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            break
    pygame.display.update()

        
