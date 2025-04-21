import random
import pygame
from alien import Alien
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
  
class AlienFleet:
    
    def __init__(self, game: 'AlienInvasion'):
        """Initialize the alien fleet with reference to the main game instance."""
        self.game = game
        self.settings = game.settings
        self.fleet_direction = self.settings.fleet_direction
        self.aliens = pygame.sprite.Group()
        self.layout = "scatter"

       
        self.create_fleet(layout=self.layout, num_aliens=30)
        

    def create_fleet(self, layout="grid", num_aliens=20):
        self.layout = layout  

        if layout == "grid":
            fleet_w, fleet_h = self.calculate_fleet_size(
                self.settings.alien_w, self.settings.screen_w,
                self.settings.alien_h, self.settings.screen_h
            )
            x_offset, y_offset = self.calculate_offsets(
                self.settings.alien_w, self.settings.alien_h,
                self.settings.screen_w, fleet_w, fleet_h
            )
            self._create_rectangle_fleet(
                self.settings.alien_w, self.settings.alien_h,
                fleet_w, fleet_h, x_offset, y_offset
            )

        elif layout == "scatter":
            self.create_scatter_fleet(num_aliens)    

        

    def _create_rectangle_fleet(self, alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset):
    def _create_rectangle_fleet(self, alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset):
        for row in range(fleet_h):
            for col in range(fleet_w):
                x = x_offset + col * alien_w
                y = y_offset + row * alien_h
                self._create_alien(x, y)

    def create_scatter_fleet(self, num_aliens=20, padding=50):
        """Randomly scatter aliens across the top third of the screen."""
        screen_rect = self.game.screen.get_rect()
        alien = Alien(self, 0, 0)
        alien_w, alien_h = alien.rect.size

        for _ in range(min(num_aliens, 100)):
            x = random.randint(padding, screen_rect.width - alien_w - padding)
            y = random.randint(padding, screen_rect.height // 3)
            self._create_alien(x, y)
            
            

    def calculate_offsets(self, alien_w, alien_h, screen_w, fleet_w, fleet_h):
        x_offset = (screen_w - (fleet_w * alien_w)) // 2
        y_offset = alien_h
        return x_offset, y_offset



    def calculate_fleet_size(self, alien_w, screen_w, alien_h, screen_h):
        available_space_x = screen_w - 2 * alien_w
        available_space_y = screen_h // 2
        num_cols = available_space_x // (2 * alien_w)
        num_rows = available_space_y // (2 * alien_h)
        return num_cols, num_rows
    
    def _create_alien(self, current_x: int, current_y: int):
        alien = Alien(self, current_x, current_y)
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        if not self.aliens:
            return

        for alien in self.aliens:
            if alien.check_edges():
                self._drop_alien_fleet()
                break
                
    def _drop_alien_fleet(self):
        for alien in self.aliens.sprites():
            try:
                alien.rect.y = int(alien.rect.y + self.settings.fleet_drop_speed)
            except Exception as e:
                print(f"[ERROR] Failed to update alien y-pos: {e}")
        self.fleet_direction *= -1

                     
    def update_fleet(self):
        self._check_fleet_edges()
        self.aliens.update()
        

    def draw(self):
        """Draw all aliens on the screen."""
        for alien in self.aliens.sprites():
            alien.draw_alien()

    def check_collisions(self, other_group):
        """Check for collisions between the fleet and another group of sprites."""
        return pygame.sprite.groupcollide(self.aliens, other_group, True, True)


    def check_fleet_bottom(self):
        """Check if any alien has reached the bottom of the screen."""
        alien: 'Alien'
        for alien in self.aliens:
            if alien.rect.bottom >= self.settings.screen_h:
                return True
        return False

    def check_destroyed_status(self):
        """Check if all aliens in the fleet have been destroyed."""
        return not self.aliens