import pygame

BLACK = (0, 0, 0)

class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.color = color
        self.width = width
        self.height = height
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

    def move_up(self, pixels, min_y):
        self.rect.y -= pixels
        if self.rect.y < min_y:
            self.rect.y = min_y
    
    def move_down(self, pixels, max_y):
        self.rect.y += pixels
        if self.rect.y > max_y - self.height:
            self.rect.y = max_y - self.height

        