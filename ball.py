import pygame
from random import randint

BLACK = (0, 0, 0)

# Define a class for the ball
class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        
        # Create a rectangular image for the ball
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)  # Fill the image with the background color
        self.image.set_colorkey(BLACK)  # Set the color key for transparency
        
        # Store the width and height of the ball
        self.width = width
        self.height = height
        
        # Draw the ball's appearance onto the image
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        # Initialize the ball's velocity with random values
        self.velocity = [randint(4, 8), randint(-8, -8)]
        
        # Get the rectangle that represents the ball's position and size
        self.rect = self.image.get_rect()

    # Update the ball's position based on its velocity
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    # Change the ball's direction when it hits something
    def bounce(self):
        self.velocity[0] = -self.velocity[0]  # Reverse the horizontal velocity
        self.velocity[1] = randint(-8, 8)  # Set a random vertical velocity
