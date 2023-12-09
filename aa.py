import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 20
GOAL_WIDTH = 100
GOAL_HEIGHT = 50
BALL_SPEED = 10
INITIAL_GOAL_SPEED = 5

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Goal Shooter")

# Load background image
background_image = pygame.image.load("b.jpg")  # Replace with the path to your image

# Load ball image
ball_image = pygame.image.load("cupcake.jpeg")  # Replace with the path to your ball image
ball_image = pygame.transform.scale(ball_image, (BALL_RADIUS * 2, BALL_RADIUS * 2))

# Load goal image
goal_image = pygame.image.load("R.jpeg")  # Replace with the path to your goal image
goal_image = pygame.transform.scale(goal_image, (GOAL_WIDTH, GOAL_HEIGHT))

# Initialize the clock
clock = pygame.time.Clock()

# Initialize the ball
ball_pos = [WIDTH // 2, HEIGHT - 2 * BALL_RADIUS]
ball_speed = [0, 0]

# Initialize the goal
goal_pos = [random.randint(0, WIDTH - GOAL_WIDTH), 0]
goal_speed = [INITIAL_GOAL_SPEED, 0]

# Initialize the score
score = 0

# Load sound effect for scoring a goal
goal_score_sound = pygame.mixer.Sound("a.mp3")  # Replace with the path to your sound file

# Load sound effect for missing a goal
miss_sound = pygame.mixer.Sound("aa.mp3")  # Replace with the path to your sound file

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Shoot the ball upward when the mouse is clicked
            ball_speed = [0, -BALL_SPEED]

    
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    
    goal_pos[0] += goal_speed[0]
    goal_pos[1] += goal_speed[1]

    # Check if the ball goes beyond the top edge of the screen
    if ball_pos[1] < 0:
        # Reset the ball's position
        ball_pos = [WIDTH // 2, HEIGHT - 2 * BALL_RADIUS]
        ball_speed = [0, 0]

        # Reset the score
        score = 0

        # Play the sound effect for missing a goal
        miss_sound.play()

    # Check for collisions
    if (
        ball_pos[0] + BALL_RADIUS > goal_pos[0]
        and ball_pos[0] - BALL_RADIUS < goal_pos[0] + GOAL_WIDTH
        and ball_pos[1] + BALL_RADIUS > goal_pos[1]
        and ball_pos[1] - BALL_RADIUS < goal_pos[1] + GOAL_HEIGHT
    ):
        # Goal scored!
        score += 1
        ball_pos = [WIDTH // 2, HEIGHT - 2 * BALL_RADIUS]
        ball_speed = [0, 0]

        # Increase the goal speed
        goal_speed[0] += 1

        # Play the sound effect for scoring a goal
        goal_score_sound.play()

    # Check if the goal reaches the edges of the screen
    if goal_pos[0] < 0 or goal_pos[0] + GOAL_WIDTH > WIDTH:
        goal_speed[0] = -goal_speed[0]

    # Blit the background image onto the screen
    screen.blit(background_image, (0, 0))

    # Draw other elements
    screen.blit(ball_image, (ball_pos[0] - BALL_RADIUS, ball_pos[1] - BALL_RADIUS))
    screen.blit(goal_image, (goal_pos[0], goal_pos[1]))

    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

    # Set the frames per second
    clock.tick(30)
