import pygame
from game import Game


pygame.init()


# Display
pygame.display.set_caption("Comet Fall Game")
screen = pygame.display.set_mode((1080, 720))



# Background
background = pygame.image.load('assets/bg.jpg')


# Charge the game

game = Game()


running = True
while running:
    # Set the background image
    screen.blit(background, (0, -200))

    # Set the player image
    screen.blit(game.player.image, game.player.rect)


    # Update screen
    pygame.display.flip()

    # If player quit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
