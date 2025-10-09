import pygame
pygame.init()

class Victory:
    def __init__(self, game, winner_name=""):
        self.game = game
        self.WIDTH = game.WIDTH
        self.HEIGHT = game.HEIGHT
        self.font_title = pygame.font.Font(None, 150)
        self.font_name = pygame.font.Font(None, 100)
        self.font_button = pygame.font.Font(None, 60)
        self.winner_name = winner_name

        self.setup_background()
        self.create_buttons()

    def setup_background(self):
        self.background = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.background.fill((0, 0, 0))  # fond noir

    def create_buttons(self):
        """Crée les deux boutons du bas."""
        button_width = 300
        button_height = 80
        spacing = 100

        # Positions
        total_width = button_width * 2 + spacing
        start_x = (self.WIDTH - total_width) // 2
        y = self.HEIGHT - 180

        # Bouton Restart
        self.restart_button = pygame.Rect(start_x, y, button_width, button_height)
        self.restart_text = self.font_button.render("RESTART", True, (255, 255, 255))
        self.restart_text_rect = self.restart_text.get_rect(center=self.restart_button.center)

        # Bouton Menu principal
        self.menu_button = pygame.Rect(start_x + button_width + spacing, y, button_width, button_height)
        self.menu_text = self.font_button.render("MENU PRINCIPAL", True, (255, 255, 255))
        self.menu_text_rect = self.menu_text.get_rect(center=self.menu_button.center)

    def set_winner(self, name):
        """Permet de changer le nom du gagnant dynamiquement"""
        self.winner_name = name

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            if self.restart_button.collidepoint(mouse_pos):
                print("🔁 Restart clicked")
                self.game.change_page("map")
            elif self.menu_button.collidepoint(mouse_pos):
                print("🏠 Retour au menu principal")
                self.game.change_page("menu")

        elif event.type == pygame.KEYDOWN:
            # touche espace ou entrée -> retour menu principal
            if event.key in [pygame.K_RETURN, pygame.K_SPACE]:
                self.game.change_page("menu")

    def update(self):
        pass

    def draw(self, screen):
        # fond
        screen.blit(self.background, (0, 0))

        # texte principal
        title = self.font_title.render("VICTORY!", True, (255, 215, 0))
        name = self.font_name.render(self.winner_name, True, (255, 0, 0))

        title_rect = title.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 3))
        name_rect = name.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2 - 50))

        screen.blit(title, title_rect)
        screen.blit(name, name_rect)

        # boutons
        pygame.draw.rect(screen, (255, 0, 0), self.restart_button, border_radius=10)
        pygame.draw.rect(screen, (255, 0, 0), self.menu_button, border_radius=10)
        screen.blit(self.restart_text, self.restart_text_rect)
        screen.blit(self.menu_text, self.menu_text_rect)
