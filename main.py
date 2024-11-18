from numpy import equal
import pygame
import time

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Snake")

col = 10
row = 10
grid = [[0]*col]*row
body = 1
apples = 0
def initGrid():
    for i in range(col):
        for j in range(row):
            grid[i][j] = 0

def drawGrid():
    for i in range(col):
        for j in range(row):
            if grid[i][j] == 0:
                pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(i * 50, j * 50, 50, 50), 1)
                pygame.display.update()
            elif grid[i][j] == 1:
                pygame.draw.rect(screen, (255,0,0), pygame.Rect(i * 50, j * 50, 50, 50))
                pygame.display.update()
    pygame.display.update()

# def gridSnake():
             



while True:
    initGrid()
    drawGrid()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            break
    pygame.display.update()

        
