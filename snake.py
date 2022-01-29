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
        self.image = pg.image.load(r'data\Snake.jpg')
        self.image =pg.transform.scale(self.image, (25,25))
        self.rect = self.image.get_rect()
        self.pos = (200,200)
        self.speed = 10
        self.direction = 'UP' #can be UP, DOWN, RIGHT, LEFT


    def update(self):
        if self.direction == 'UP':
            self.move(0,-1)
        elif self.direction == 'DOWN':
            self.move(0,1)
        elif self.direction == 'LEFT':
            self.move(-1,0)
        elif self.direction == 'RIGHT':
            self.move(1,0)
        
        self.rect.topleft = self.pos
        self.rect.move_ip(0,0)
    

    def move(self, x_sign, y_sign):
        x = self.pos[0]
        y = self.pos[1]
        
        x = x + x_sign * self.speed
        y = y + y_sign * self.speed
        self.pos = (x,y)
        print(self.pos)
        
