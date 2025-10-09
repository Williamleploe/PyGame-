import pygame
import json
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
        self.maps = []

        self.load_maps()
        self.setup_background()
        self.setup_text()
        self.create_buttons()

    def load_maps(self):
        try:
            with open("maps.json", "r") as f:
                self.maps = json.load(f)
        except Exception as e:
            print("Erreur lors du chargement du fichier maps.json :", e)
            # Fallback si maps.json est absent
            self.maps = [
                {"name": "cave_1"},
                {"name": "cave_2"},
                {"name": "jungle_1"},
                {"name": "jungle_2"}
            ]

    def setup_background(self):
        try:
            # ✅ On utilise maintenant ton image “orig_big.png”
            self.background = pygame.image.load("assets/background/back/4 background/orig_big.png").convert()
            self.background = pygame.transform.scale(self.background, (self.Width, self.Height))
        except Exception as e:
            print("Erreur lors du chargement du fond :", e)
            # Couleur de secours
            self.background = pygame.Surface((self.Width, self.Height))
            self.background.fill((20, 20, 20))

    def setup_text(self):
        font = pygame.font.Font(None, 80)
        self.text = font.render("Choisis ta map", True, (255, 0, 0))
        self.text_rect = self.text.get_rect(center=(self.Width // 2, 80))

    def create_buttons(self):
        font = pygame.font.Font(None, 50)
        button_width = 250
        button_height = 80
        spacing = 50
        total_width = len(self.maps) * (button_width + spacing) - spacing
        start_x = (self.Width - total_width) // 2
        y = self.Height // 2

        for i, map_info in enumerate(self.maps):
            rect = pygame.Rect(start_x + i * (button_width + spacing), y, button_width, button_height)
            text_surface = font.render(map_info["name"], True, (255, 0, 0))
            text_rect = text_surface.get_rect(center=rect.center)
            self.buttons.append({
                "name": map_info["name"],
                "rect": rect,
                "text": text_surface,
                "text_rect": text_rect
            })

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            for button in self.buttons:
                if button["rect"].collidepoint(mouse_pos):
                    print(f"Map '{button['name']}' cliquée !")
                    print(f"✔ Carte sélectionnée : {button['name']}")
                    self.game.selected_map = button["name"]

                    # ✅ Passe à l'écran de sélection de personnages
                    self.game.current_page = self.game.Choose_Player
                    self.game.Choose_Player.update()

    def update(self):
        pass  # Pas de mise à jour dynamique ici

    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        screen.blit(self.text, self.text_rect)
        for button in self.buttons:
            pygame.draw.rect(screen, (255, 255, 255), button["rect"], 2)
            screen.blit(button["text"], button["text_rect"])
