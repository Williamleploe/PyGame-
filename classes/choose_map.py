import pygame
import json
import os
pygame.init()

class Choose_map:
    def __init__(self, game):
        self.game = game
        self.buttons = []
        self.Width = 1280
        self.Height = 720
        self.background = None
        self.text = None
        self.text_rect = None
        self.maps = [
            {"name": "cave_1", "background": "assets/background/cave_1/Preview 1.png", "plan": "assets/background/cave_1/Plan 1.png"},
            {"name": "jungle_1", "background": "assets/background/jungle_1/Preview 1.png", "plan": "assets/background/jungle_1/Plan 1.png"}
        ]
        self.setup_background()
        self.setup_text()
        self.create_buttons()

    def setup_background(self):
        self.background = pygame.Surface((self.Width, self.Height))
        self.background.fill((20, 20, 20))

    def setup_text(self):
        font = pygame.font.Font(None, 80)
        self.text = font.render("Choisis ta map", True, (255, 0, 0))
        self.text_rect = self.text.get_rect(center=(self.Width // 2, 80))

    def create_buttons(self):
        font = pygame.font.Font(None, 50)
        x, y = 300, 250
        for m in self.maps:
            rect = pygame.Rect(x, y, 300, 100)
            text_surface = font.render(m["name"], True, (255, 0, 0))
            text_rect = text_surface.get_rect(center=rect.center)
            self.buttons.append({"rect": rect, "name": m["name"], "text": text_surface, "text_rect": text_rect, "data": m})
            y += 150

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            for button in self.buttons:
                if button["rect"].collidepoint(pos):
                    print(f"Map '{button['name']}' choisie !")
                    self.save_map_choice(button["data"])
                    self.game.change_page("player")

    def save_map_choice(self, map_data):
        data = {"map": {"background": map_data["background"], "plan": map_data["plan"]}, "players": []}
        with open("setup.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        print("💾 Map sauvegardée dans setup.json")

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        screen.blit(self.text, self.text_rect)
        for button in self.buttons:
            pygame.draw.rect(screen, (255, 255, 255), button["rect"], 2)
            screen.blit(button["text"], button["text_rect"])
