# Project: Blue Sky
# Class: CSC-121 OA1
# Author: Jessica Griffin

# Creating the basket class
import pygame

class Basket:
    """A class to manage the basket."""

    def __init__(self, bs_game):
        """Initialize the basket and set its starting position"""
        self.screen = bs_game.screen
        self.screen_rect = bs_game.screen.get_rect()

        # Load the basket image and get its rect.
        self.image = pygame.image.load("C:/Users/jngri/Desktop/python_work/Chapter_12/images/easter_bunny.bmp")
        self.rect = self.image.get_rect()

        # Start each new basket at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the basket at its current location."""
        self.screen.blit(self.image, self.rect)