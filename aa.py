import pygame
import sys
import random


pygame.init()


WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 20
GOAL_WIDTH = 100
GOAL_HEIGHT = 50
BALL_SPEED = 10
INITIAL_GOAL_SPEED = 5


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Goal Shooter")


background_image = pygame.image.load("b.jpg")  


ball_image = pygame.image.load("cupcake.jpeg")  
ball_image = pygame.transform.scale(ball_image, (BALL_RADIUS * 2, BALL_RADIUS * 2))

# Load goal image
goal_image = pygame.image.load("R.jpeg")  
goal_image = pygame.transform.scale(goal_image, (GOAL_WIDTH, GOAL_HEIGHT))


clock = pygame.time.Clock()

ball_pos = [WIDTH // 2, HEIGHT - 2 * BALL_RADIUS]
ball_speed = [0, 0]


goal_pos = [random.randint(0, WIDTH - GOAL_WIDTH), 0]
goal_speed = [INITIAL_GOAL_SPEED, 0]


score = 0

goal_score_sound = pygame.mixer.Sound("a.mp3")  


miss_sound = pygame.mixer.Sound("aa.mp3")  


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            
            ball_speed = [0, -BALL_SPEED]

    
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    
    goal_pos[0] += goal_speed[0]
    goal_pos[1] += goal_speed[1]

   
    if ball_pos[1] < 0:
        
        ball_pos = [WIDTH // 2, HEIGHT - 2 * BALL_RADIUS]
        ball_speed = [0, 0]

    
        score = 0

        
        miss_sound.play()

    
    if (
        ball_pos[0] + BALL_RADIUS > goal_pos[0]
        and ball_pos[0] - BALL_RADIUS < goal_pos[0] + GOAL_WIDTH
        and ball_pos[1] + BALL_RADIUS > goal_pos[1]
        and ball_pos[1] - BALL_RADIUS < goal_pos[1] + GOAL_HEIGHT
    ):
      
        score += 1
        ball_pos = [WIDTH // 2, HEIGHT - 2 * BALL_RADIUS]
        ball_speed = [0, 0]

        
        goal_speed[0] += 1

        goal_score_sound.play()

    
    if goal_pos[0] < 0 or goal_pos[0] + GOAL_WIDTH > WIDTH:
        goal_speed[0] = -goal_speed[0]


    screen.blit(background_image, (0, 0))

    
    screen.blit(ball_image, (ball_pos[0] - BALL_RADIUS, ball_pos[1] - BALL_RADIUS))
    screen.blit(goal_image, (goal_pos[0], goal_pos[1]))

    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

    
    clock.tick(30)
