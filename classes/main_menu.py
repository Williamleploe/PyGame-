import pygame
import json
import os
pygame.init()

class MainMenu:
    def __init__(self, game):
        self.game = game
        self.WIDTH = 1280
        self.HEIGHT = 720
        self.buttons = []
        self.background = None
        self.title = None
        self.title_rect = None
        self.vampire_boy = None
        self.vampire_girl = None
        self.setup_background()
        self.setup_decorations()
        self.setup_buttons()

    def setup_background(self):
        """Charge le fond d’écran du menu principal"""
        try:
            self.background = pygame.image.load("assets/background/back/2 background/orig.png").convert()
            self.background = pygame.transform.scale(self.background, (self.WIDTH, self.HEIGHT))
        except Exception as e:
            print("⚠️ Erreur chargement fond :", e)
            self.background = pygame.Surface((self.WIDTH, self.HEIGHT))
            self.background.fill((0, 0, 0))

    def setup_decorations(self):
        """Ajoute le titre et les personnages sur les côtés"""
        # Titre
        font = pygame.font.Font(None, 100)
        self.title = font.render("FIGHTING GAME", True, (255, 0, 0))
        self.title_rect = self.title.get_rect(center=(self.WIDTH // 2, 150))

        # 🧛‍♂️ Vampire garçon (à gauche)
        try:
            self.vampire_boy = pygame.image.load("assets/perso/Converted_Vampire/idle/00.png").convert_alpha()
            self.vampire_boy = pygame.transform.scale(self.vampire_boy, (400, 400))
            # Le placer au sol (y = bas de l’écran)
            self.vampire_boy_rect = self.vampire_boy.get_rect(midbottom=(self.WIDTH // 4 - 50, self.HEIGHT - 30))
        except Exception as e:
            print("⚠️ Erreur chargement vampire garçon :", e)
            self.vampire_boy = None

        # 🧛‍♀️ Vampire fille (à droite)
        try:
            self.vampire_girl = pygame.image.load("assets/perso/Countess_Vampire/idle/00.png").convert_alpha()
            self.vampire_girl = pygame.transform.scale(self.vampire_girl, (400, 400))
            # Position au sol à droite
            self.vampire_girl_rect = self.vampire_girl.get_rect(midbottom=(self.WIDTH - self.WIDTH // 4 + 50, self.HEIGHT - 30))
        except Exception as e:
            print("⚠️ Erreur chargement vampire fille :", e)
            self.vampire_girl = None

    def setup_buttons(self):
        """Crée les boutons du menu"""
        self.buttons = []
        font = pygame.font.Font(None, 60)

        # Vérifie si setup.json contient une sauvegarde
        continue_exists = False
        if os.path.exists("setup.json"):
            try:
                with open("setup.json", "r", encoding="utf-8") as f:
                    data = f.read().strip()
                    if data and data != "{}":
                        continue_exists = True
            except Exception:
                continue_exists = False

        # Boutons
        play_rect = pygame.Rect(self.WIDTH // 2 - 150, 400, 300, 80)
        quit_rect = pygame.Rect(self.WIDTH // 2 - 150, 520, 300, 80)
        self.buttons.append({
            "rect": play_rect,
            "text": font.render("NOUVELLE PARTIE", True, (255, 255, 255)),
            "action": "new"
        })

        if continue_exists:
            cont_rect = pygame.Rect(self.WIDTH // 2 - 150, 620, 300, 80)
            self.buttons.append({
                "rect": cont_rect,
                "text": font.render("CONTINUER", True, (255, 255, 255)),
                "action": "continue"
            })

        self.buttons.append({
            "rect": quit_rect,
            "text": font.render("QUITTER", True, (255, 255, 255)),
            "action": "quit"
        })

    def handle_events(self, event):
        """Gère les clics sur les boutons"""
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            for button in self.buttons:
                if button["rect"].collidepoint(pos):
                    action = button["action"]
                    if action == "new":
                        print("🆕 Nouvelle partie")
                        with open("setup.json", "w", encoding="utf-8") as f:
                            json.dump({}, f, indent=2)
                        self.game.change_page("map")
                    elif action == "continue":
                        print("⏩ Continuer la partie")
                        self.game.change_page("player")
                    elif action == "quit":
                        self.game.running = False

    def update(self):
        pass

    def draw(self, screen):
        """Affiche tout à l’écran"""
        screen.blit(self.background, (0, 0))
        screen.blit(self.title, self.title_rect)

        # Affiche les vampires si dispos
        if self.vampire_boy:
            screen.blit(self.vampire_boy, self.vampire_boy_rect)
        if self.vampire_girl:
            screen.blit(self.vampire_girl, self.vampire_girl_rect)

        # Dessine les boutons
        for button in self.buttons:
            pygame.draw.rect(screen, (255, 0, 0), button["rect"], border_radius=10)
            text_rect = button["text"].get_rect(center=button["rect"].center)
            screen.blit(button["text"], text_rect)
