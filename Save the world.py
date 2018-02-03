# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 11:29:38 2018

@author: rohit
"""

import pygame,time,random,sys
from pygame.locals import *

pygame.init()
display_width,display_height = 1280,720
RESOLUTION = (display_width,display_height)
DISPLAYSURF = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption("Save The World!")
clock = pygame.time.Clock()
# define colors
BLACK = (0,0,0)
WHITE = (255,255,255)

#add menu screen


#main game loop
# anything after the game has started is written inside this loop
ball_image= pygame.image.load('images/fireball.png')


def load_image(name):
     return pygame.image.load(name)
class flames:
    def __init__(self):
        self.image = load_image("images/flames_for_games_by_naruhanaluvr_without_background.png")
        self.width, self.height = 1280,200
        self.position = (0, 0)

class plane:
    def __init__(self):
        self.image = pygame.image.load("images/plane1.png")
        self.width = 114
        self.height = 123
    def text_objects(self,text,font):
        textSurface = font.render(text, True, WHITE)
        return textSurface, textSurface.get_rect()

    def message_display(self,text):
        largeText = pygame.font.Font("freesansbold.ttf",115)
        textSurf,textRect = self.text_objects(text,largeText)
        textRect.center = ((display_width/2),(display_height/2))
        DISPLAYSURF.blit(textSurf,textRect)

        pygame.display.update()

        time.sleep(2)
        gameloop()

    def crash(self) :
        self.message_display("you crashed")


    def planeRender (self,x,y):
        DISPLAYSURF.blit(self.image,(x,y))


'''def firewall():
    wall_image = pygame.image.load('images/flames.png')
    DISPLAYSURF.blit(wall_image,(display_width-100,0))'''
def gameloop():
    fireball1_position_x = random.randint(0,display_width - 100)
    fireball1_position_y = -((display_height+104)/4)*1

    fireball2_position_x = random.randint(0,display_width - 100)
    fireball2_position_y = -((display_height+104)/4)*2

    fireball3_position_x = random.randint(0,display_width - 100)
    fireball3_position_y = -((display_height+104)/4)*3

    fireball4_position_x = random.randint(0,display_width - 100)
    fireball4_position_y = -((display_height+104)/4)*4

    jet = plane()
    x = display_width/2 - jet.width/2
    y = display_height - jet.height
    xchange = 0
    while True:
        DISPLAYSURF.fill(BLACK)
        firewall = flames()
        DISPLAYSURF.blit(firewall.image,firewall.position)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT :
                    xchange = -10

                if event.key == pygame.K_RIGHT:
                    xchange = 10

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    xchange = 0
        x = x + xchange
        DISPLAYSURF.blit(ball_image,(fireball1_position_x,fireball1_position_y))
        fireball1_position_y += 5

        DISPLAYSURF.blit(ball_image,(fireball2_position_x,fireball2_position_y))
        fireball2_position_y += 5

        DISPLAYSURF.blit(ball_image,(fireball3_position_x,fireball3_position_y))
        fireball3_position_y += 5

        DISPLAYSURF.blit(ball_image,(fireball4_position_x,fireball4_position_y))
        fireball4_position_y += 5

        if fireball1_position_y > display_height:
            fireball1_position_x = random.randint(0,display_width - 240)
            fireball1_position_y = -104

        if fireball2_position_y > display_height:
            fireball2_position_x = random.randint(0,display_width - 240)
            fireball2_position_y = -104

        if fireball3_position_y > display_height:
            fireball3_position_x = random.randint(0,display_width - 240)
            fireball3_position_y = -104

        if fireball4_position_y > display_height:
            fireball4_position_x = random.randint(0,display_width - 240)
            fireball4_position_y = -104
        jet.planeRender(x,y)
        if x < 0 or x > display_width - jet.width:
            jet.crash()
        pygame.display.update()
        clock.tick(60)
gameloop()
