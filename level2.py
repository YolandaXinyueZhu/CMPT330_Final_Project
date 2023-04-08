import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the window
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake Game - Level 2: The Maze")

# Set up the clock
clock = pygame.time.Clock()

# Set up the snake
SNAKE_SIZE = 10
snake = [(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)]
snake_direction = "right"

# Set up the maze
def create_maze():
    maze = []
    # Horizontal walls
    for x in range(0, WINDOW_WIDTH, SNAKE_SIZE):
        maze.append((x, 100))
        maze.append((x, 380))
    # Vertical walls
    for y in range(120, 380, SNAKE_SIZE):
        maze.append((100, y))
        maze.append((500, y))
    return maze


maze = create_maze()
maze_exit = (WINDOW_WIDTH - 2 * SNAKE_SIZE, WINDOW_HEIGHT // 2)


# Set up the food
def generate_food():
    while True:
        food_position = (random.randint(0, WINDOW_WIDTH // SNAKE_SIZE - 1) * SNAKE_SIZE,
                         random.randint(0, WINDOW_HEIGHT // SNAKE_SIZE - 1) * SNAKE_SIZE)
        if food_position not in maze and food_position not in snake:
            return food_position

food_position = generate_food()


# Set up the score and required food items
score = 0
required_food_items = 5

# Set up the game loop
game_running = True
while game_running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != "down":
                snake_direction = "up"
            elif event.key == pygame.K_DOWN and snake_direction != "up":
                snake_direction = "down"
            elif event.key == pygame.K_LEFT and snake_direction != "right":
                snake_direction = "left"
            elif event.key == pygame.K_RIGHT and snake_direction != "left":
                snake_direction = "right"

    # Move the snake
    if snake_direction == "up":
        snake.insert(0, (snake[0][0], snake[0][1] - SNAKE_SIZE))
    elif snake_direction == "down":
        snake.insert(0, (snake[0][0], snake[0][1] + SNAKE_SIZE))
    elif snake_direction == "left":
        snake.insert(0, (snake[0][0] - SNAKE_SIZE, snake[0][1]))
    elif snake_direction == "right":
        snake.insert(0, (snake[0][0] + SNAKE_SIZE, snake[0][1]))

    # Check for collisions with the walls, maze, and itself
    if (snake[0][0] < 0 or snake[0][0] >= WINDOW_WIDTH or
        snake[0][1] < 0 or snake[0][1] >= WINDOW_HEIGHT or
        snake[0] in maze or
        snake[0] in snake[1:]):
        game_running = False

    # Check for collisions with the
        if snake[0] == food_position:
            food_position = generate_food()
            score += 1
            if score == required_food_items:
                if snake[-1] == maze_exit:
                    print("Congratulations! You have completed Level 2: The Maze!")
                    game_running = False
        else:
            snake.pop()

        # Draw the game objects
        window.fill((0, 0, 0))
        for segment in snake:
            pygame.draw.rect(window, (255, 255, 255), (segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))
        pygame.draw.rect(window, (255, 0, 0), (food_position[0], food_position[1], SNAKE_SIZE, SNAKE_SIZE))

        # Draw the maze
        for wall in maze:
            pygame.draw.rect(window, (255, 255, 255), (wall[0], wall[1], SNAKE_SIZE, SNAKE_SIZE))

        # Draw the exit
        pygame.draw.rect(window, (0, 255, 0), (maze_exit[0], maze_exit[1], SNAKE_SIZE, SNAKE_SIZE))

        pygame.display.update()

        # Set the game speed
        clock.tick(10)

# Clean up Pygame
pygame.quit()

