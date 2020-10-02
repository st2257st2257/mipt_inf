import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 700))

cloud=(168, 186, 186)






"""
#back
rect(screen, (255, 255, 255), (0, 0, 500, 450))
rect(screen, (183, 196, 200), (0, 0, 500, 445))
rect(screen, (83, 108, 103, 0), (0, 450, 500, 250))
ellipse(screen, cloud, (-100, 50, 400, 100))
"""


#front








def back(scr):
    rect(scr, (255, 255, 255), (0, 0, 500, 450))
    rect(scr, (183, 196, 200), (0, 0, 500, 445))
    rect(scr, (83, 108, 103, 0), (0, 450, 500, 250))
    ellipse(scr, (168, 186, 186), (-100, 50, 400, 100))


def dcloud(scr,x=90,y=200,a=500,b=130):
    ellipse(screen, cloud, (x, y, a, b))


def house(scr,  color , x=50, y=100, w=130, h=490):
    rect(scr, color , (x, y, w, h))


def car(scr,xx,yy,k):

    x=-10   #x_bias
    y=-560  #y_bias

    rect(screen, (100, 200, 200), (xx+(x+200)*k, yy+(y+600)*k, 200*k, 50*k))
    rect(screen, (100, 200, 200), (xx+(x+240)*k, yy+(y+570)*k, 110*k, 30*k))
    rect(screen, (200, 200, 255), (xx+(x+250)*k, yy+(y+575)*k, 40*k, 25*k))
    rect(screen, (200, 200, 255), (xx+(x+300)*k, yy+(y+575)*k, 40*k, 25*k))

    ellipse(screen, (0, 0, 0), (xx+(x+350)*k, yy+(y+630)*k,40*k, 40*k))

    ellipse(screen, (0, 0, 0), (xx+(x+220)*k, yy+(y+630)*k, 40*k, 40*k))
    rect(screen, (0, 0, 0), (xx+(x+185)*k, yy+(y+635)*k, 15*k, 7*k))

    ellipse(screen, (130, 150, 150), (xx+(x+40)*k, yy+(y+610)*k, 130*k, 40*k))
    ellipse(screen, (130, 150, 150), (xx+(x+10)*k, yy+(y+560)*k, 130*k, 40*k))





back(screen)

house(screen, (147, 167, 172), 10, 20, 100, 450)
house(screen, (219, 227, 226), 400, 10, 95, 460)


##ellipse_surface = pygame.Surface((50, 50), pygame.SRCALPHA)
##ellipse_surface.fill((255, 100, 100, 100))
dcloud(screen, 150, -20, 400, 123)

house(screen, (111, 145, 138), 350, 100, 100, 500)
house(screen, (147, 172, 167), 150, 90, 80, 450)
house(screen, (183, 200, 196), 50, 100, 130, 490)


dcloud(screen, 90, 200, 500, 130)
dcloud(screen, -20, 600, 600, 180)

car(screen,10,400,1)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
