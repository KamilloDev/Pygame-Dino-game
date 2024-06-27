import pygame, sys, random
from data.scripts.dino import *
from data.scripts.enemies import  *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 500))
        self.display = pygame.Surface((400, 250))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Dino Run')
        self.icon = pygame.image.load('data/imgs/dino/Dino.png').convert_alpha()
        pygame.display.set_icon(self.icon)

        self.dino = pygame.sprite.GroupSingle(Dino())
        self.enemies = pygame.sprite.Group(Enemies())
        self.start = 0
        
        self.background = pygame.image.load('data/imgs/tileset/Background.png').convert_alpha()
        self.ground = pygame.image.load('data/imgs/tileset/Ground.png').convert_alpha()
        
        self.score = 0
        self.alive = True
        
        # Timers
        pygame.time.set_timer(pygame.USEREVENT + 2, 2500)
        
        # Fonts
        self.font = pygame.font.Font('data/fonts/Press.ttf', 16)
        
         
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r and not self.alive:
                        self.score = 0
                        self.enemies.empty()
                        self.dino = pygame.sprite.GroupSingle(Dino())
                        self.alive = True
                if event.type == pygame.USEREVENT + 1 or self.start == 0:
                    self.start = 1
                    self.enemies.add(Enemies())
                    pygame.time.set_timer(pygame.USEREVENT + 1, random.randint(1000, 3000))  
                if event.type == pygame.USEREVENT + 2 and self.alive:
                    self.score += 1 
            
            #Background stuff
            collision = pygame.sprite.groupcollide(self.dino, self.enemies, True, False)
            
            if collision:
                self.alive = False
            
            if self.alive:
                # Clear screen/Fill black
                self.display.fill('black')
                
                self.display.blit(self.background, (0, 0))
                self.display.blit(self.ground, (0, 205))
                
                font_render = self.font.render(f'Score: {self.score}', False, 'black')
                self.display.blit(font_render, (10, 10))
                
                self.dino.update()
                self.dino.draw(self.display)
                
                self.enemies.update()
                self.enemies.draw(self.display)
                
            else:
                # Clear screen/Fill black
                self.display.fill('black')
                
                self.display.blit(self.background, (0, 0))
                self.display.blit(self.ground, (0, 205))
                
                font_score = self.font.render(f'Youre final score: {self.score}', False, 'black')
                self.display.blit(font_score, (50, 30))
                font_restart = self.font.render(f'Press R to restart', False, 'black')
                self.display.blit(font_restart, (50, 50))
                
                self.dino.update()
                self.dino.draw(self.display)
                
                #self.enemies.update()
                self.enemies.draw(self.display)
                
                
                
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)
            
Game().run()