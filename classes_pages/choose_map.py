import pygame
import json
from classes_jeu.utils import insert_data_json, FILE_SETUP

class ChooseMap:
    def __init__(self, game):
        self.game = game
        self.Width = game.WIDTH
        self.Height = game.HEIGHT
        self.buttons = []

        # Background
        self.background_path = "assets/background/back/2 background/orig.png"
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

        # Dictionnaire des maps
        self.maps = {
            "cave_1": {
                "name": "cave_1",
                "background": "assets/background/cave_1/Preview 1.png",
                "plan": "assets/background/cave_1/Plan 1.png"
            },
            "cave_2": {
                "name": "cave_2", 
                "background": "assets/background/cave_2/Preview 3.png",
                "plan": "assets/background/cave_2/Plan 1.png"
            },
            "jungle_1": {
                "name": "jungle_1",
                "background": "assets/background/jungle_1/Preview 1.png",
                "plan": "assets/background/jungle_1/Plan 1.png"
            },
            "jungle_2": {
                "name": "jungle_2",
                "background": "assets/background/jungle_2/Preview 2.png", 
                "plan": "assets/background/jungle_2/Plan 1.png"
            }
        }

        self.font = pygame.font.Font(self.game.font, 50)
        self.title = pygame.font.Font(self.game.font, 70).render("Choisis ta carte", True,(255, 10, 10) )
        self.title_rect = self.title.get_rect(center=(self.Width // 2, 100))

        self.setup_buttons()

    def setup_buttons(self):
        spacing_x, spacing_y = 300, 150
        cols = 2
        total_width = (cols-1)*spacing_x
        total_height = ((len(self.maps)-1)//cols)*spacing_y
        start_x = (self.Width - total_width) // 2
        start_y = (self.Height - total_height) // 2 + 50

        self.buttons = []
        for index, map_name in enumerate(self.maps.keys()):
            text_surface = self.font.render(map_name, True, (255, 255, 255))
            row = index // cols
            col = index % cols
            x = start_x + col * spacing_x
            y = start_y + row * spacing_y
            rect = text_surface.get_rect(center=(x, y))
            self.buttons.append({"surface": text_surface, "rect": rect, "name": map_name})

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for button in self.buttons:
                if button["rect"].collidepoint(event.pos):
                    pygame.mixer.Sound("assets/sounds/bouton_sound.wav").play()
                    map_name = button["name"]
                    self.game.game_setup["map"] = self.maps[map_name]
                    print(f"🗺️ Map sélectionnée : {map_name}")
                    self.game.change_page(self.game.Choose_Character)

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.BACKGROUND, self.background_rect)
        screen.blit(self.title, self.title_rect)
        for btn in self.buttons:
            screen.blit(btn["surface"], btn["rect"])