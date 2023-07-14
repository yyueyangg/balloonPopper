# creating a ballon shape using pygame 

import pygame 
import sys 
from pygame.locals import *

WINDOW_WIDTH = 300
WINDOW_HEIGHT = 400
GREY = (230, 230, 230)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# initialize the window
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


# Loop forever
while True:

    # check and handle events (in this case only for quitting)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill a clear window with grey color
    window.fill(GREY)

    # draw balloon 
    # top left is origin(0, 0)
    pygame.draw.line(window, BLUE, (150, 200), (150, 380))  # (x1, y1), (x2, y2)
    pygame.draw.ellipse(window, RED, (115, 150, 70, 70))    # (x, y, xwidth, ywidth)
    pygame.draw.ellipse(window, RED, (143, 215, 15, 15))
    pygame.draw.rect(window, BLUE, (0, 0, 150, 100))

    pygame.display.update()