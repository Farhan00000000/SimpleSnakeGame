import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 480, 640
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Load images
snake_img = pygame.image.load('snake.png').convert_alpha()  # Ensure your snake image has a transparent background
food_img = pygame.image.load('food.png').convert_alpha()  # Ensure your food image has a transparent background

# Scale images if needed
snake_img = pygame.transform.scale(snake_img, (30, 30))
food_img = pygame.transform.scale(food_img, (25, 20))

# Colors
black = (7, 1, 50)
white = (125, 225, 1)

# Game variables
clock = pygame.time.Clock()
snake_speed = 10
snake_block = 20

font_style = pygame.font.SysFont(None, 34)
score_font = pygame.font.SysFont(None, 37)


def score_display(score):
    value = score_font.render("Your Score: " + str(score), True, white)
    win.blit(value, [0, 0])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    win.blit(mesg, [width / 20, height / 40])


def gameloop():

    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0

    while not game_over:

        while game_close == True:
            win.fill(black)
            message("You Lost! Press Q-Quit or C-Play Again", white)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameloop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        win.fill(black)
        win.blit(food_img, (foodx, foody))
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        for pos in snake_list:
            win.blit(snake_img, (pos[0], pos[1]))

        score_display(length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameloop()
