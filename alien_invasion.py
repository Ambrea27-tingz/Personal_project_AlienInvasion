"""
Author: Ambrea Williams

Unit 13: Lab 14 / Part 3

Date: 04/17/2025

Title: Alien Invasion

Description: A simple game where the player controls a ship and shoots at aliens.

"""
import sys
import pygame
import pygame.mixer 
from settings import Settings
from game_stats import GameStats
from ship import Ship
from arsenal import Arsenal
#from alien import Alien 
from alien_fleet import AlienFleet
from time import sleep
from button import Button
from hud import HUD
from button import Button
from hud import HUD

class AlienInvasion:
    
    
    def __init__(self):
        """Initialize the game instance and set up resources.""" 
        pygame.init()
        self.settings = Settings()
        self.settings.initialize_dynamic_settings()
        self.settings.initialize_dynamic_settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_w,self.settings.screen_h)
            )
        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg,
                (self.settings.screen_w, self.settings.screen_h)
                )

        self.game_stats = GameStats(self)
        self.HUD = HUD(self)
        self.game_stats = GameStats(self)
        self.HUD = HUD(self)
        self.running = True
        self.clock = pygame.time.Clock()

        pygame.mixer.init()
        pygame.mixer.music.load('Assets/sound/game_bg_sound.mp3')
        pygame.mixer.music.set_volume(0.3)  # Adjust volume 0.0 - 1.0
        pygame.mixer.music.play(-1)  # -1 means loop forever
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        self.laser_sound.set_volume(0.7)
        

        self.impact_sound = pygame.mixer.Sound(self.settings.impact_sound)
        self.impact_sound.set_volume(0.7)

        self.ship = Ship(self, Arsenal(self)) 
        self.alien_fleet = AlienFleet(self)
        self.alien_fleet.aliens.empty()
        self.alien_fleet.create_fleet(layout="scatter", num_aliens=30)

        self.level_up_sound = pygame.mixer.Sound('Assets/sound/level_up_sound1.mp3')
        self.level_up_sound.set_volume(0.6)
        
        self.play_button = Button(self, 'Play')
        self.game_active = False


        

    def run_game(self):
        #Game loop
        while self.running:
            self._check_events()    
            if self.game_active:
                self.ship.update()
                self.alien_fleet.update_fleet()
                self._check_collisions()
            self._update_screen()
            self.clock.tick(self.settings.FPS)



    def _check_collisions(self):
        """Detect and respond to collisions between game objects."""
        if self.ship.check_collisions(self.alien_fleet.aliens):
            self._check_game_status() #Deduct one life
    
        if self.alien_fleet.check_fleet_bottom():
            self._check_game_status()
        collisions = self.alien_fleet.check_collisions(self.ship.arsenal.arsenal)
        if collisions:
            self.impact_sound.play()
            self.impact_sound.fadeout(500)
            self.game_stats.update(collisions)
            self.HUD.update_scores()
            self.game_stats.update(collisions)
            self.HUD.update_scores()
        
        if self.alien_fleet.check_destroyed_status():  
            self._reset_level()
            self.settings.increase_difficulty()
            self.game_stats._update_level()
            self.HUD.update_level()
            
                

            self.settings.increase_difficulty()
            self.game_stats._update_level()
            self.HUD.update_level()
            
                

        
    def _check_game_status(self):
        """Evaluate the current status of the game"""
        if self.game_stats.ships_left > 0:
            self.game_stats.ships_left -= 1 #win or lose conditions
            self._reset_level()
            sleep(0.5)
        else:
            self.game_active = False




    def _reset_level(self):
        """Reset game elements for the start of a new level."""
        self.ship.arsenal.arsenal.empty()
        self.alien_fleet.aliens.empty()
        self.alien_fleet.aliens.empty()
        self.alien_fleet.create_fleet(layout="scatter", num_aliens=30)
        
        self.level_up_sound.play()
      

       
    def restart_game(self):
        """Restart the game, reinitializing necessary state and objects."""
        self.settings.initialize_dynamic_settings()
        self.game_stats.reset_stats()
        self.HUD.update_scores()
        self._reset_level()
        self.ship._center_ship()
        self.game_active = True
        pygame.mouse.set_visible(False)


    def _update_screen(self):
        """Update images on the screen and flip to the new screen."""
        self.screen.blit(self.bg, (0, 0)) 
        self.ship.draw()  
        self.alien_fleet.draw()
        self.HUD.draw()
        
        if not self.game_active:
            self.play_button.draw()
            pygame.mouse.set_visible(True)
        
        self.HUD.draw()
        
        if not self.game_active:
            self.play_button.draw()
            pygame.mouse.set_visible(True)
        
        pygame.display.flip()

    def _check_events(self):
        """Respond to keypresses, mouse events, and other user input."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.game_stats.save_scores()
                pygame.mixer.music.stop()
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and self.game_active == True:
            elif event.type == pygame.KEYDOWN and self.game_active == True:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_button_clicked()

    def _check_button_clicked(self):
        """Check if the start/play button has been clicked."""
        mouse_pos = pygame.mouse.get_pos()
        if self.play_button.check_click(mouse_pos):
            self.restart_game()
    
    def _check_keyup_events(self, event):
        """Respond to key release events."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    def _check_keydown_events(self, event):
        """Respond to key press events."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True 
            self.ship.moving_left = True 
        elif event.key == pygame.K_SPACE:
            if self.ship.fire():
                self.laser_sound.play()
                self.laser_sound.fadeout(250)
        elif event.key == pygame.K_q:
            self.running = False
            self.game_stats.save_scores()
            self.game_stats.save_scores()
            pygame.quit()
            sys.exit()  
     
            sys.exit()  
     
       

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

