# Desc: A small game where when the screen is clicked
# A ball will be generated with a traveling at a random velocity
# and bounces when it hits a wall
import pygame
import random

## Constants
# Ball object constants
# Load ball and set ball config
BALL_SIZE = 20
ball_img = pygame.image.load('ball.png')
BALL = pygame.transform.scale(ball_img, (BALL_SIZE, BALL_SIZE))

# Game frame constants declaration
FPS = 60                    # Frames per second
WIDTH, HEIGHT = 900, 500    # Game dimensions
GRAY = (100,100,110)        # Background colour
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!")

# Updates and creates movements for balls, updates velocity on collision
def ball_movement(balls):
    for i, (ball, ball_prop_x, ball_prop_y) in enumerate(balls):
        # Change X direction on wall collision
        if ball.x <= 0 or ball.x >= WIDTH - BALL_SIZE: 
            ball.x -= ball_prop_x 
            balls[i][1] = -ball_prop_x 
        else:
            ball.x += ball_prop_x 
        
        # Change Y direction on wall collision
        if ball.y <= 0 or ball.y >= HEIGHT - BALL_SIZE: 
            ball.y -= ball_prop_y
            balls[i][2] = -ball_prop_y 
        else:
            ball.y += ball_prop_y

# Create the pygame frame
def draw_window(balls):
    WIN.fill(GRAY)      # Background
    for ball in balls:  # Draw balls onto frame
        WIN.blit(BALL, (ball[0].x, ball[0].y))

    pygame.display.update()

# MAIN LOOP START HERE
def main():
    # Variable declarations
    run = True
    clock = pygame.time.Clock()
    balls = []

    while run:
        clock.tick(FPS)
        # Main loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT: run = False
        
            # Get position of mouse and register click
            mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP:
                # create a ball
                ball = pygame.Rect(mouse_pos[0], mouse_pos[1], BALL_SIZE, BALL_SIZE)
                ball_prop_x = random.randrange(-7,7,1)
                ball_prop_y = random.randrange(-7,7,2) 
                balls.append([ball, ball_prop_x, ball_prop_y])

        ball_movement(balls)
        draw_window(balls)

    pygame.quit()

if __name__ == "__main__":
    main()
