import pygame
import random 
pygame.init() 
screen=pygame.display.set_mode((500,500))
def shape_dockalien(surface,x,y):
    pygame.draw.ellipse(surface,(0,255,0),(x-20,y-15,40,30))
    pygame.draw.circle(surface,(0,255,0),(x,y-20),10)
    pygame.draw.circle(surface,(255,0,15),(x-7,y-22),5)
    pygame.draw.line(surface,(0,255,0),(x-10,y-35),(x+10,y-35),3)