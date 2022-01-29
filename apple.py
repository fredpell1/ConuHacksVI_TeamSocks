import pygame as pg
import random

class apple(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(r'data\Apple.png')
        self.image = pg.transform.scale(self.image, (25,25))
        self.rect = self.image.get_rect()
        self.rect = (random.randrange(0, 600), random.randrange(0, 600))
        self.eaten = False

    def update(self):
        #self.position = ((random.randrange(0, 25), random.randrange(0, 25)))
        pass

    def eaten(self):
        if not self.eaten:
            self.eaten = True

    
    def not_eaten(self):
        self.eaten = False
