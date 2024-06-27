import pygame

class Dino(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Load the image
        self.image = pygame.transform.scale_by(pygame.image.load('data/imgs/dino/Dino.png').convert_alpha(), 2)
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.gravity = 0.2
        self.velocity = 0
        
    def apply_gravity(self):
        self.rect.y -= self.velocity
        self.velocity -= self.gravity
        
    def collisions(self):
        if self.rect.y >= 173:
            self.rect.y = 173
            self.velocity = 0  
    
    def jump(self):
        if self.velocity == 0:
            self.velocity += 5
        
    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.jump()
        
    def update(self):
        self.apply_gravity()
        self.collisions()
        self.input()