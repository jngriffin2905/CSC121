# Project: Blue Sky
# Class: CSC-121 OA1
# Author: Jessica Griffin


# Creating a pygame window.
import sys

import pygame

from blue_sky_settings import Settings 

from blue_sky_basket import Basket

class BlueSky:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Blue Sky")

     
        

        self.basket = Basket(self)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)
             
     
    def _check_events(self):
            """Respond to keypresses and mouse events."""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
    
    def _update_screen(self):
            """Update images on the screen, and flip to the new screen."""
            self.screen.fill(self.settings.bg_color)
            self.basket.blitme()           

            # Make the most recently drawn screen visible.
            pygame.display.flip()
            

if __name__ == '__main__':
    # Make a game instance, and run the game.
    bs = BlueSky()
    bs.run_game()

