import numpy as np
import pygame

pygame.init()

screen_width = 800
screen_height = 900

screen = pygame.display.set_mode((screen_width, screen_height))

done = False
FPS = 60
clock = pygame.time.Clock()


def makeRandomCircle():
    x = np.random.randint(0, screen_width)
    y = np.random.randint(0, screen_height)
    xy = np.array((x,y), dtype="float")
    vxy = np.random.uniform(low=1, high=13, size=2)
    color = np.random.randint(low=0, high=256, size=3)
    color[1] = 200
    color[2] = 200
    radius = np.random.uniform(low=2., high=55.)

    monster = {
        "loc" : xy,
        "radius" : radius,
        "velocity" : vxy,
        "rgb" : color
    }

    return monster

# ---------------------------------------------------------------------------
def draw_circles(myscreen, circles):
    for circ in circles:
        pygame.draw.circle(surface=myscreen,
                           color = circ["rgb"],
                           center = circ["loc"],
                           radius = circ["radius"])
        
    return

# ---------------------------------------------------------------------------
list_of_circles = []

for i in range(1000):
    c = makeRandomCircle()
    list_of_circles.append(c)

while not done:
    # 1. event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # 2. draw
    screen.fill((255, 255, 255))
    draw_circles(screen, list_of_circles)

    # 3. state update
    for circ in list_of_circles:
        # 1. update
        circ["loc"] += circ["velocity"]

        xy = circ["loc"]
        x = xy[0]
        y = xy[1]

        # 2. check the location
        if x >= screen_width or x < 0:  # left & right
            circ["velocity"][0] *= -1
       
        if y >= screen_height or y < 0: # up & down
            circ["velocity"][1] *= -1

        circ["velocity"][1] += 0.5



    # 4. refresh
    pygame.display.flip()
    clock.tick(FPS)

# save things

#
pygame.quit()
print("bye~~")