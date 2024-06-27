import pygame

class Enemies(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale_by(pygame.image.load('data/imgs/tileset/Cactus.png').convert_alpha(), 1)
        self.rect = self.image.get_rect()
        self.location = (400, 181)
        self.rect = self.rect.move(self.location)
    
        
    def update(self):
        self.rect.x -= 2
        return self.rect.x
        