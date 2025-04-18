from pathlib import Path

class Settings:
    
    def __init__(self):
        self.name: str = 'Alien Invasion'
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'Starbasesnow.png'

        # Image courtesy of jagdos of OpenGameArt.org. Original name is simply "Rocket", and this
        # is a public domain image.

        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'onlyrocket.png'
        self.ship_w = 60
        self.ship_h = 150
        self.ship_speed = 5
        self.starting_ship_count = 3

        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'laserBlast.png'
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'laser.mp3'
        self.impact_sound = Path.cwd() / 'Assets' / 'sound' / 'impactSound.mp3'
        self.bullet_speed = 7
        self.bullet_w = 25
        self.bullet_h = 80
        self.bullet_amount = 5

        self.alien_file = Path.cwd() / 'Assets' / 'images' / 'enemy_4.png'
        self.alien_w = 40
        self.alien_h = 40
        self.fleet_speed = 2
        self.fleet_direction = 2
        self.fleet_drop_speed = 20

        self.button_w = 200
        self.button_l = 50
        self.button_color = (0,135,50)

        self.text_color = (255,255,255)
        self.button_font_size = 48
        self.HUD_front_size = 20
        self.font_file = Path.cwd() / 'Assets' / 'Fonts' / 'Silkscreen' / 'Silkscreen-Bold.ttf'