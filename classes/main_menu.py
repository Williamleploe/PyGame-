import pygame
pygame.init()

class MainMenu:
    def __init__(self, game):
        self.game = game
        self.screen_width = 1280
        self.screen_height = 720
        self.buttons = []
        self.setup_background()
        self.setup_buttons()

    def setup_background(self):
        # 💡 tu peux changer le fond ici si tu veux un autre visuel pour le menu
        self.background = pygame.Surface((self.screen_width, self.screen_height))
        self.background.fill((10, 10, 30))  # fond sombre stylé
        font = pygame.font.Font(None, 100)
        self.title = font.render("FIGHTING GAME", True, (255, 0, 0))
        self.title_rect = self.title.get_rect(center=(self.screen_width // 2, 150))

    def setup_buttons(self):
        font = pygame.font.Font(None, 60)
        play_button = pygame.Rect(self.screen_width // 2 - 150, 300, 300, 80)
        quit_button = pygame.Rect(self.screen_width // 2 - 150, 420, 300, 80)

        self.buttons.append({"rect": play_button, "text": font.render("PLAY", True, (255, 255, 255))})
        self.buttons.append({"rect": quit_button, "text": font.render("QUIT", True, (255, 255, 255))})

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            for i, button in enumerate(self.buttons):
                if button["rect"].collidepoint(mouse_pos):
                    if i == 0:  # PLAY
                        print("Play clicked")
                        self.game.change_page("map")  # 👉 Passe au choix de map
                    elif i == 1:  # QUIT
                        print("Quit clicked")
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
