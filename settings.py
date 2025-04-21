from pathlib import Path

class Settings:
    
    def __init__(self):
        """

        SpecialGothicExpandedOne-Regular.ttf is the font used for the code text:
            Link: https://fonts.google.com/selection

        """
        self.name: str = 'Alien Invasion'
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'bg5.jpg'
        self.difficulty_scale = 1.1
        self.scores_file = Path.cwd() / 'Assets' / 'file' / 'scores.json'

        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'onlyrocket.png'
        self.ship_w = 60
        self.ship_h = 150

        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'bullet.png'
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / '521492__typeoo__air_blast_big_1_5s.wav'
        self.impact_sound = Path.cwd() / 'Assets' / 'sound' / '478277__joao_janz__8-bit-explosion-1_6.wav'

        self.alien_file = Path.cwd() / 'Assets' / 'images' / 'alien2.png'
        self.alien_w = 40
        self.alien_h = 40
        self.fleet_speed = 2
        self.fleet_direction = 2
        self.fleet_drop_speed = 20

        self.button_w = 200
        self.button_h = 50
        self.button_color = (0,135,0)

        self.text_color = (255,255,255)
        self.button_font_size = 48
        self.HUD_font_size = 20
        self.font_file = Path.cwd() / 'Assets' / 'Fonts' / 'Silkscreen' / 'SpecialGothicExpandedOne-Regular.ttf'

    def initialize_dynamic_settings(self):
        """
        
        This function sets up the size for the ship, fleet, and bullets.

        """
        self.ship_speed = 5
        self.starting_ship_count = 3

        self.bullet_w = 250
        self.bullet_h = 80
        self.bullet_speed = 7
        self.bullet_amount = 5

        self.fleet_speed = 2
        self.fleet_drop_speed = 40
        self.alien_points = 50

    def increase_difficulty(self):
        """

        This function makes the speed for the sprites increase once each level is passed.

        """
        self.ship_speed += self.difficulty_scale
        self.bullet_speed += self.difficulty_scale
        self.fleet_speed += self.difficulty_scale