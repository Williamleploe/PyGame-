import sys
import pygame
pygame.init()

from main_menu import MainMenu
from choose_map import Choose_map

class Game:
    def __init__(self, width=1280, height=700, title="Albertos VS Albertas"):
        self.WIDTH = width
        self.HEIGHT = height
        self.title = title
        self.icon = None
        self.screen = None
        self.clock = pygame.time.Clock()
        self.running = True
        self.current_page = None
        self.font = "assets/fonts/GlitchGoblin.ttf"

        # --- Paramètres du son ---
        self.file_mp3 = "assets/sounds/fond/track_2.mp3"
        self.volume_level = 0.95
        self.loop = True

        # --- Instances des pages ---
        self.MainPage = MainMenu(self.WIDTH, self.HEIGHT, self.font)
        self.MainPage.game = self

        self.Choose_Map = Choose_map()
        self.Choose_Map.game = self

        self.Choose_Character = None
        self.Fight = None
        self.Victory = None

    # --- Musique de fond ---
    def sound_background(self):
        """Joue la musique seulement si rien ne joue déjà."""
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(self.file_mp3)
            pygame.mixer.music.set_volume(self.volume_level)
            pygame.mixer.music.play(-1 if self.loop else 0)


    def setup_window(self):
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption(self.title)
        self.icon = pygame.image.load("assets/icon.png")
        pygame.display.set_icon(self.icon)

    # --- Gestion des pages ---
    def update_current_page(self):
        """Détermine quelle page est active."""
        if self.MainPage.Page:
            self.current_page = self.MainPage
        elif self.MainPage.choose_map:
            self.current_page = self.Choose_Map
        # ici tu pourras ajouter d'autres pages ( Choose_Character, Fight, Victory )

    # --- Boucle principale ---
    def run(self):
        self.setup_window()
        self.sound_background()

        while self.running:
            self.update_current_page()
            for event in pygame.event.get():
                if self.current_page:
                    self.current_page.handle_events(event)

            # Mettre à jour et dessiner la page active
            if self.current_page:
                self.current_page.update(self.font)
                self.current_page.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()
