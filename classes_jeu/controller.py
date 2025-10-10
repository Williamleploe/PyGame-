import pygame
from classes_jeu.projectile import Projectile

class PlayerController:
    def __init__(self, player_instance, enemy_instance, projectile_group, key_list, sound_manager, screen_width=None, screen_height=None):
        self.player = player_instance
        self.enemy = enemy_instance
        self.projectile_group = projectile_group
        self.sound_manager = sound_manager
        self.melee_range = 80
        self.protect_active = False

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.move_left_key = key_list[0]
        self.move_right_key = key_list[1]
        self.jump_key = key_list[2]
        self.attack_keys = key_list[3:6]
        self.protect_key = key_list[6]

        # 🦶 Gestion du son de pas
        self.is_walking = False
        self.footstep_channel = None


    def handle_input(self, events):
        keys = pygame.key.get_pressed()
        p = self.player.perso

        # 🔽 Gestion des touches appuyées une seule fois
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == self.jump_key and not p.is_jumping:
                    p.jump()
                    self.sound_manager.play('jump')

                for i, key in enumerate(self.attack_keys, start=1):
                    if event.key == key:
                        self.attack(i)

        # 🔁 Déplacement continu
        is_moving = False

        if keys[self.move_right_key]:
            p.x += p.velocity
            self.player.direction = False
            is_moving = True

        if keys[self.move_left_key]:
            p.x -= p.velocity
            self.player.direction = True
            is_moving = True

        # 🎵 Gestion du son de pas
        if is_moving and not p.is_jumping:
            if not self.is_walking:
                # Démarre la boucle des pas
                footstep_sound = getattr(self.sound_manager.sounds, 'get', lambda x: None)('footstep')
                if footstep_sound:
                    self.footstep_channel = pygame.mixer.find_channel(True)
                    # Jouer en boucle avec volume un peu réduit (optionnel)
                    self.footstep_channel.play(footstep_sound, loops=-1)
                    self.footstep_channel.set_volume(0.5)
                self.is_walking = True
        else:
            if self.is_walking:
                # Arrête le son de pas
                if self.footstep_channel and self.footstep_channel.get_busy():
                    self.footstep_channel.stop()
                self.is_walking = False

        # 🔄 Mises à jour du perso
        p.update_jump()
        p.regen_energy()
        p.update_rect_from_values()
        self.player.rect = p.perso_rect.copy()
        self.protect_active = keys[self.protect_key]


    def attack(self, attack_number):
        p = self.player.perso
        e = self.enemy.perso
        damage, energy_cost = getattr(p, f"attack{attack_number}")

        if p.energy < energy_cost:
            return

        if p.type == "melee":
            distance = abs(p.x - e.x)
            if distance <= self.melee_range:
                e.health = max(e.health - damage, 0)
                p.use_Energy(energy_cost)

                # 🔊 Son de mêlée
                if hasattr(self.sound_manager, 'play_melee'):
                    self.sound_manager.play_melee()
                else:
                    self.sound_manager.play('melee')

                print(f"⚔️ {self.player.name} attaque {self.enemy.name} (-{damage} dégâts)")
            else:
                print(f"❌ {self.player.name} trop loin! (distance: {distance})")

        elif p.type == "range":
            start_x = p.x + p.width // 2
            start_y = p.y + p.height // 2
            direction = self.player.direction

            proj = Projectile(x=start_x, y=start_y, direction=direction, damage=damage)
            proj.owner = self.player
            self.projectile_group.add(proj)

            p.use_Energy(energy_cost)

            # 🔊 Son à distance
            if hasattr(self.sound_manager, 'play_range'):
                self.sound_manager.play_range()
            else:
                self.sound_manager.play('range')

            print(f"🏹 {self.player.name} lance un projectile (-{damage} dégâts, direction: {'gauche' if direction else 'droite'})")
