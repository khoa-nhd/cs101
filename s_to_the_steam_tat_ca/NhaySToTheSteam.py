
import pygame as pg
import sys, os
pg.init()
clock = pg.time.Clock()


WIDTH = 724 
HEIGHT = 540 

FPS = 60

IMAGE_WIDTH = 720 
IMAGE_HEIGHT = 540
OFFSET = 100

ASSETS_PATH = './'
timeBetweenPicture = 0.95
timeBetweenPicture1 = 0.5
moves = {
    'move0': {
        'time': 0,
        'sprites': [
            '0.png'
            ]
        },
    'move1': {
        'time': timeBetweenPicture,
        'sprites': [
            '1.1.png',
            '1.2.png',
            '1.3.png'
            ]
        },
    'move2': {
        'time': timeBetweenPicture,
        'sprites': [
            '2.1.png',
            '2.2.png'
            ]
        },
    'move3': {
        'time': timeBetweenPicture,
        'sprites': [
            '3.1.png',
            '3.2.png'
            ]
        },
    'move4': {
        'time': timeBetweenPicture,
        'sprites': [
            '4.1.png',
           '4.2.png'
            ]
        },
    'move5': {
        'time': timeBetweenPicture,
        'sprites': [
            '5.1.png',
            '5.2.png'
            ]
        },
    'move6': {
        'time': timeBetweenPicture,
        'sprites': [
            '6.1.png',
            '6.2.png'
            ]
        },
    'move7': {
        'time': timeBetweenPicture1,
        'sprites': [
            '7.1.png',
            '7.2.png',
            '7.3.png'
            ]
        }
    }
procedure = [
    'move0',
    'move1',
    'move2',
    'move3',
    'move4',
    'move1',
    'move2',
    'move3',
    'move4',
    'move5',
    'move6',
    'move3',
    'move4',
    'move5',
    'move6',
    'move3',
    'move7',
    'move7',
    'move7'
    ]

class Dancer(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.moves = {}
        self.current_move = 0
        self.current_sprite = 0
        self.frames_per_image = 0
        self.count = 0
        self.image = None
        self.rect = None
        
    def init(self):
        self.load_images()
        self.draw_image(self.moves[procedure[self.current_move]]['sprites'][self.current_sprite])
    
    def load_images(self):
        count = 0
        for move in moves:
            count+=1
            sprites = []
            for sprite in moves[move]['sprites']:
                sprites.append(pg.image.load(os.path.join(ASSETS_PATH+move,sprite)))
            self.moves[move]= {
                'time': moves[move]['time'],
                'sprites': sprites
                }
    def draw_image(self,sprite):
        self.image = sprite
        self.image = pg.transform.scale(self.image, (IMAGE_WIDTH, IMAGE_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.topleft = [0,0]
      
    def update(self):
        number_of_moves = len(procedure)
        if self.current_move < number_of_moves:
            number_of_sprites = len(self.moves[procedure[self.current_move]]['sprites'])
            time_of_move = self.moves[procedure[self.current_move]]['time']
            self.frames_per_image = FPS*time_of_move//number_of_sprites
            
            if self.count >= self.frames_per_image:
                if self.current_sprite < number_of_sprites:
                    self.next_sprite()
                else:
                    self.next_move()
                    
            self.count += 1
            

    def next_sprite(self):
        sprite = self.moves[procedure[self.current_move]]['sprites'][self.current_sprite]
        self.draw_image(sprite)
        self.count = 0
        self.current_sprite += 1
    
    def next_move(self):
        self.current_move += 1
        self.current_sprite = 0
    

def main():
    screen = pg.display.set_mode((WIDTH,HEIGHT))
    pg.display.set_caption("Nhảy bài S to the team!!!")
    moving_sprites = pg.sprite.Group()
    dancer = Dancer()
    dancer.init()
    moving_sprites.add(dancer)

    pg.mixer.init()
    pg.mixer.music.load(os.path.join(ASSETS_PATH,'music.wav'))
    pg.mixer.music.play(-1)
    
   
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        moving_sprites.update()
        moving_sprites.draw(screen)
        
        pg.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
    pg.quit()
