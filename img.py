# Import a library of functions called 'pygame'
import pygame
from math import pi
import numpy as np
from random import *





# Initialize the game engine
pygame.init()

# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

# Set the height and width of the screen
size = [400, 300]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Example code for the draw module")

#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()



#             0           1           2           3           4            5          6             7           8 
color = [(15,82,14),(234,46,67),(146,106,14),(180,97,16),(14,147,145),(255,0,0),(153,227,237),(14,147,37),(249,194,194),(0,0,0)]


#create sun
c = []
a = [ np.cos((2*np.pi)*(i/20))  for i in range(20) ]
b = [ np.sin((2*np.pi)*(i/20))  for i in range(20) ]
aa = [ np.cos((2*np.pi)*(i/20)+(2*np.pi)*(1/60))  for i in range(20) ]
bb = [ np.sin((2*np.pi)*(i/20)+(2*np.pi)*(1/60))  for i in range(20) ]
for i in range(20):
    d = []; d.append(a[i]*20 + 8.5*40); d.append(b[i]*20 + 40);
    dd = []; dd.append(a[i] * 19 + 8.5 * 40); dd.append(b[i] * 19 + 40);

    c.append(d)
    c.append(dd)

#end create sun
print(c)


while not done:

    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(1)

    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop

    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.

    # Clear the screen and set the screen background
    screen.fill(WHITE)
    """
    # Draw on the screen a GREEN line from (0, 0) to (50, 30)
    # 5 pixels wide.
    pygame.draw.line(screen, GREEN, [0, 0], [50,30], 5)
    # Draw on the screen 3 BLACK lines, each 5 pixels wide.
    # The 'False' means the first and last points are not connected.
    pygame.draw.lines(screen, BLACK, False, [[0, 80], [50, 90], [200, 80], [220, 30]], 5)
    # Draw on the screen a GREEN line from (0, 50) to (50, 80)
    # Because it is an antialiased line, it is 1 pixel wide.
    pygame.draw.aaline(screen, GREEN, [0, 50],[50, 80], True)
    # Draw a rectangle outline
    pygame.draw.rect(screen, BLACK, [75, 10, 50, 20], 2)
    # Draw a solid rectangle
    pygame.draw.rect(screen, BLACK, [150, 10, 50, 20])
 # Draw an ellipse outline, using a rectangle as the outside boundaries
    pygame.draw.ellipse(screen, RED, [225, 10, 50, 20], 2)
    # Draw an solid ellipse, using a rectangle as the outside boundaries
    pygame.draw.ellipse(screen, RED, [300, 10, 50, 20])
    # This draws a triangle using the polygon command
    pygame.draw.polygon(screen, BLACK, [[100, 100], [0, 200], [200, 200]], 5)
    # Draw an arc as part of an ellipse.
    # Use radians to determine what angle to draw.
    pygame.draw.arc(screen, BLACK,[210, 75, 150, 125], 0, pi/2, 2)
    pygame.draw.arc(screen, GREEN,[210, 75, 150, 125], pi/2, pi, 2)
    pygame.draw.arc(screen, BLUE, [210, 75, 150, 125], pi,3*pi/2, 2)
    pygame.draw.arc(screen, RED,  [210, 75, 150, 125], 3*pi/2, 2*pi, 2)
"""

    #back
    pygame.draw.rect(screen, color[6], [0, 0, 400, 150])
    pygame.draw.rect(screen, color[7], [0, 150, 400, 300])

    #tree
    pygame.draw.line(screen, color[9], [6.9 * 40, 3.2 * 40], [6.9 * 40, 4.8 * 40], 12)
    pygame.draw.circle(screen, color[0], [7*40, 150-20], 20);        pygame.draw.circle(screen, color[0], [7*40, 150-20], 20);
    pygame.draw.circle(screen, (0, 0, 0), [7*40+5, 150-20+5], 20);    pygame.draw.circle(screen, color[0], [7*40+5, 150-20+5], 20);
    pygame.draw.circle(screen, color[0], [7*40+5, 150-20-5], 20);    pygame.draw.circle(screen, color[0], [7*40+5, 150-20+5], 20);
    pygame.draw.circle(screen, (0, 255, 0), [7*40-5, 150-20+5], 20);    pygame.draw.circle(screen, color[0], [7*40+5, 150-20+5], 20);
    pygame.draw.circle(screen, (0, 55, 0), [7*40-5, 150-20-5], 20);    pygame.draw.circle(screen, color[0], [7*40+5, 150-20+5], 20);

    #house
    pygame.draw.polygon(screen, color[5], [[0.4 * 40, 3.1 * 40], [(0.4 * 40 + 2.9 * 40) / 2 , 3.1 * 40 - 30],[0.4 * 40 + 2.9 * 40, 3.1 * 40]], 30)    
    pygame.draw.rect(screen, color[2], [0.4*40, 3.1*40-13, 2.9*40+1, 2.1*40])
    pygame.draw.rect(screen, color[3], [ 1.4*40-1 , 3.6*40 -1 , 0.8*40+2, 0.7*40 +2])
    pygame.draw.rect(screen, color[4], [ 1.4*40 , 3.6*40  , 0.8*40, 0.7*40 ])


    #sun
    pygame.draw.polygon(screen,color[8], c,1 )
    pygame.draw.circle(screen, color[8] , [85*4, 40], 20)

    # cloud
    pygame.draw.circle(screen, (0, 0, 0),[50 * 4, 30], 21);  pygame.draw.circle(screen, (255, 255, 255),[50 * 4, 30], 20);

    pygame.draw.circle(screen, (0, 0, 0), [50 * 4+15, 30], 21);
    pygame.draw.circle(screen, (255, 255, 255), [50 * 4+15, 30], 20);

    pygame.draw.circle(screen, (0, 0, 0), [50 * 4+30, 30], 21);
    pygame.draw.circle(screen, (255, 255, 255), [50 * 4+30, 30], 20);

    pygame.draw.circle(screen, (0, 0, 0), [50 * 4+45, 30], 21);
    pygame.draw.circle(screen, (255, 255, 255), [50 * 4+45, 30], 20);
    pygame.draw.circle(screen, (0, 0, 0), [50 * 4+60, 30], 21);
    pygame.draw.circle(screen, (255, 255, 255), [50 * 4+60, 30], 20);


    pygame.draw.circle(screen, (0, 0, 0), [50 * 4 + 8, 30+12], 21);
    pygame.draw.circle(screen, (255, 255, 255), [50 * 4 + 8, 30+12], 20);

    pygame.draw.circle(screen, (0, 0, 0), [50 * 4 + 23, 30+12], 21);
    pygame.draw.circle(screen, (255, 255, 255), [50 * 4 + 23, 30+12], 20);

    pygame.draw.circle(screen, (0, 0, 0), [50 * 4 + 38, 30+12], 21);
    pygame.draw.circle(screen, (255, 255, 255), [50 * 4 + 38, 30+12], 20);


    """
    
    # Draw a circle
    pygame.draw.circle(screen, (255,255,0) , [150, 150], 100)
    pygame.draw.circle(screen, (255, 0, 0), [150 - 26, 150-20], 20)
    pygame.draw.circle(screen, (255, 0, 0), [150 + 28, 150-20], 20)
    pygame.draw.circle(screen, (0, 0, 0), [150 - 26, 150-20], 8)
    pygame.draw.circle(screen, (0, 0, 0), [150+28, 150-20], 8)
    pygame.draw.rect(screen, BLACK, [150-45, 150+30, 90, 15])
    pygame.draw.line(screen, BLACK, [150 - 20, 150-20-20], [150 - 26-40, 150-20-20-30], 5)
    pygame.draw.line(screen, BLACK, [150 + 22, 150-20-20], [150 + 26+40, 150-20-20-30], 5)
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands."""
    pygame.display.flip()



# Be IDLE friendly


pygame.quit()
