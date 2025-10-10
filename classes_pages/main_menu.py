# classes_pages/main_menu.py
import pygame
from classes_jeu.utils import open_json, FILE_SETUP

class MainMenu:
    def __init__(self, game):
        self.game = game
        self.Width = game.WIDTH
        self.Height = game.HEIGHT

        # Chemins des images
        self.image_1_path = "assets/perso/Converted_Vampire/idle/00.png"
        self.image_2_path = "assets/perso/Countess_Vampire/idle/00.png"
        self.background_path = "assets/background/back/2 background/orig.png"

        # ⚡ Variable pour éviter de recharger plusieurs fois
        self.images_loaded = False
        
        # ⚡ Charger les images directement
        self.load_images()
        
        # Fonts et texte
        font = pygame.font.Font(self.game.font, 60)
        small = pygame.font.Font(self.game.font, 40)

        self.title = font.render("Albertos VS Albertas", True, (255, 10, 10))
        self.title_rect = self.title.get_rect(center=(self.Width // 2, 100))

        self.play_text = small.render("New Game", True, (255, 255 ,255))
        self.play_rect = self.play_text.get_rect(center=(self.Width // 2, 240))

        self.cont_text = small.render("Continue", True, (255, 255 ,255))
        self.cont_rect = self.cont_text.get_rect(center=(self.Width // 2, 320))

        self.exit_text = small.render("Exit", True, (255, 10, 10))
        self.exit_rect = self.exit_text.get_rect(center=(self.Width // 2, 400))

    def load_images(self):
        """Charge les images une seule fois."""
        if self.images_loaded:
            return
        
        # ✅ Taille des personnages (augmentée de 4 pixels)
        size = 204

        # Image 1 (gauche)
        self.image_1_original = pygame.image.load(self.image_1_path).convert_alpha()
        self.image_1 = pygame.transform.scale(self.image_1_original, (size, size))
        self.img1_rect = self.image_1.get_rect()
        self.img1_rect.x = 100
        self.img1_rect.y = self.Height - (size + 100)

        # Image 2 (droite)
        self.image_2_original = pygame.image.load(self.image_2_path).convert_alpha()
        self.image_2 = pygame.transform.scale(self.image_2_original, (size, size))
        self.image_2 = pygame.transform.flip(self.image_2, True, False)
        self.img2_rect = self.image_2.get_rect()
        self.img2_rect.x = self.Width - (size + 100)
        self.img2_rect.y = self.Height - (size + 100)

        # Background
        self.BACKGROUND = pygame.image.load(self.background_path).convert()
        bg_width = self.BACKGROUND.get_width()
        bg_height = self.BACKGROUND.get_height()
        ratio = bg_height / bg_width
        new_height = self.Height
        new_width = int(new_height / ratio)
        self.BACKGROUND = pygame.transform.scale(self.BACKGROUND, (new_width, new_height))
        self.background_rect = self.BACKGROUND.get_rect()
        self.background_rect.x = (self.Width - new_width) // 2
        self.background_rect.y = 0
        
        self.images_loaded = True
        print(f"✅ Images du menu chargées ({size}x{size})")

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = event.pos
            
            # Jouer son de clic
            if hasattr(self.game, 'sound_manager'):
                self.game.sound_manager.play('armor')
            
            if self.play_rect.collidepoint(pos):
                self.game.game_setup = {"map": None, "players": [
                    {"name": None, "type": None},
                    {"name": None, "type": None}
                ]}
                self.game.change_page(self.game.Choose_Map)

            elif self.cont_rect.collidepoint(pos):
                setup = open_json(FILE_SETUP)
                if setup and "players" in setup and len(setup["players"]) >= 2:
                    print("🔄 Chargement sauvegarde ->", FILE_SETUP)
                    self.game.game_setup["map"] = setup.get("map", None)
                    players_short = []
                    for p in setup.get("players", []):
                        players_short.append({
                            "name": p.get("name"),
                            "type": p.get("type_personnage", p.get("type", None))
                        })
                    while len(players_short) < 2:
                        players_short.append({"name": None, "type": None})
                    self.game.game_setup["players"] = players_short[:2]
                    self.game.GamePlay = True

            elif self.exit_rect.collidepoint(pos):
                self.game.running = False

    def update(self):
        # ⚡ Vérifie que la taille des images n’a pas changé
        if hasattr(self, 'image_1') and self.image_1.get_width() != 204:
            print("⚠️ Images redimensionnées incorrectement, rechargement...")
            self.images_loaded = False
            self.load_images()

    def draw(self, screen):
        # Dessiner le background
        screen.blit(self.BACKGROUND, self.background_rect)

        # Dessiner les personnages
        screen.blit(self.image_1, self.img1_rect)
        screen.blit(self.image_2, self.img2_rect)

        # Dessiner les textes
        screen.blit(self.title, self.title_rect)
        screen.blit(self.play_text, self.play_rect)
        screen.blit(self.cont_text, self.cont_rect)
        screen.blit(self.exit_text, self.exit_rect)
