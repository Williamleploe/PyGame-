import pygame
pygame.init()
from classes_jeu.utils import Utils

class GameDisplay:
    def __init__(self, screen, player1, player2, background_path, plan1_path, icon_vs_path, font_path, font_size):
        self.screen = screen
        self.player1 = player1
        self.player2 = player2
        self.utils = Utils()
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        # --- Fonts ---
        self.font = self.utils.font_setup(font_path, font_size)
        # --- Charger les images ---
        self.background_img = self.load_background(background_path)
        self.plan1_img = self.load_plan(plan1_path)
        try:
            self.icon_vs_img = self.utils.scale(0.15, pygame.image.load(icon_vs_path).convert_alpha())
        except Exception as e:
            print("⚠️ Icon VS introuvable:", icon_vs_path, e)
            self.icon_vs_img = pygame.Surface((100, 50))
        # --- Icônes joueurs ---
        try:
            self.icon1_img = self.utils.scale(1.5, pygame.image.load(player1.icon_path).convert_alpha())
        except Exception:
            self.icon1_img = pygame.Surface((64,64))
        try:
            self.icon2_img = self.utils.scale(1.5, pygame.image.load(player2.icon_path).convert_alpha())
            self.icon2_img = self.utils.flip(self.icon2_img, True, False)
        except Exception:
            self.icon2_img = pygame.Surface((64,64))
        # --- Charger les sprites des joueurs ---
        try:
            self.player1_sprite = pygame.image.load(player1.perso.idle_path).convert_alpha()
        except Exception:
            self.player1_sprite = pygame.Surface((player1.perso.width, player1.perso.height))
        try:
            self.player2_sprite = pygame.image.load(player2.perso.idle_path).convert_alpha()
        except Exception:
            self.player2_sprite = pygame.Surface((player2.perso.width, player2.perso.height))
        self.player1_sprite = self.utils.scale(2.5 , self.player1_sprite)
        self.player2_sprite = self.utils.scale(2.5 , self.player2_sprite)
        self.update()

    def load_background(self, path):
        try:
            bg_img = pygame.image.load(path).convert()
            ratio = bg_img.get_height() / bg_img.get_width()
            new_height = int(self.screen_width * ratio)
            bg_img = pygame.transform.scale(bg_img, (self.screen_width, new_height))
            return bg_img
        except Exception:
            return pygame.Surface((self.screen_width, self.screen_height))

    def load_plan(self, path):
        try:
            plan_img = pygame.image.load(path).convert_alpha()
            ratio = plan_img.get_height() / plan_img.get_width()
            new_height = int(self.screen_width * ratio)
            plan_img = pygame.transform.scale(plan_img, (self.screen_width, new_height))
            return plan_img
        except Exception:
            return pygame.Surface((self.screen_width, 100), pygame.SRCALPHA)

    def draw_background(self):
        bg_y = (self.screen_height - self.background_img.get_height()) // 2
        self.screen.blit(self.background_img, (0, bg_y))

    def draw_plan(self):
        plan_y = self.screen_height - self.plan1_img.get_height()
        self.screen.blit(self.plan1_img, (0, plan_y))

    def draw_scores(self):
        text_surface1 = self.font.render(str(self.player1.score_Player), True, (0, 0, 0))
        text_surface2 = self.font.render(str(self.player2.score_Player), True, (0, 0, 0))
        self.screen.blit(text_surface1, (540, 40))
        self.screen.blit(text_surface2, (self.screen_width - 580, 40))

    def draw_bars(self):
        max_width = 400
        # Joueur 1
        pygame.draw.rect(self.screen, (0, 0, 0), (100, 50, max_width + 4, 28))
        pygame.draw.rect(self.screen, (10, 150, 10), 
                         (102, 51, self.player1.perso.health / self.player1.perso.max_health * max_width, 12))
        pygame.draw.rect(self.screen, (10, 10, 150), 
                         (102, 65, self.player1.perso.energy / self.player1.perso.max_energy * max_width, 12))
        # Joueur 2
        right_x = self.screen_width - 100 - max_width
        pygame.draw.rect(self.screen, (0, 0, 0), (right_x, 50, max_width + 4, 28))
        pygame.draw.rect(self.screen, (10, 150, 10), 
                         (right_x + 2, 51, self.player2.perso.health / self.player2.perso.max_health * max_width, 12))
        pygame.draw.rect(self.screen, (10, 10, 150), 
                         (right_x + 2, 65, self.player2.perso.energy / self.player2.perso.max_energy * max_width, 12))

    def draw_icons(self):
        try:
            self.screen.blit(self.icon1_img, (-40, -70))
            self.screen.blit(self.icon_vs_img, ((self.screen_width - self.icon_vs_img.get_width()) // 2, 30))
            self.screen.blit(self.icon2_img, (self.screen_width - 150, -70))
        except Exception:
            pass

    def draw_players(self):
        player1_sprite, player1_rect = self.utils.flip_surface_keep_position(
            self.player1_sprite, self.player1.perso.perso_rect, direction=self.player1.direction
        )
        player2_sprite, player2_rect = self.utils.flip_surface_keep_position(
            self.player2_sprite, self.player2.perso.perso_rect, direction=self.player2.direction
        )

        self.screen.blit(player1_sprite, player1_rect)
        self.screen.blit(player2_sprite, player2_rect)
    
    def draw_projectiles(self, projectile_group):
        projectile_group.draw(self.screen)

    def update(self, projectile_group=None):
        self.screen.fill((0, 0, 0))
        self.draw_background()
        self.draw_plan()
        self.draw_scores()
        self.draw_bars()
        self.draw_icons()
        self.draw_players()
        if projectile_group:
            self.draw_projectiles(projectile_group)
        pygame.display.flip()