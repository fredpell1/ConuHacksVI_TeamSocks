import pygame 
import random

class apple(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.position = ((random.randrange(0, 25), random.randrange(0, 25)))
        self.eaten = False

    def update(self):
        
        self.position = ((random.randrange(0, 25), random.randrange(0, 25)))

    def eaten(self):
        if not self.eaten:
            self.eaten = True

    
    def not_eaten(self):
        self.eaten = False
