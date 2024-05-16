import pygame
import numpy as np

pygame.init()

screen_width = 800
screen_height = 900
screen_size = (screen_width, screen_height)

screen = pygame.display.set_mode (screen_size)

done = False
FPS = 60
clock = pygame.time.Clock()

# ---------------------------------------------------------------
def makeRandomCircles():
    x = np.random.randint(0, screen_width)
    y = np.random.randint(0, screen_height)
    xy = np.array([x,y])
    vxy = np.random.uniform(low=1., high=15., size=2)
    color = np.random.randint(low=0, high=256, size=3)
    radius = np.random.uniform(low=2., high=50.)
#              0      1     2     3
    monster = [xy, radius, vxy, color]
    return monster

def draw_circles(scrn, circles):
    for circ in circles:
        pygame.draw.circle(surface=scrn,
                           color=circ[3],
                           center=circ[0],
                           radius=circ[1])
    pass

def update_circles(circles):
    for c in circles:
        xy = c[0]
        vxy = c[2]
        xy = xy + vxy
        c[0] = xy
        # print("---")
    pass

list_of_circles = []

for i in range(10):
    circ = makeRandomCircles()
    list_of_circles.append(circ)
# ---------------------------------------------------------------

while not done:
    # 1. event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # 2. draw
    screen.fill ( (255, 255, 255))

    draw_circles(screen, list_of_circles)

    # 3. state update
    update_circles(list_of_circles)

    # 4. refresh
    pygame.display.flip()
    clock.tick(FPS)