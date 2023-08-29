''' Code for Calculating the value of Pi by collision between two blocks.
'''

### Sahil Islam ###
### 02/06/2020 ###

import pygame
import numpy as np
from fractions import Fraction
import time

pygame.init()

#pygame.mixer.music.load('Tick.mp3')
display_width = 1100
display_height = 650

black = [0, 0, 0]
white = [255, 255, 255]

display_surface = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()
pygame.display.set_caption("Pi Collision")


def box(x, y, s):
    pygame.draw.rect(display_surface, white, [np.float128(x), np.float128(y) - s, s, s])


def collisionVel(m1, m2, u1, u2):
    totalMass = m1 + m2
    #v1 = np.float128((m1 - m2) / totalMass) * u1 + np.float128(2 * m2 / totalMass) * u2
    v1=Fraction((m1-m2),totalMass)* u1 + Fraction(2*m2,totalMass ) * u2
    #v2 = np.float128(2 * m1 / totalMass) * u1 + np.float128((m2 - m1) / totalMass) * u2
    v2=Fraction(2*m1, totalMass) * u1 + Fraction((m2-m1),totalMass)*u2
    return v1, v2


def collisonShow(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render(("Pi= " + str(count)), True, white)
    display_surface.blit(text, (0, 0))


digit = 2

massSmall = 1
massBig = pow(10, digit)

widthSmall = 25
widthBig = 50

velocitySmall = 0
velocityBig = -5

positionSmall = Fraction(display_width , 4)
positionBig = Fraction(display_height , 2) 

yposition=Fraction(display_height , Fraction(3,2))

count = 0
c=0

game_exit = False
while not game_exit:
    display_surface.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    positionSmall += velocitySmall
    positionBig += velocityBig

    newVelBig, newVelSmall = collisionVel(massBig, massSmall, velocityBig, velocitySmall)

    if positionBig <= 0:
        velocityBig *= -1
        count += 1
        #pygame.mixer.music.play(0)
    
    
        
        
    if positionSmall <= 0:
        velocitySmall *= -1
        count += 1
        #pygame.mixer.music.play(0)

    if positionBig <= positionSmall + widthSmall or positionSmall + widthSmall >= positionBig:
        velocityBig = newVelBig
        velocitySmall = newVelSmall
        count += 1
        #pygame.mixer.music.play(0)

    #if positionBig<display_width:
        #print(positionSmall, positionBig)
        #time.sleep(2)
    if positionSmall<0:
        #print("Out")
        c +=1

    #print(c)


    box(positionSmall, yposition , widthSmall)
    box(positionBig,yposition, widthBig)
    pi = count / 10 ** digit
    collisonShow(pi)

    pygame.display.update()
    clock.tick(30)
