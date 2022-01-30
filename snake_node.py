import pygame as pg

class snake_container():

    dx = 25
    dy = 25

    def __init__(self, head_pos = (200,200,25,25), color = (255,0,0)):
        
        self.body = [snake_node(head_pos, color=color), snake_node((200,225,25,25)), snake_node((200,250,25,25))]
        self.direction = 'UP'
        self.color  = color


    def move(self, direction):
        
        #update the direction
        self.direction = direction

        
        #set the direction
        if direction == 'UP':
            x_sign = 0
            y_sign = -1 #coord system is reversed
        elif direction == 'DOWN':
            x_sign = 0
            y_sign = 1
        elif direction == 'LEFT':
            x_sign = -1
            y_sign = 0
        elif direction == 'RIGHT':
            x_sign = 1
            y_sign = 0

        last_pos = self.body[0].rect
        for i,b in enumerate(self.body):        
            if i == 0:
               self.body[i].rect = (b.rect[0] + x_sign * snake_container.dx, b.rect[1] + y_sign * snake_container.dy, b.rect[2], b.rect[3])
            else:
                temp = last_pos
                last_pos = self.body[i].rect
                self.body[i].rect = temp


    # def draw(self, surface, background):
    #     for rec in self.body:
    #         pg.draw.rect(surface, self.color, rec)
        

class snake_node(pg.sprite.Sprite):

    def __init__(self, pos = (200,200,25,25), color = (255,0,0)):
        pg.sprite.Sprite.__init__(self)
        self.rect = pos
        self.image = pg.Surface([25,25])
        self.image.fill(color)
        self.color = color




s = snake_container()
print(s.body[0].rect, s.body[1].rect, s.body[2].rect)
s.move('RIGHT')
print(s.body[0].rect, s.body[1].rect, s.body[2].rect)
s.move('RIGHT')
print(s.body[0].rect, s.body[1].rect, s.body[2].rect)
