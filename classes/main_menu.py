import pygame
pygame.init()

# --- Page principale (menu) ---
class MainMenu:
    def __init__(self, W, H, font_path):
        self.Page = True
        self.choose_map = False
        self.Width = W
        self.Height = H
        self.title = "Albertos VS Albertas"
        self.font = font_path
        self.game = None

        self.img_background = "assets/background/back/2 background/orig.png"
        self.background = None

        self.text = None
        self.text_rect = None
        self.play_text = None
        self.play_rect = None
        self.exit_text = None
        self.exit_rect = None

        self.perso_1 = None
        self.perso_2 = None
        self.perso_1_rect = None
        self.perso_2_rect = None

    # --- Setup visuel ---
    def setup_background(self):
        bg = pygame.image.load(self.img_background)
        self.background = pygame.transform.scale(bg, (self.Width, self.Height))

    def setup_decoration(self, font_path):
        self.perso_1 = self.scale_and_flip(pygame.image.load("assets/perso/Converted_Vampire/hurt/00.png"))
        self.perso_2 = self.scale_and_flip(pygame.image.load("assets/perso/Countess_Vampire/idle/00.png"))

        font = pygame.font.Font(font_path, 83)
        self.text = font.render(self.title, True, (255, 10, 10))

    def setup_buttons(self):
        font_btn = pygame.font.Font(self.font, 50)
        self.play_text = font_btn.render("Play", True, (255, 10, 10))
        self.exit_text = font_btn.render("Exit", True, (255, 10, 10))

    def setup_positions(self):
        self.text_rect = self.text.get_rect(center=(self.Width // 2, self.Height // 2 - 175))
        self.play_rect = self.play_text.get_rect(center=(self.Width // 2, self.Height // 2))
        self.exit_rect = self.exit_text.get_rect(center=(self.Width // 2, self.Height // 2 + 75))

        self.perso_1_rect = self.perso_1.get_rect(center=(self.Width // 2 - 275, self.Height // 2 - 30))
        self.perso_2_rect = self.perso_2.get_rect(center=(self.Width // 2 + 275, self.Height // 2 - 30))

    # --- Méthodes utilitaires ---
    def scale_and_flip(self, sprite, scale_factor=4):
        sprite = pygame.transform.flip(sprite, True, False)
        size = sprite.get_size()
        return pygame.transform.scale(sprite, (size[0] * scale_factor, size[1] * scale_factor))

    # --- Gestion des événements ---
    def handle_events(self, event):
        if event.type == pygame.QUIT:
            self.game.running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.play_rect.collidepoint(event.pos):
                print("Play clicked")
                sound = pygame.mixer.Sound("assets/sounds/bouton_sound.wav")
                sound.play()
                self.Page = False
                self.choose_map = True  # Active la page Choose_map
            elif self.exit_rect.collidepoint(event.pos):
                self.game.running = False
                print("Exit clicked")

    def update(self, font_path):
        self.setup_background()
        self.setup_decoration(font_path)
        self.setup_buttons()
        self.setup_positions()

    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        screen.blit(self.text, self.text_rect)
        screen.blit(self.play_text, self.play_rect)
        screen.blit(self.exit_text, self.exit_rect)
        screen.blit(self.perso_1, self.perso_1_rect)
        screen.blit(self.perso_2, self.perso_2_rect)
