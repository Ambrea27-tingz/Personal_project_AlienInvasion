from pathlib import Path
import json

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

from pathlib import Path
import json

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class GameStats():

    def __init__(self, game: 'AlienInvasion'):
        """Initialize game statistics tracking for the given game instance."""
        self.game = game
        self.settings = game.settings
        self.max_score = 0
        self.init_saved_scores()
        self.reset_stats()

    
    def init_saved_scores(self):
        """Initialize or load previously saved high scores."""
        self.path = self.settings.scores_file
        if self.path.exists() and self.path.stat.__sizeof__ () > 20:
            contents = self.path.read_text()
            scores = json.loads(contents)
            self.hi_score = scores.get('hi_score', 0)
        else:
            self.hi_score = 0
            self.save_scores()
            # save the file

    
    def save_scores(self):
        """Save the current high scores to persistent storage."""
        scores = {
            'hi_score': self.hi_score
        }
        contents = json.dumps(scores, indent=4)
        try:
            self.path.write_text(contents)
        except FileNotFoundError as e:
            print(f'File Not Found: {e}')
            

    def reset_stats(self):
        """Reset statistics that change during gameplay."""
        self.ships_left = self.settings.starting_ship_count
        self.score = 0
        self.level = 1


    def update(self, collisions):
        """Update score, level, and other stats based on collisions.""" 
        self._update_score(collisions)
        self._update_max_score()
        self._update_hi_score()

    def _update_max_score(self):
        """Update the maximum score achieved in the session."""
        if self.score > self.max_score:
            self.max_score = self.score
       

    def _update_hi_score(self):
        """Update and track the all-time high score."""
        if self.score > self.hi_score:
            self.hi_score = self.score
       
   
    def _update_score(self, collisions):
        """Update the player's score based on the number of collisions."""
        for alien in collisions.values():
            self.score += self.settings.alien_points
       
      
    def _update_level(self):
        """Advance the game to the next level and update level count."""
        self.level += 1
        
       

