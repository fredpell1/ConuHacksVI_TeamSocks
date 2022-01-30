import pygame as pg
import random

class apple(pg.sprite.Sprite):
    def __init__(self, color = (255,0,0)):
        pg.sprite.Sprite.__init__(self)
        self.position = ((random.randrange(0, 400), random.randrange(0, 400)))
        self.rect = self.position
        self.image.fill(color)
        self.color = color
        self.isEaten = False


    def update(self):
        if self.isEaten is True:
            self.position = ((random.randrange(0, 400), random.randrange(0, 400)))


    def digest(self):
        self.isEaten = True
