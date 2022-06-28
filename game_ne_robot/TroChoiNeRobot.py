import pygame

class Door:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        sprite = pygame.image.load("sprites/door.png")
        self.image = pygame.transform.scale(sprite, (80, 80))

class Robot:
    def __init__(self, x, y, x_heading, y_heading, hinh_anh):
        self.x = x
        self.y = y
        self.x_heading = x_heading
        self.y_heading = y_heading
        sprite = pygame.image.load(hinh_anh)
        self.image = pygame.transform.scale(sprite, (60, 60))

    def move(self):
        self.x = self.x + self.x_heading
        self.y = self.y + self.y_heading
        
        if self.x > 440: self.x_heading = - self.x_heading
        if self.x < 0:   self.x_heading = - self.x_heading
        if self.y > 440: self.y_heading = - self.y_heading
        if self.y < 0:   self.y_heading = - self.y_heading

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        sprite = pygame.image.load("sprites/trau.png")
        self.image = pygame.transform.scale(sprite, (50, 80))
    
    def move(self, change_x, change_y):
        new_x = self.x + change_x
        new_y = self.y + change_y

        if new_x > 0 and new_x < 450:
            self.x = new_x
        if new_y > 0 and new_y < 420:
            self.y = new_y

    def touch(self, obj):
        mask1 = pygame.mask.from_surface(self.image)
        mask2 = pygame.mask.from_surface(obj.image)
        offset_x = obj.x - self.x
        offset_y = obj.y - self.y
        if mask1.overlap(mask2, (offset_x, offset_y)):
            return True
        else:
            return False

class Game:
    def __init__(self):
        pygame.init()
        self.WIDTH = 500  
        self.HEIGHT = 500  
        self.screen = pygame.display.set_mode([self.WIDTH, self.HEIGHT])

        self.clock = pygame.time.Clock()
        self.FPS = 100    
        self.font = pygame.font.SysFont("Times New Roman", 30, bold=True)

    def draw_background(self):
        BLACK = (0, 0, 0)
        self.screen.fill(BLACK)
        background = pygame.image.load("sprites/background.png").convert_alpha()
        background = pygame.transform.scale(background, (self.WIDTH, self.HEIGHT))
        self.screen.blit(background, (0, 0))
    
    def draw_new_frame(self):
        pygame.display.flip()
        self.clock.tick(self.FPS)

    def draw_object(self, obj):
        self.screen.blit(obj.image, (obj.x, obj.y))

    def draw_result(self, win):

        YELLOW = (255, 255, 0)
        if win:
            text = self.font.render("YOU WON!! YOU THE BEST!!", 1, YELLOW)
            self.screen.blit(text, (50, 250))
        else:
            text = self.font.render("GAME OVER!!", 1, YELLOW)
            self.screen.blit(text, (150, 250))

    def is_quit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        return False

    def start(self):
        trau = Player(100, 250)
        door = Door(375, 20)

        robots = [
            Robot(100, 400, 5, 0, "sprites/robot1.png"),
            Robot(300, 300, 0, 5, "sprites/robot2.png"),
            Robot(200, 200, 10, 2, "sprites/robot3.png"),
            Robot(100, 100, -2, -5, "sprites/robot4.png")
        ]

        end_game = False
        is_won = False

        running = True
        while running:
            if self.is_quit():
                running = False

            self.draw_background()
            
            if not end_game:
                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_UP]:    trau.move( 0, -5)
                if pressed[pygame.K_DOWN]:  trau.move( 0,  5)
                if pressed[pygame.K_LEFT]:  trau.move(-5,  0)
                if pressed[pygame.K_RIGHT]: trau.move( 5,  0)

                if trau.touch(door):
                    print("YOU WON!! YOU THE BEST!!")
                    end_game = True
                    is_won = True

                for robot in robots:
                    robot.move()

                    if trau.touch(robot):
                        print("GAME OVER!!")
                        end_game = True
                        is_won = False
            
            self.draw_object(trau)
            for robot in robots:
                self.draw_object(robot)
            self.draw_object(door)
            
            if end_game:
                self.draw_result(is_won)

            self.draw_new_frame()
            
        pygame.quit()

game = Game()
game.start()