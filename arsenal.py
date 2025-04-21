import pygame
from bullet import Bullet
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
   

class Arsenal:
    def __init__(self, game: 'AlienInvasion'):
        """Initialize the player's arsenal with reference to the game instance."""
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self):
        """Update positions of all bullets in the arsenal and remove offscreen ones."""
        self.arsenal.update()
        self._remove_bullet_offscreen()


    def _remove_bullet_offscreen(self):
        """Remove bullets that have moved off the top of the screen."""
        for bullet in self.arsenal.copy():
            if bullet.rect.bottom <= 0:
                self.arsenal.remove(bullet)

    def draw(self):
        """Draw all bullets currently in the arsenal to the screen."""
        for bullet in self.arsenal:
            bullet.draw()
    
    def fire_bullet(self):
        """Create and fire a new bullet if the limit hasn't been reached."""
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False
          
       