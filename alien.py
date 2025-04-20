import random
import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_fleet import AlienFleet

class Alien(Sprite):
    def __init__(self, fleet: 'AlienFleet', x: float, y: float):
            """Initialize an alien at the specified (x, y) position within the fleet."""
            super().__init__()
            self.fleet = fleet
            self.screen = fleet.game.screen
            self.boundaries = fleet.game.screen.get_rect()
            self.settings = fleet.game.settings

            self.image = pygame.image.load(self.fleet.settings.alien_file)
            self.image = pygame.transform.scale(self.image, 
                (self.settings.alien_w, self.settings.alien_h)
                )

            self.rect = self.image.get_rect()
            self.rect.x = int(x)
            self.rect.y = int(y)

            self.y = float(self.rect.y)
            self.x = float(self.rect.x)

            
            self.center_x = float(self.rect.x)
            self.center_y = float(self.rect.y)
            self.velocity_x = random.uniform(-1.5, 1.5)
            self.velocity_y = random.uniform(0.2, 0.5)

    def update(self):
        """Random jittering movement with soft bouncing and descent."""
        self.center_x += self.velocity_x
        self.center_y += self.velocity_y

        screen_w = self.boundaries.width
        screen_h = self.boundaries.height

        # === Soft bounce zone ===
        horizontal_margin = 20
        vertical_ceiling = 0
        vertical_floor = screen_h // 1.8

    # Bounce X
        if self.center_x <= horizontal_margin:
            self.center_x = horizontal_margin  # stop it from going too far
            self.velocity_x *= -1
        elif self.center_x + self.rect.width >= screen_w - horizontal_margin:
            self.center_x = screen_w - horizontal_margin - self.rect.width
            self.velocity_x *= -1

        # Bounce Y (optional: control how deep they go)
        if self.center_y <= vertical_ceiling:
            self.center_y = vertical_ceiling
            self.velocity_y *= -1
        elif self.center_y + self.rect.height >= vertical_floor:
            self.center_y = vertical_floor - self.rect.height
            self.velocity_y *= -1

        # Apply updated position
        self.rect.x = int(self.center_x)
        self.rect.y = int(self.center_y)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        return self.rect.right >= screen_rect.right or self.rect.left <= 0

    def draw_alien(self):
        """Draw the alien at its current position on the screen."""
        self.screen.blit(self.image, self.rect)
        