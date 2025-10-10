import pygame
pygame.init()
from classes_jeu.perso import Perso

class Player(pygame.sprite.Sprite):
    def __init__(self, idle_path, name="", position="left", direction=False):
        super().__init__()
        self.idle_path = idle_path
        try:
            self.image = pygame.image.load(idle_path)
        except Exception:
            self.image = pygame.Surface((128,128))
        self.rect = self.image.get_rect()
        
        self.name = name
        self.score_Player = 0
        self.position = position
        self.direction = direction
        self.perso = Perso(idle_path)
        self.icon_path = idle_path

        self.rect.topleft = (self.perso.x, self.perso.y)

    def post_init(self):
        try:
            self.image = pygame.image.load(self.idle_path).convert_alpha()
        except Exception:
            self.image = pygame.Surface((self.perso.width, self.perso.height))
        self.rect = self.perso.perso_rect.copy()