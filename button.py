import pygame.font

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Button:

    def __init__(self, game: 'AlienInvasion', msg):
        """Initialize the button with game context and display message."""
        self.game = game
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.settings = game.settings
        self.font = pygame.font.Font(self.settings.font_file, 
             self.settings.button_font_size)
        self.rect = pygame.Rect(0, 0, self.settings.button_w, self.settings.button_h)
        self.rect.center = self.boundaries.center
        self._prep_msg(msg)


    def _prep_msg(self, msg):
        """Render the button's message text as an image."""
        self.msg_image = self.font.render(msg, True, self.settings.text_color, None)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        """Draw the button with a glowing edge and its message to the screen."""
        glow_rect = self.rect.inflate(10, 10)
        pygame.draw.rect(self.screen, self.settings.button_glow_color, glow_rect, border_radius=12)

        #button background with rounded corners
        pygame.draw.rect(self.screen, self.settings.button_color, self.rect, border_radius=10)

        #button text
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def check_click(self, mouse_pos):
        """Check if the button was clicked based on the mouse position."""
        return self.rect.collidepoint(mouse_pos)
         