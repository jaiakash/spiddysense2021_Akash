import sys
import os
import math
import pygame
from pygame.locals import *
from pygame import mixer
from math import *
import random
pygame.init()

screen = pygame.display.set_mode((720, 720))
clk = pygame.time.Clock()

# Sound
mixer.music.load("background.wav")
mixer.music.play(-1)

#font
velo = pygame.font.Font('freesansbold.ttf',24)

# Title and TODO icon
pygame.display.set_caption("Rocket game")

#background
background = pygame.image.load('back.jpg')

#Rocket
rocket_img = pygame.image.load('rocket.png')
rkt_x = 360
rkt_y = 650

#Show velocity
def show_vel(cur_vel):
    veloc="Velocity : "+cur_vel
    vl=velo.render(veloc,True, (255,255,255))
    screen.blit(vl,(10,10))


def move_rkt(mouse_X,mouse_Y):
    rkt_copy=rocket_img.copy()
    global rkt_x,rkt_y
    dist_x=(mouse_X-rkt_x)/10
    dist_y=(mouse_Y-rkt_y)/10

    #Show Velocity with 2 decimal place
    v=str(math.sqrt(dist_x*dist_x+dist_y*dist_y)/10)
    show_vel(v[0:4])

    # Linear movement of Rocket
    rkt_x+=dist_x
    rkt_y+=dist_y

    # Angular movement of Rocket
    angle=math.degrees(math.atan(dist_y/dist_x))
    if dist_y>0:
        angle+=180
    rkt_copy = pygame.transform.rotate(rkt_copy,45+angle)
    #draw the rocket
    screen.blit(rkt_copy, (rkt_x-20, rkt_y))

while True:
    clk.tick(10)

    screen.fill((0,0,0))
    screen.blit(background,(0,0))

    #----------this is called when we need to quit the window------------------#
    for event in pygame.event.get():
       if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #------------------setting destination to be where cursor is placed--------##
    if pygame.mouse.get_pressed():
        m_X,m_Y = pygame.mouse.get_pos()
        move_rkt(m_X,m_Y)

    #screen.blit(rocket_img, (rkt_x, rkt_y))

    pygame.display.update()
