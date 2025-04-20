import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal

class Ship:


    def __init__(self, game: 'AlienInvasion', arsenal: 'Arsenal'):
        """Initialize the player's ship and set its starting position."""
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(self.image, 
             (self.settings.ship_w, self.settings.ship_h)
             )
        
        self.rect = self.image.get_rect()
        self._center_ship()
        self.moving_right = False
        self.moving_left = False
        self.arsenal = arsenal

    def _center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.boundaries.midbottom
        self.x = float(self.rect.x)
    
    def update(self):
        """Update the ship's position based on movement flags."""
        self._update_ship_movement()
        self.arsenal.update_arsenal()

    
    def _update_ship_movement(self):
        """Adjust ship's horizontal position if movement is active."""
        temp_speed = self.settings.ship_speed
        if self.moving_right and self.rect.right < self.boundaries.right:
           self.x += temp_speed
        if self.moving_left and self.rect.left > self.boundaries.left:
           self.x -= temp_speed

        self.rect.x = self.x

    def draw(self):
        """Draw the ship on the screen at its current location."""
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)        

    def fire(self):
        """Fire a bullet from the ship if allowed."""
        return self.arsenal.fire_bullet()  


    def check_collisions(self, other_group):
         """Check for collisions between the ship and another group of sprites."""
         if pygame.sprite.spritecollideany(self, other_group):
             self._center_ship()
             return True
         return False