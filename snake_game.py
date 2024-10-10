import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 600, 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Game parameters
snake_block = 10
initial_speed = 10  # Start with a slower speed
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
level_font = pygame.font.SysFont("bahnschrift", 30)

# Function to display the score
def show_score(score):
    value = score_font.render(f"Score: {score}", True, black)
    win.blit(value, [10, 10])

# Function to display the level
def show_level(level):
    value = level_font.render(f"Level: {level}", True, black)
    win.blit(value, [width - 150, 10])

# Function to display the snake
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(win, black, [x[0], x[1], snake_block, snake_block])

# Function to display a message on the screen
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    win.blit(mesg, [width / 6, height / 3])

# Main game loop
def game_loop():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    # Create initial food position
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    # Start with the initial slower speed
    snake_speed = initial_speed
    score = 0
    level = 1

    while not game_over:

        while game_close:
            win.fill(white)
            message("You Lost! Press P-Play Again or Q-Quit", red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        game_loop()

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

        # Check if the snake hits the boundaries
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        win.fill(blue)
        
        # Draw the food
        pygame.draw.rect(win, green, [foodx, foody, snake_block, snake_block])

        # Draw the snake
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        
        # Remove the last segment if the snake doesn't eat food
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check collision with itself
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(snake_block, snake_list)
        show_score(score)
        show_level(level)

        pygame.display.update()

        # Check if the snake eats the food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length_of_snake += 1
            score += 1

            # Increase speed and level every 10 points
            if score % 10 == 0:
                level += 1
                snake_speed += 5

            # Win the game if the player reaches 100 points
            if score >= 100:
                win.fill(white)
                message("Congratulations! You Win!", green)
                pygame.display.update()
                time.sleep(2)
                game_over = True

        pygame.time.Clock().tick(snake_speed)

    pygame.quit()
    quit()

# Start the game
game_loop()
