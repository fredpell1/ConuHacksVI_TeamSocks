import pygame as pg
import random

class apple(pg.sprite.Sprite):
    def __init__(self, color = (255, 0, 0)):
        pg.sprite.Sprite.__init__(self)
        #self.image = pg.image.load(r'data\Apple.png')
        #self.image = pg.transform.scale(self.image, (25,25))
        #self.rect = self.image.get_rect()
        #self.rect = (random.randrange(0, 600), random.randrange(0, 600))
        self.rect = (random.randrange(25, 400, 25), random.randrange(25, 400, 25), 25, 25)
        self.image = pg.Surface([25, 25])
        self.image.fill(color)
        self.isEaten = False

    def update(self):
        #self.position = ((random.randrange(0, 25), random.randrange(0, 25)))
        if self.isEaten:
            self.rect = (random.randrange(25, 400, 25), random.randrange(25, 400, 25), 25, 25)
            self.isEaten = False



