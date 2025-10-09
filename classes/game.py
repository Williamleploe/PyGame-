import pygame
from classes.main_menu import MainMenu
from classes.choose_map import Choose_map
from classes.choose_player import Choose_Player
from classes.victory import Victory

pygame.init()

class Game:
    def __init__(self):
        # --- dimensions et fenêtre ---
        self.WIDTH = 1280
        self.HEIGHT = 720
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Fighting Game Project")

        # --- états de pages ---
        self.in_main_menu = True
        self.in_choose_map = False
        self.in_choose_player = False
        self.in_victory = False

        # --- pages du jeu ---
        self.Main_Menu = MainMenu(self)
        self.Choose_Map = Choose_map(self)
        self.Choose_Player = Choose_Player(self)
        self.Victory = Victory(self)

        # page actuelle
        self.current_page = self.Main_Menu

        # variables globales
        self.running = True
        self.clock = pygame.time.Clock()
        self.selected_map = None

    def change_page(self, target):
        """Change entre les différentes pages du jeu"""
        # Reset des états
        self.in_main_menu = False
        self.in_choose_map = False
        self.in_choose_player = False
        self.in_victory = False

        # Sélection de la page à afficher
        if target == "menu":
            self.in_main_menu = True
            self.current_page = self.Main_Menu
        elif target == "map":
            self.in_choose_map = True
            self.current_page = self.Choose_Map
        elif target == "player":
            self.in_choose_player = True
            self.current_page = self.Choose_Player
        elif target == "victory":
            self.in_victory = True
            self.current_page = self.Victory

    def run(self):
        """Boucle principale du jeu"""
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                else:
                    # Transmet les événements à la page active
                    self.current_page.handle_events(event)

            # Mise à jour et affichage de la page actuelle
            self.current_page.update()
            self.current_page.draw(self.screen)

            # Rafraîchissement
            pygame.display.flip()
            self.clock.tick(60)
