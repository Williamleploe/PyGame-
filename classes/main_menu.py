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
        self.setup_background()
        self.setup_buttons()

    def setup_background(self):
        self.background = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.background.fill((0, 0, 0))
        font = pygame.font.Font(None, 100)
        self.title = font.render("FIGHTING GAME", True, (255, 0, 0))
        self.title_rect = self.title.get_rect(center=(self.WIDTH // 2, 150))

    def setup_buttons(self):
        self.buttons = []
        font = pygame.font.Font(None, 60)

        # Vérifie si setup.json existe et contient des données
        continue_exists = False
        if os.path.exists("setup.json"):
            try:
                with open("setup.json", "r", encoding="utf-8") as f:
                    data = f.read().strip()
                    if data and data != "{}":
                        continue_exists = True
            except Exception:
                continue_exists = False

        # Crée les boutons
        play_rect = pygame.Rect(self.WIDTH // 2 - 150, 300, 300, 80)
        quit_rect = pygame.Rect(self.WIDTH // 2 - 150, 420, 300, 80)
        self.buttons.append({"rect": play_rect, "text": font.render("NOUVELLE PARTIE", True, (255, 255, 255)), "action": "new"})
        if continue_exists:
            cont_rect = pygame.Rect(self.WIDTH // 2 - 150, 520, 300, 80)
            self.buttons.append({"rect": cont_rect, "text": font.render("CONTINUER", True, (255, 255, 255)), "action": "continue"})
        self.buttons.append({"rect": quit_rect, "text": font.render("QUITTER", True, (255, 255, 255)), "action": "quit"})

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            for button in self.buttons:
                if button["rect"].collidepoint(pos):
                    action = button["action"]
                    if action == "new":
                        print("🆕 Nouvelle partie")
                        # Efface le setup.json
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
        screen.blit(self.background, (0, 0))
        screen.blit(self.title, self.title_rect)
        for button in self.buttons:
            pygame.draw.rect(screen, (255, 0, 0), button["rect"], border_radius=10)
            text_rect = button["text"].get_rect(center=button["rect"].center)
            screen.blit(button["text"], text_rect)
