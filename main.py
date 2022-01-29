from cmath import rect
from operator import truediv
from tarfile import BLOCKSIZE
from turtle import update
import pygame as pg
from snake import Snake
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
SCREEN_WIDTH=625
SCREEN_HEIGHT=625
FPS=10
BLOCKSIZE = 25 


back=pg.image.load('data\Grass.jpg')

def main():
    global SCREEN, CLOCK
    pg.init()
    s = Snake()
    SCREEN = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    CLOCK = pg.time.Clock()
    SCREEN.fill(BLACK)
    SCREEN.blit(back,(0,0))

    allsprites = pg.sprite.RenderPlain(s)

    flag= True
    while flag:
        CLOCK.tick(FPS)
        drawGrid()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                flag= False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    flag = False

                elif event.key == pg.K_LEFT:
                    s.move(-1, 0)
                    s.direction = 'LEFT'
                elif event.key == pg.K_RIGHT:
                    s.move(1,0)
                    s.direction = 'RIGHT'
                elif event.key == pg.K_UP:
                    s.move(0,-1) #coord system is flipped
                    s.direction = 'UP'
                elif event.key == pg.K_DOWN:
                    s.move(0,1)
                    s.direction = 'DOWN'

                

        allsprites.update()

        SCREEN.blit(back, (0,0))
        allsprites.draw(SCREEN)
        pg.display.update()


def drawGrid():
    
    for x in range(0, SCREEN_WIDTH,BLOCKSIZE):
        for y in range(0, SCREEN_HEIGHT, BLOCKSIZE):
            rect = pg.Rect(x, y,BLOCKSIZE, BLOCKSIZE)
            pg.draw.rect(SCREEN, WHITE, rect, 1)
   


if __name__ == '__main__':
    main()