import sys
import pygame
from settings import Settings
from game_stats import GameStats
from ship import Ship
from arsenal import Arsenal
# from alien import Alien
from alien_fleet import AlienFleet
from time import sleep
from button import Button
from hud import HUD

class AlienInvasion:

    def __init__(self):
        """
        
        This function deals with setting up the basics of the entire "alien_invasion" code; namely the sprites and background.

        bg5.jpg is the background choice:
            Link: https://opengameart.org/content/space-background

        521492__typeoo__air_blast_big_1_5s.wav is the laser sound effect:
            Link: https://freesound.org/people/typeoo/sounds/521492/

        478277__joao_janz__8-bit-explosion-1_6.wav is the impact sound effect:
            Link: https://freesound.org/people/Joao_Janz/sounds/478277/

        """
        pygame.init()
        self.settings = Settings()
        self.settings.initialize_dynamic_settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_w,self.settings.screen_h)
            )
        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load('bg5.jpg')
        self.bg = pygame.transform.scale(self.bg, 
            (self.settings.screen_w, self.settings.screen_h)
            )

        self.game_stats = GameStats(self)
        self.HUD = HUD(self)
        self.running = True
        self.clock = pygame.time.Clock()

        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound('521492__typeoo__air_blast_big_1_5s.wav')
        self.laser_sound.set_volume(0.7)

        self.impact = pygame.mixer.Sound('478277__joao_janz__8-bit-explosion-1_6.wav')
        self.impact.set_volume(0.7)


        self.ship = Ship(self, Arsenal(self))
        self.alien_fleet = AlienFleet(self)
        self.alien_fleet.create_fleet()

        self.play_button = Button(self, 'Play')
        self.game_active = False
    
    def run_game(self):
        """
        
        This function causes various aspects of the code to change for every round completed.

        """
        # Game loop
        while self.running:
            self._check_events()
            if self.game_active:
                self.ship.update()
                self.alien_fleet.update_fleet()
                self._check_collisions()
            self._update_screen()
            self.clock.tick(self.settings.FPS)
    
    def _check_collisions(self):
        # check collisions for ship
        if self.ship.check_collisions(self.alien_fleet.fleet):
            self._check_game_status()
            # subtract one life if possible

        # check collisions for aliens and bottom of screen
        if self.alien_fleet.check_fleet_bottom():
            self._check_game_status()
        # check collisions of projectiles and any aliens
        collisions = self.alien_fleet.check_collisions(self.ship.arsenal.arsenal)
        if collisions:
            self.impact.play()
            self.impact.fadeout(500)
            self.game_stats.update(collisions)
            self.HUD.update_scores()
        
        if self.alien_fleet.check_destroyed_status():
            self._reset_level()
            self.settings.increase_difficulty()
            # update game stats level
            self.game_stats.update_level()
            # update HUD view
            self.HUD.update_level()


    def _check_game_status(self):
        
        """

        This function makes sure that when the ship count reaches zero, the game is over.

        """
        if self.game_stats.ships_left > 0:
            self.game_stats.ships_left -= 1
            self._reset_level()
            sleep(0.5)
        else:
            self.game_active = False


        

    def _reset_level(self):
        self.ship.arsenal.arsenal.empty()
        self.alien_fleet.fleet.empty()
        self.alien_fleet.create_fleet()
    
    def restart_game(self):
        self.settings.initialize_dynamic_settings()
        self.game_stats.reset_stats()
        self.HUD.update_scores()
        self._reset_level()
        self.ship._center_ship()
        self.game_active = True
        pygame.mouse.set_visible(False)

    def _update_screen(self):
        self.screen.blit(self.bg, (0,0))
        self.ship.blitme()
        self.alien_fleet.draw()
        self.HUD.draw()


        if not self.game_active:
            self.play_button.draw()
            pygame.mouse.set_visible(True)

        pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.game_stats.save_scores()
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and self.game_active == True:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_button_clicked()

    def _check_button_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.play_button.check_clicked(mouse_pos):
            self.restart_game()

    def _check_keyup_events(self, event):
        """

        This function makes the ship move left to right per the right or left button being pressed.

        Args:
            self.ship.moving_right: Moves the ship right.
            self.ship.moving_left: Moves the ship left.
        """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        

    def _check_keydown_events(self, event):
        """
        
        This function ensures that the ship moves in accordance to the keydown, and that the ship fires lasers when the space bar is pressed.

        Args:
            self.ship.fire(): Makes sure that when a laser is fired, the appropriate sound is played as well.
            
        """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            if self.ship.fire():
                self.laser_sound.play()
                self.laser_sound.fadeout(160)

        elif event.key == pygame.K_q:
            self.running = False
            self.game_stats.save_scores()
            pygame.quit()
            sys.exit()
        

if __name__ == '__main__':
    AlienInvasion = AlienInvasion()
    AlienInvasion.run_game()
