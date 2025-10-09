import pygame
from classes.choose_map import Choose_map
from classes.choose_player import Choose_Player

pygame.init()

class Game:
    def __init__(self):
        # --- Fenêtre principale ---
        self.WIDTH = 1280
        self.HEIGHT = 720
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Jeu de Combat - Sélection")

        # --- Police (aucune police custom pour l’instant) ---
        self.FONT_PATH = None

        # --- États du jeu ---
        self.running = True
        self.clock = pygame.time.Clock()

        # --- Données de sélection ---
        self.selected_map = None
        self.player1_character = None
        self.player2_character = None

        # --- Pages ---
        self.Choose_Map = Choose_map(self)
        self.Choose_Player = Choose_Player(self)

        # Page actuelle = menu de carte
        self.current_page = self.Choose_Map

    def run(self):
        """Boucle principale"""
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    raise SystemExit()

                # Transmet les événements à la page actuelle
                if self.current_page:
                    self.current_page.handle_events(event)

            # Met à jour et affiche la page actuelle
            if self.current_page:
                self.current_page.update()
                self.current_page.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)

    def go_to_player_select(self):
        """Appelé après le choix de la map"""
        self.current_page = self.Choose_Player
        self.Choose_Player.reset_choices()

if __name__ == "__main__":
    game = Game()
    game.run()
