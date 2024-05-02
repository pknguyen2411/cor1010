"""
 Simple graphics demo
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
"""
 
# Import a library of functions called 'pygame'
import pygame
import numpy as np
 
# Initialize the game engine
pygame.init()
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
myColor = (242, 170, 188)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


PI = 3.141592653
 
# Set the width and height of the screen
size = (400, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("용덕 bi lam sao y")
 
# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
 
# Loop as long as done == False
while not done:

    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         print("User asked to quit.")
    #     elif event.type == pygame.KEYDOWN:
    #         print("User pressed a key.")
    #     elif event.type == pygame.KEYUP:
    #         print("User let go of a key.")
    #     elif event.type == pygame.MOUSEBUTTONDOWN:
    #         print("User pressed a mouse button")

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            print("Close pressed.")
            done = True  # Flag that we are done so we exit this loop
 
    # All drawing code happens after the for loop and but
    # inside the main while not done loop.
 
    # Clear the screen and set the screen background
    screen.fill(WHITE)
 
    x0 = np.random.randint(0, size[0])
    y0 = np.random.randint(0, size[1])
    pygame.draw.line(screen, RED, [x0, y0], [100, 500])
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
 
    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)
 
# Be IDLE friendly
pygame.quit()