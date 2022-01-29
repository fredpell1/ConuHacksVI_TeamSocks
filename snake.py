#imports
import os
import pygame as pg
from fileUtil import load_image, load_sound

if not pg.font:
    print("Warning, fonts disabled")
if not pg.mixer:
    print("Warning, sound disabled")

class Snake(pg.sprite.Sprite):


    """Moves a snake critter across the screen. 
    
    """

    def __init__(self):
        pg.sprite.Sprite.__init__(self) #call sprite initializer
        self.image = pg.image.load(r'data\block.jpg')
        self.rect = self.image.get_rect()
        self.pos = (10,10)
        self.speed = 10


    def update(self):
        
        self.rect.topleft = self.pos
        self.rect.move_ip(0,0)
    

    def move(self, x_sign, y_sign):
        x = self.pos[0]
        y = self.pos[1]
        x += x + x_sign * self.speed
        y += y + y_sign * self.speed
        self.pos = (x,y)
        print(self.pos)
        
