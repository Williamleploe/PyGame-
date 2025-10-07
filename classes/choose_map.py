import pygame
import json
pygame.init()

class Choose_map:
    def __init__(self):
        self.buttons = []
        self.Width = 0
        self.Height = 0
        self.background = None
        self.text = None
        self.text_rect = None
        self.maps = []
        self.game = None

        with open("classes/json/maps.json", "r") as f:
            self.maps = json.load(f)

    # --- Setup visuel ---
    def setup_background(self, W, H):
        self.Width = W
        self.Height = H
        bg = pygame.image.load("assets/background/back/2 background/orig.png")
        self.background = pygame.transform.scale(bg, (W, H))

    def setup_decoration(self, font_path, W):
        self.title_font = pygame.font.Font(font_path, 70)
        self.button_font = pygame.font.Font(font_path, 50)
        self.text = self.title_font.render("Choisis ta carte", True, (255, 255, 255))
        self.text_rect = self.text.get_rect(center=(W // 2, 100))

    def setup_buttons(self):
        spacing_x, spacing_y = 300, 150
        font_color = (255, 10, 10)
        cols = 2
        total_width = (cols - 1) * spacing_x
        total_height = ((len(self.maps) - 1) // cols) * spacing_y
        start_x = (self.Width - total_width) // 2
        start_y = (self.Height - total_height) // 2 + 50

        self.buttons = []
        for index, map_data in enumerate(self.maps):
            text_surface = self.button_font.render(map_data["name"], True, font_color)
            row = index // cols
            col = index % cols
            x = start_x + col * spacing_x
            y = start_y + row * spacing_y
            rect = text_surface.get_rect(center=(x, y))
            self.buttons.append({"surface": text_surface, "rect": rect, "name": map_data["name"]})

    # --- Gestion des événements ---
    def handle_events(self, event):
        if event.type == pygame.QUIT:
            self.game.running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = event.pos
            for button in self.buttons:
                if button["rect"].collidepoint(mouse_pos):
                    print(f"Map '{button['name']}' cliquée !")
                    sound = pygame.mixer.Sound("assets/sounds/bouton_sound.wav")
                    sound.play()
                    self.on_map_selected(button["name"])

    def on_map_selected(self, map_name):
        """Appelée lorsqu'une carte est choisie"""
        print(f"✔ Carte sélectionnée : {map_name}")
        self.game.MainPage.choose_map = False
        # Ici tu peux activer la page de choix de personnage si tu la crées
        # self.game.current_page = self.game.Choose_Character

    # --- Mise à jour ---
    def update(self, font_path):
        self.setup_background(self.game.WIDTH, self.game.HEIGHT)
        self.setup_decoration(font_path, self.game.WIDTH)
        self.setup_buttons()

    # --- Dessin ---
    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        screen.blit(self.text, self.text_rect)
        for button in self.buttons:
            screen.blit(button["surface"], button["rect"])
