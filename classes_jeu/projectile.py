import pygame
pygame.init()

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, damage):
        super().__init__()
        self.damage = damage
        self.speed = 10
        self.direction = direction  # True = gauche, False = droite
        self.owner = None  # Propriétaire du projectile
        
        # Créer un simple rectangle rouge pour le projectile
        self.image = pygame.Surface((20, 10))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
    def update(self):
        if self.direction:  # Vers la gauche
            self.rect.x -= self.speed
        else:  # Vers la droite
            self.rect.x += self.speed
        
        # Supprimer si hors écran (utilise la largeur fixe 1280 ici)
        if self.rect.x < -50 or self.rect.x > 1280 + 50:
            self.kill()