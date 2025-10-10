import sys
import pygame
from classes_pages.main_menu import MainMenu
from classes_pages.choose_map import ChooseMap
from classes_pages.choose_character import ChooseCharacter
from classes_pages.victory import VictoryScreen

class Game:
    def __init__(self, width=1280, height=700, title="Albertos VS Albertas"):
        self.WIDTH = width
        self.HEIGHT = height
        self.title = title
        self.screen = None
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = "assets/fonts/GlitchGoblin.ttf"

        # Son
        self.file_mp3 = "assets/sounds/fond/track_1.mp3"
        self.volume_level = 0.95
        self.loop = True

        # ⚡ INITIALISER LA FENÊTRE D'ABORD
        self.setup_window()

        # ⚡ MAINTENANT créer les pages (après l'initialisation de Pygame)
        self.MainPage = MainMenu(self)
        self.Choose_Map = ChooseMap(self)
        self.Choose_Character = ChooseCharacter(self)
        
        self.current_page = self.MainPage
        self.GamePlay = False
        self.game_setup = {
            "map": None,
            "players": [
                {"name": None, "type": None},
                {"name": None, "type": None}
            ]
        }

    def setup_window(self):
        """Initialise la fenêtre Pygame"""
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption(self.title)
        try:
            icon = pygame.image.load("assets/icon.png")
            pygame.display.set_icon(icon)
        except Exception:
            print("⚠️ Icon introuvable : assets/icon.png")

    def sound_background(self):
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(self.file_mp3)
            pygame.mixer.music.set_volume(self.volume_level)
            pygame.mixer.music.play(-1 if self.loop else 0)

    def change_page(self, new_page):
        """Change la page actuelle"""
        self.current_page = new_page

    def run(self):
        self.sound_background()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
                if self.current_page:
                    self.current_page.handle_events(event)

            # 🎮 LANCEMENT DU COMBAT
            if self.GamePlay:
                from classes_jeu.fight import FightGame
                print("🚀 Lancement du combat...")
                fight = FightGame()
                fight.start()
                
                # 🏆 RÉCUPÉRER LES STATS DE FIN DE PARTIE
                if hasattr(fight, 'get_game_stats'):
                    game_stats = fight.get_game_stats()
                    
                    # 🎉 AFFICHER L'ÉCRAN DE VICTOIRE
                    victory_screen = VictoryScreen(self, game_stats)
                    
                    showing_victory = True
                    while showing_victory and self.running:
                        victory_events = pygame.event.get()
                        for event in victory_events:
                            if event.type == pygame.QUIT:
                                self.running = False
                                showing_victory = False
                            
                            # Vérifier si on retourne au menu
                            return_to_menu = victory_screen.handle_events(event)
                            if return_to_menu:
                                showing_victory = False
                        
                        victory_screen.update()
                        victory_screen.draw(self.screen)
                        self.clock.tick(60)
                
                # Retour au menu principal
                self.GamePlay = False
                self.current_page = self.MainPage
                print("🔙 Retour au menu principal")

            elif self.current_page:
                self.current_page.update()
                self.current_page.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()