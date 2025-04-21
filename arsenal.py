import pygame
from bullet import Bullet
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Arsenal:
    def __init__(self, game: 'AlienInvasion'):
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self):
        self.arsenal.update()
        self._remove_bullets_offscreen()
    
    def _remove_bullets_offscreen(self):
        """

        This function ensures that should a bullet fly offscreen, it'll vanish.

        """
        for bullet in self.arsenal.copy():
            if bullet.rect.bottom <= 0:
                self.arsenal.remove(bullet)
    
    def draw(self):
        for bullet in self.arsenal:
            bullet.draw_bullet()

    def fire_bullet(self):
        """

        This function ensures that if a bullet flies offscreen, it'll be added to the ship's arsenal.

        """
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False