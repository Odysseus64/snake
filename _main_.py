import pygame
import random

pygame.init()

window_width = 800
window_height = 600

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake")

snake_size = 20
snake_speed = 10

font_style = pygame.font.SysFont(None, 40)

def show_score(score):
    score_text = font_style.render("Счет: " + str(score), True, white)
    window.blit(score_text, [10, 10])

def draw_snake(snake_list):
    for snake in snake_list:
        pygame.draw.rect(window, green, [snake[0], snake[1], snake_size, snake_size])

def game_loop():
    game_over = False
    game_close = False

    x1 = window_width // 2
    y1 = window_height // 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_length = 1

    food_x = round(random.randrange(0, window_width - snake_size) / snake_size) * snake_size
    food_y = round(random.randrange(0, window_height - snake_size) / snake_size) * snake_size

    clock = pygame.time.Clock()

    while not game_over:
        while game_close:
            window.fill(white)
            game_over_text = font_style.render("q - exit c - restart", True, red)
            window.blit(game_over_text, [window_width // 6, window_height // 3])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_size
                    x1_change = 0

        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        window.fill(white)
        pygame.draw.rect(window, red, [food_x, food_y, snake_size, snake_size])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for snake in snake_list[:-1]:
            if snake == snake_head:
                game_close = True

        draw_snake(snake_list)
        show_score(snake_length - 1)

        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, window_width - snake_size) / snake_size) * snake_size
            food_y = round(random.randrange(0, window_height - snake_size) / snake_size) * snake_size
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()

game_loop()
