from pathlib import Path
class Settings:
    
    
    def __init__(self):
        """Initialize the game's static settings."""
        self.name: str = "Alien Invasion"
        self.screen_w = 1200
        self.screen_h = 800
        #frames per second
        self.FPS = 60
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'Starbasesnow.png'
        self.scores_file = Path.cwd() / 'Assets' / 'file' / 'scores.json'

        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'ship.png'
        self.ship_w = 90          
        self.ship_h = 95          
      

        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'laserBlast.png'
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'laser.mp3'
        self.impact_sound = Path.cwd() / 'Assets' / 'sound' / 'impactSound.mp3'
        self.fleet_step_sound = Path.cwd() / 'Assets' / 'sound' / 'fleet_step.wav'
        
        

        self.alien_file = Path.cwd() / 'Assets' / 'images' / 'enemy.png'
        self.alien_w  = 40 
        self.alien_h = 40  
        self.fleet_direction = 1 
        self.fleet_drop_speed = 10

        self.button_w = 200
        self.button_h = 50
        self.button_color = (76, 0, 153)           # Deep purple
        self.button_glow_color = (138, 43, 226)    # Bright violet (outline glow)
        self.text_color = (173, 216, 230)          # Light cyan text
        
        self.button_font_size = 48
        self.HUD_font_size = 20
        self.font_file = Path.cwd() / 'Assets' / 'Fonts' / 'Silkscreen'/'Silkscreen-Bold.ttf'
       

    def initialize_dynamic_settings(self):
             """Initialize settings that change throughout the game."""
             self.ship_speed = 5
             self.starting_ship_count = 3 

             self.bullet_w = 25
             self.bullet_h = 80
             self.bullet_speed = 7
             self.bullet_amount = 5
             
             self.alien_speed = 80
             self.fleet_drop_speed = 40
             self.alien_points = 50

    def increase_difficulty(self):
        """Increase game difficulty by adjusting speed."""
        self.ship_speed *= 1.1
        self.bullet_speed *= 1.15
        self.alien_speed *= 1.3
        self.fleet_drop_speed *= 1.30

