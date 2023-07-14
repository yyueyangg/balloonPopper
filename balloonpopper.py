# creating a balloon popping game 
# sys imported for sys.exit() if not there will be am error in display surface quit

import pygame 
import sys
import random 
from math import *

# constants 
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
MARGIN = 100
LOWERBOUND = 100

# colors rgb 
WHITE = (255, 255, 255)
LIGHTBLUE = (173, 216, 230)
RED = (255, 0, 0)
LIGHTGREEN = (124, 252, 0)
DARKGREY = (169, 169, 169)
DARKBLUE = (0, 0, 139)
GREEN = (0, 255, 0)
YELLOW= (255, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (155, 48, 255)
ORANGE = (255, 128, 0)

# why cant u declare score global here 
# global score declared within the function itself, 
# once declared global, anywhere throughout the code will be able to access
# however if declare here, code dont know what the global will be for 
# Python interpreter sees this at module load time and decides that the 
# global scope's score  should not be used inside the local scope, which leads to a problem when 
# you try to reference the variable before it is locally assigned

# If declare and assign at the same time in function burst
# invalid syntax 

# If declare score global and assign it 0 in burst function, the SCORE in showScore function is not defined 

SCORE = 0

# initialize the window 
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Balloon Popper")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 30)

# create balloon class 
class Balloon():
    def __init__(self, speed):
        # self.a and self.b purposes' are for the balloon to be an oval shape when drawing it 
        self.a = random.randint(30, 40)
        self.b = self.a + random.randint(0, 10)                             # range 30 to 50 
        self.x = random.randrange(MARGIN, WINDOW_WIDTH - self.a - MARGIN)   # range 100 to 360-370
        self.y = WINDOW_HEIGHT - LOWERBOUND                                 # 400
        self.angle = 90
        self.speed = speed 
        self.probability = [-1, -1, -1, 0, 0, 0, 0, 1, 1, 1]
        self.length = random.randint(50, 100)                               # range 50 to 100
        self.color = random.choice([RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE])

    # move balloons around window 
    def move(self):
        # different angle
        direction = random.choice(self.probability)
        if direction == -1:
            self.angle -= 10
        elif direction == 0:
            self.angle += 0
        else:
            self.angle += 10

        # different speed (as in moving towards the x and y position)
        self.x -= self.speed*cos(radians(self.angle))
        self.y -= self.speed*sin(radians(self.angle))

        # if balloon goes out of window, reset 
        if (self.x > WINDOW_WIDTH) or (self.x < 0):
            # if its 100 away from floating towards the upper bound, bounce back
            if self.y > WINDOW_HEIGHT/5:
                self.x -= self.speed*cos(radians(self.angle))
            else:
                self.reset()
        if (self.y < 0) or (self.y > WINDOW_HEIGHT):
            self.reset()

    # if ballon is bursted by the player, add score and reset another balloon  
    def burst(self):
        pos = pygame.mouse.get_pos()
        # get pos of cursor within range to pop balloon 
        if onBalloon(self.x, self.y, self.a, self.b, pos):
            global SCORE
            SCORE += 1
            self.reset()
            
    # reset balloon if fly away / burst
    # basically most attributes stay the same, just that the speed will keep getting slower 
    def reset(self):
        self.a = random.randint(30, 40)
        self.b = self.a + random.randint(0, 10)
        self.x = random.randrange(MARGIN, WINDOW_WIDTH - self.a - MARGIN)
        self.y = WINDOW_HEIGHT - LOWERBOUND
        self.angle = 90
        self.speed -= 0.02 
        self.probability = [-1, -1, -1, 0, 0, 0, 0, 1, 1, 1]
        self.length = random.randint(50, 100)
        self.color = random.choice([RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE])


    # drawing balloon 
    def draw(self):
        # for x, to align the line in the centre of the ellipse, line + self.a/2 for ellipse to have width of self.a
        # for y, for the line to not be too short, the line itself need to + self.b for the line to be drawn relatively more 
        # below the ellipse 
        pygame.draw.line(window, DARKBLUE, (self.x + self.a/2, self.y + self.b), (self.x + self.a/2, self.y + self.b + self.length))
        pygame.draw.ellipse(window, self.color, (self.x, self.y, self.a, self.b))
        # draw a smaller ellipse to connect the big ellipse to the line 
        pygame.draw.ellipse(window, self.color, (self.x + self.a/2 - 5, self.y + self.b - 3, 10, 10))


# instantiation 
# create a balloon list 
# create a range of 10 balloons with random choice of speed
# append balloons into this list 
balloons = []
oBalloon = 10
for i in range(oBalloon):
    obj = Balloon(random.choice([1, 1, 2, 2, 2, 2, 3, 3, 3, 4]))
    balloons.append(obj)    
    

# This is to get the range of position the mouse click can burst the balloon
# will also be used for burst and pointer functions. 
def onBalloon(x, y, a, b, pos):
    if (x < pos[0] < x+a) and (y < pos[1] <y+b):
        return True 
    else:
        return False 


# draw platform
def platform():
    pygame.draw.rect(window, DARKGREY, (0, WINDOW_HEIGHT-LOWERBOUND, WINDOW_WIDTH, WINDOW_HEIGHT)) # (x1, y1, x2, Y2)

# show score on the platform drawn 
# Pygame does not provide a direct way to write text onto a Surface object. The method render() must be used to create a Surface
# object from the text, which then can be blit to the screen. The method render() can only render single lines.
# blit (image print, (x, y))
# render true antialias, make font look smoother edge by blurring pixels
def showScore():
    text = font.render("Balloons Bursted: " + str(SCORE), True, WHITE)
    window.blit(text, (120, WINDOW_HEIGHT - LOWERBOUND + 50))

# pointer for aiming / popping balloons 
def pointer():
    pos = pygame.mouse.get_pos()
    r = 25
    l = 20
    color = LIGHTGREEN
    # loop through every balloon to check if the pointer is onBalloon for each of the balloons
    for i in range(oBalloon):
        if onBalloon(balloons[i].x, balloons[i].y, balloons[i].a, balloons[i].b, pos):
            color = RED # change color
    # x1, y1, xwidth, ywidth, width
    pygame.draw.ellipse(window, color, (pos[0]-r/2, pos[1]-r/2, r, r), 4) # if declared width, it will be an outline, not filled 
    # vertical lines 
    pygame.draw.line(window, color, (pos[0], pos[1] - l/2), (pos[0], pos[1]-l), 4)
    pygame.draw.line(window, color, (pos[0], pos[1] + l/2), (pos[0], pos[1]+l), 4)
    # horizontal lines
    pygame.draw.line(window, color, (pos[0] + l/2, pos[1]), (pos[0]+l, pos[1]), 4)
    pygame.draw.line(window, color, (pos[0] - l/2, pos[1]), (pos[0]-l, pos[1]), 4)

def game():
    # game loops forever
    while True:
        for event in pygame.event.get():
            # quit by closing tab
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # quit by pressing ENTER
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.quit()
                    sys.exit()

            # for popping balloons 
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(oBalloon):
                    balloons[i].burst()
        
        # set up the starting scenario
        window.fill(LIGHTBLUE)
        for i in range(oBalloon):
            balloons[i].draw()
            balloons[i].move()

        pointer()
        platform()
        showScore()

        pygame.display.update()
        clock.tick(70)

game()