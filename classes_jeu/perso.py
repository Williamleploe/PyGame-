import pygame
pygame.init()

class Movements():
    def __init__(self):
        self.velocity = 6          # vitesse horizontale générale (au lieu de 5)
        self.air_velocity = 5      # vitesse horizontale spécifique en saut
        self.is_jumping = False
        self.jump_height = 200     # plus haut pour plus de temps en l'air
        self.jump_speed = 7        # vitesse verticale plus lente
        self.jump_start_y = 0
        self.jump_phase = "up"

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.jump_start_y = self.y
            self.jump_phase = "up"

    def update_jump(self):
        if self.is_jumping:
            # montée
            if self.jump_phase == "up":
                self.y -= self.jump_speed
                if self.y <= self.jump_start_y - self.jump_height:
                    self.jump_phase = "down"
            # descente
            else:
                self.y += self.jump_speed
                if self.y >= self.jump_start_y:
                    self.y = self.jump_start_y
                    self.is_jumping = False
                    self.jump_phase = "up"

            # appliquer vitesse horizontale pendant le saut
            keys = pygame.key.get_pressed()
            if keys[pygame.K_q] or keys[pygame.K_j]:  # gauche pour Player1 / Player2
                self.x -= self.air_velocity
            if keys[pygame.K_d] or keys[pygame.K_l]:  # droite pour Player1 / Player2
                self.x += self.air_velocity

            self.update_rect_from_values()


class Perso(Movements):
    def __init__(self, idle_path):
        super().__init__()
        self.idle_path = idle_path
        self.path = idle_path
        self.name = ""
        self.max_health = 100
        self.health = self.max_health
        self.max_energy = 100
        self.energy = self.max_energy
        self.type = "melee"
        self.attack1 = [15, 10]
        self.attack2 = [25, 15]
        self.attack3 = [35, 25]
        self.velocity = 5
        
        self.energy_regen = 5
        self.last_energy_time = pygame.time.get_ticks()
        
        try:
            self.perso = pygame.image.load(self.idle_path)
        except Exception:
            # image de secours
            self.perso = pygame.Surface((128, 128))
        self.perso_rect = self.perso.get_rect()
        
        self.x = self.perso_rect.x = 300
        self.y = self.perso_rect.y = 200  # valeur modifiée ensuite pour être 20px du bas
        self.width = self.perso_rect.width
        self.height = self.perso_rect.height

    def update_rect_from_values(self):
        self.perso_rect.x = int(self.x)
        self.perso_rect.y = int(self.y)
        self.perso_rect.width = int(self.width)
        self.perso_rect.height = int(self.height)

    def update_values_from_rect(self):
        self.x = self.perso_rect.x
        self.y = self.perso_rect.y
        self.width = self.perso_rect.width
        self.height = self.perso_rect.height

    def attack(self, target, damage):
        target.perso.health = max(target.perso.health - damage, 0)

    def use_Energy(self, energy_cost):
        if self.energy - energy_cost >= 0:
            self.energy -= energy_cost

    def regen_energy(self):
        now = pygame.time.get_ticks()
        if now - self.last_energy_time >= 1000:
            self.energy = min(self.energy + self.energy_regen, self.max_energy)
            self.last_energy_time = now