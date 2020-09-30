# Import a library of functions called 'pygame'
import pygame
from math import pi
import numpy as np
from random import *


#base define 
scr_w = 900
scr_h = 400
scr_k = 1

# Initialize the game engine
pygame.init()

# Define the colors we will use in RGB format


# Set the height and width of the screen
size = [scr_w, scr_h]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Example code for the draw module")

#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()


BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
#             0           1           2           3           4            5          6             7           8 
color = [(15,82,14),(234,46,67),(146,106,14),(180,97,16),(14,147,145),(255,0,0),(153,227,237),(14,147,37),(249,194,194),(0,0,0)]

def set_back(scr, x, y, w, h, k):
    #back
    pygame.draw.rect(scr, color[7], [x*k//1, (y*k)//2, w*k//1, (h*k)//1]) 
    pygame.draw.rect(scr, color[6], [x*k//1, y*k//1, w*k//1, (h*k)//2])
    #print("background set")
    
def house(scr, x, y, w, h, k): #house
    pygame.draw.polygon(scr, color[5], [[int((x)*k), int((y+30)*k)], [int(((2*x + 2.9 * 40) / 2)*k) , int((y)*k)],[int((x + 2.9 * 40)*k), int((y+30)*k)]], int(30*k))    
    pygame.draw.rect(scr, color[2],    [int((x)*k), int((y+17)*k), int((2.9*40+1)*k), int((2.1*40)*k)])
    pygame.draw.rect(scr, color[3],    [int((x + 40-1)*k) , int((y+1.2*40 -1)*k) , int((0.8*40+2)*k), int((0.7*40 +2)*k)])
    pygame.draw.rect(scr, color[4],    [int((x + 40 )*k), int((y+1.2*40)*k)  , int((0.8*40)*k), int((0.7*40)*k)])    

def sun(scr, x=85*4, y=40, w=0, h=0, k=1, r=20, n= 20):
    #create sun
    c = []; a = [ np.cos((2*np.pi)*(i/n))  for i in range(n) ]; b = [ np.sin((2*np.pi)*(i/n))  for i in range(n) ];
    aa = [ np.cos((2*np.pi)*(i/n)+(2*np.pi)*(1/60))  for i in range(n) ]; bb = [ np.sin((2*np.pi)*(i/n)+(2*np.pi)*(1/60))  for i in range(n) ];
    for i in range(20):
        d = []; d.append(int((a[i]*r + x)*k)); d.append(int((b[i]*r + y)*k)); 
        dd = []; dd.append(int((a[i]*(r-1) + x)*k)); dd.append(int((b[i]*(r-1) + y)*k));
        c.append(d); c.append(dd); 
    #end create sun
    pygame.draw.polygon(screen,color[8], c,1 )
    pygame.draw.circle(screen, color[8] , [x, y], r)

def branch(x,y,r,k,y_bias,x_bias):
    pygame.draw.circle(screen, color[9], [int((20+x+x_bias)*k), int(((y+12)+y_bias)*k)], int((1+r)*k));    pygame.draw.circle(screen, color[0], [int((20+x+x_bias)*k), int(((y+12)+y_bias)*k)], int(r*k));
    
def tree(scr, x, y, w, h, k, n): #tree
    pygame.draw.line(screen, color[9],      [int(x*k),     int((y)*k)], [int(x*k), int((4.8 * 40-128+y)*k)], 12)
    branch(x,y,20,k,0,0); branch(x,y,20,k,5,-15); branch(x,y,20,k,5,-25); branch(x,y,20,k,-5,-15); branch(x,y,20,k,-5,-25);     
            
def cloud(scr,x,y,r,k,x_bias,y_bias):
    pygame.draw.circle(scr, (0, 0, 0), [int((x+x_bias)*k), int((y+y_bias)*k)], int((r+1)*k));    pygame.draw.circle(scr, (255, 255, 255), [int((x+x_bias)*k), int((y+y_bias)*k)], int((r)*k));    

def clouds(scr, x, y, w, h, k, n):
    cloud(scr,x,y,20,k,0,0); cloud(scr,x,y,20,k,15,0); cloud(scr,x,y,20,k,30,0); cloud(scr,x,y,20,k,45,0); cloud(scr,x,y,20,k,60,0); cloud(scr,x,y,20,k,8,12); cloud(scr,x,y,20,k,23,12); cloud(scr,x,y,20,k,38,12);
            
while not done:
    clock.tick(1)

    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop

    screen.fill(WHITE)
    
    set_back(screen, 0, 0, scr_w, scr_h, scr_k)

    #tree
    tree(screen, 4.2*40, 128, 0, 0, 1.2, 0)
    house(screen, 250, 136, 0, 0, 1)
    
    tree(screen, 20*40, 188, 0, 0, 1, 0)
    house(screen, 600, 156, 0, 0, 1)
    
    
    tree(screen, 9*40, 188, 0, 0, 1, 0)
        
    #house
    house(screen, 16, 96, 0, 0, 1.2)
    
    #sun
    sun(screen,r=30)
    # cloud    
    clouds(screen, 10*4, 30, 0, 0, 1, 0); clouds(screen, 60*4, 50, 0, 0, 1, 0); clouds(screen, 200*2, 40, 0, 0, 1.5, 0); clouds(screen, 130*4, 20, 0, 0, 1, 0); clouds(screen, 100*4, 80, 0, 0, 1, 0); 
    pygame.display.flip()

pygame.quit()
