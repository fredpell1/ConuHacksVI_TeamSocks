from msilib.schema import Icon
import pygame_menu
import pygame as pg
from snake import Snake
from apple import apple
from snake_node import  snake_container
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
SCREEN_WIDTH=625
SCREEN_HEIGHT=625
FPS=7
BLOCKSIZE = 25 

def start_the_game():
    SCREEN.fill(BLACK)
    #SCREEN.blit(back,(0,0))
    
    s = snake_container()
    allsprites = pg.sprite.RenderPlain(s.body)
    flag= True
    while flag:
        CLOCK.tick(FPS)
        SCREEN.fill(BLACK)
        #SCREEN.blit(back,(0,0))
        drawGrid()
        last_move = s.direction
        for event in pg.event.get():
            if event.type == pg.QUIT:
                flag= False
            elif event.type == pg.KEYDOWN:
                
                if event.key == pg.K_ESCAPE:
                    flag = False

                elif event.key == pg.K_LEFT:
                    s.move('LEFT')
                    last_move = 'LEFT'
                elif event.key == pg.K_RIGHT:
                    #s.move(1,0)
                    #s.direction = 'RIGHT'
                    s.move('RIGHT')
                    last_move = 'RIGHT'
                elif event.key == pg.K_UP:
                    #s.move(0,-1) #coord system is flipped
                    #s.direction = 'UP'
                    s.move('UP')
                    last_move = 'UP'
                elif event.key == pg.K_DOWN:
                    #s.move(0,1)
                    #s.direction = 'DOWN'
                    s.move('DOWN')
                    last_move = 'DOWN'

        #allsprites.add(s.body)
        s.move(last_move)
        #allsprites.update()
        SCREEN.blit(back, (0,0))
        allsprites.draw(SCREEN)
        
        
        
        

        #SCREEN.blit(back, (0,0))
        
        pg.display.update()

    pass


back=pg.image.load('data\Grass.jpg')

def main():
    global SCREEN, CLOCK
    pg.init()
   
    SCREEN = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pg.display.set_caption('SNAKEHACK')
    CLOCK = pg.time.Clock()
    a = pg.image.load('data\Apple.png')
    pg.display.set_icon(a)
    menu = pygame_menu.Menu('SNAKEHACK', 625, 625,theme=pygame_menu.themes.THEME_GREEN)
    
    menu.add.button('Play', start_the_game)
    menu.add.button('AI', start_the_game)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    
    menu.mainloop(SCREEN)




def drawGrid():
    
    for x in range(0, SCREEN_WIDTH,BLOCKSIZE):
        for y in range(0, SCREEN_HEIGHT, BLOCKSIZE):
            rect = pg.Rect(x, y,BLOCKSIZE, BLOCKSIZE)
            pg.draw.rect(back, WHITE, rect, 1)
   


if __name__ == '__main__':
    main()