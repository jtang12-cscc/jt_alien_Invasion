import sys
import pygame

class AlienInvasion:

    def __init__(self):
        pygame.init()

        self.screen = pygame.displa.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion!")

        self.running = True
        self.clock = pygame.time.Clock()
    
    def run_game(self):
        # Game loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
            
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()