import pygame
import random


pygame.init()


WIDTH, HEIGHT = 500, 500

BLOCK_SIZE = 10
SNAKE_SPEED = 15

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

 
clock = pygame.time.Clock()
def draw_snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, (0, 255, 0), [x[0], x[1], block_size, block_size])


while True:
    game_over = False
    game_close = False

    x1, y1 = round(WIDTH/2), round(HEIGHT/2)
    x1_change, y1_change = 0, 0


    snake_list = []
    length_of_snake = 1

    food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 10.0) * 10.0
    food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 10.0) * 10.0

    while not game_over:
        while game_close:
            screen.fill((0,0,0))
            pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -BLOCK_SIZE
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = BLOCK_SIZE
                    x1_change = 0
                    
        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            pygame.quit()

        x1 += x1_change
        y1 += y1_change
        screen.fill((50, 50, 50))
        pygame.draw.rect(screen, (213, 50, 80), [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])

        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for block in snake_list:
            if block == snake_head and block != snake_list[-1]:
                game_close = True
                break


        draw_snake(BLOCK_SIZE, snake_list)
        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 10.0) * 10.0
            food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(SNAKE_SPEED)


