import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """
    A class to represent a single aline in the flat
    """

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position """
        super().__init__()
        self.screen = ai_game
        self.settings = ai_game.settings
        self.screen_rect    = ai_game.screen.get_rect()

        #load the aline image and sent its rect attributes
        self.image_file = 'images/ufo.bmp'
        self.image = pygame.image.load(self.image_file)
        self.rect = self.image.get_rect()

        # start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store the alien's exact horizontal position
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen_rect
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien right or left."""
        self.x += (self.settings.alien_speed *
            self.settings.fleet_direction)
        self.rect.x = self.x

