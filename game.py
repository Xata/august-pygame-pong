import pygame
from paddle import Paddle
from ball import Ball

def game():
    pygame.init()

    # Set up colors and window title
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    WINDOW_TITLE = "Pong"

    # Set up game window
    size = (800, 600)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(WINDOW_TITLE)

    # Initialize game variables
    carry_on = True
    clock = pygame.time.Clock()

    # Initialize player scores
    score_a = 0
    score_b = 0

    # Create left paddle
    paddle_a = Paddle(WHITE, 10, 100)
    paddle_a.rect.x = 20
    paddle_a.rect.y = size[1] / 2

    # Create right paddle
    paddle_b = Paddle(WHITE, 10, 100)
    paddle_b.rect.x = size[0] - 20 - paddle_b.width
    paddle_b.rect.y = size[1] / 2

    # Create ball
    ball = Ball(WHITE, 10, 10)
    ball.rect.x = size[0] / 2
    ball.rect.y = size[1] / 2

    # Create a sprite group to manage all game objects
    all_sprites_list = pygame.sprite.Group()
    all_sprites_list.add(paddle_a)
    all_sprites_list.add(paddle_b)
    all_sprites_list.add(ball)

    while carry_on:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carry_on = False
        
        # Handle player inputs
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddle_a.move_up(5, 0)
        if keys[pygame.K_s]:
            paddle_a.move_down(5, size[1])
        if keys[pygame.K_UP]:
            paddle_b.move_up(5, 0)
        if keys[pygame.K_DOWN]:
            paddle_b.move_down(5, size[1])

        # Ball bouncing logic
        if ball.rect.x >= size[0]:
            score_a += 1
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.x <= 0:
            score_b += 1
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.y > size[1] - ball.height:
            ball.velocity[1] = -ball.velocity[1]   
        if ball.rect.y < 0:
            ball.velocity[1] = -ball.velocity[1]

        # Collision detection with paddles
        if ball.rect.colliderect(paddle_a.rect) or ball.rect.colliderect(paddle_b.rect):
            ball.bounce()

        # Update ball position
        ball.update()

        # Clear the screen
        screen.fill(BLACK)

        # Draw center line
        pygame.draw.line(screen, WHITE, [size[0] / 2, 0], [size[0] / 2, size[1]], 5)

        # Draw all game objects
        all_sprites_list.draw(screen)

        # Display player scores
        font = pygame.font.Font(None, 74)
        text = font.render(str(score_a), 1, WHITE)
        screen.blit(text, ((size[0] / 2) / 2, 10))
        text = font.render(str(score_b), 1, WHITE)
        screen.blit(text, ((size[0] / 2) + ((size[0] / 2) / 2), 10))

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

    return 0
