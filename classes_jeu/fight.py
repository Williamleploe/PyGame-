import pygame
import json
from classes_jeu.player_file import Player
from classes_jeu.perso import Perso
from classes_jeu.display import GameDisplay
from classes_jeu.controller import PlayerController
from classes_jeu.sound import SoundManager
from classes_jeu.save import Save
from classes_jeu.projectile import Projectile
from classes_jeu.utils import setup_window, open_json, insert_data_json, Utils


class Game_Fight():
    def __init__(self):
        self.icon_path = "assets/icon.png"
        self.title = "Albertos vs Albertas"
        self.background_path = "assets/background/jungle_1/Preview 1.png"
        self.back_plan_1_path = "assets/background/jungle_1/Plan 1.png"
        self.screen = None
        self.Width = 1280
        self.Height = 700
        self.winner = ""
        self.Fight = True
        self.utils = Utils()
        self.GamePlay = True
        self.running = True
        self.clock = pygame.time.Clock()
        
        file = "classes_pages/json/setup.json"
        # Charger les données JSON
        self.data = open_json(file)
        players_data = self.data.get("players", [])

        # Si JSON vide ou incomplet, créer des valeurs par défaut 
        if len(players_data) < 2:
            print("⚠️ JSON vide ou incomplet, initialisation des valeurs par défaut")
            players_data = [
                {
                    "idle_image": "assets/perso/Converted_Vampire/idle/00.png",
                    "name": "Converted_Vampire",
                    "position": "left",
                    "perso_rect": {"x": 148, "y": 350, "width": 128, "height": 128},
                    "health": 100,
                    "energy": 100,
                    "score": 0,
                    "direction": False,
                    "type_personnage": "melee"
                },
                {
                    "idle_image": "assets/perso/Countess_Vampire/idle/00.png",
                    "name": "Countess_Vampire",
                    "position": "right",
                    "perso_rect": {"x": 832, "y": 350, "width": 128, "height": 128},
                    "health": 100,
                    "energy": 100,
                    "score": 0,
                    "direction": True,
                    "type_personnage": "range"
                }
            ]

        # ⚡ CORRECTION : Charger les données de la map depuis le JSON
        map_data = self.data.get("map", {})
        if map_data:
            self.background_path = map_data.get("background", self.background_path)
            self.back_plan_1_path = map_data.get("plan", self.back_plan_1_path)
            print(f"🗺️ Map chargée: {map_data.get('name', 'Unknown')}")
            print(f"   Background: {self.background_path}")
            print(f"   Plan: {self.back_plan_1_path}")

        # Création sécurisée des players
        self.Player1 = Player(idle_path=players_data[0]["idle_image"])
        self.Player1.name = players_data[0].get("name", "Player1")
        self.Player1.position = players_data[0].get("position", "left")
        self.Player1.direction = players_data[0].get("direction", False)
        rect1 = players_data[0].get("perso_rect", {"x": 148, "y": 350, "width": 128, "height": 128})
        self.Player1.perso.x = rect1["x"]
        self.Player1.perso.y = rect1["y"]
        self.Player1.perso.width = rect1["width"]
        self.Player1.perso.height = rect1["height"]
        self.Player1.perso.type = players_data[0].get("type_personnage", "melee")
        # ⚡ LIRE LA VIE ET L'ÉNERGIE depuis le JSON
        self.Player1.perso.health = players_data[0].get("health", 100)
        self.Player1.perso.energy = players_data[0].get("energy", 100)
        self.Player1.perso.max_health = 100
        self.Player1.perso.max_energy = 100
        self.Player1.perso.update_rect_from_values()

        self.Player2 = Player(idle_path=players_data[1]["idle_image"])
        self.Player2.name = players_data[1].get("name", "Player2")
        self.Player2.position = players_data[1].get("position", "right")
        self.Player2.direction = players_data[1].get("direction", True)
        rect2 = players_data[1].get("perso_rect", {"x": 832, "y": 350, "width": 128, "height": 128})
        self.Player2.perso.x = rect2["x"]
        self.Player2.perso.y = rect2["y"]
        self.Player2.perso.width = rect2["width"]
        self.Player2.perso.height = rect2["height"]
        self.Player2.perso.type = players_data[1].get("type_personnage", "range")
        # ⚡ LIRE LA VIE ET L'ÉNERGIE depuis le JSON
        self.Player2.perso.health = players_data[1].get("health", 100)
        self.Player2.perso.energy = players_data[1].get("energy", 100)
        self.Player2.perso.max_health = 100
        self.Player2.perso.max_energy = 100
        self.Player2.perso.update_rect_from_values()

        # --- Positionner les persos à 20px du bas de la fenêtre ---
        for p in (self.Player1, self.Player2):
            p.perso.y = self.Height - 120 - p.perso.height
            p.perso.update_rect_from_values()
            p.rect.topleft = (p.perso.x, p.perso.y)

        # ⚡ INITIALISER LES COMPOSANTS MANQUANTS
        self.all_projectiles = pygame.sprite.Group()
        self.sound_manager = SoundManager()
        
        # ⚡ VARIABLES POUR L'AFFICHAGE
        self.icon_vs_path = "assets/vs.png"
        self.font_path = "assets/fonts/GlitchGoblin.ttf"
        self.font_size = 50

        print(f"🎯 Joueur 1: {self.Player1.name} ({self.Player1.perso.type}) - Vie: {self.Player1.perso.health} - Énergie: {self.Player1.perso.energy}")
        print(f"🎯 Joueur 2: {self.Player2.name} ({self.Player2.perso.type}) - Vie: {self.Player2.perso.health} - Énergie: {self.Player2.perso.energy}")

    def If_Data(self):
        if not self.data:
            return

        # Map
        map_data = self.data.get("map", {})
        self.background_path = map_data.get("background", "")
        self.back_plan_1_path = map_data.get("plan", "")

        # Players
        players_list = [self.Player1, self.Player2]
        for player_obj, joueur in zip(players_list, self.data.get("players", [])):
            p = player_obj.perso
            # Injection des données
            p.name = joueur.get("name", "")
            p.health = joueur.get("health", 100)
            p.energy = joueur.get("energy", 100)
            p.type = joueur.get("type_personnage", "")
            p.idle_path = joueur.get("idle_image", "")
            p.path = joueur.get("path", "")
            player_obj.score_Player = joueur.get("score", 0)
            player_obj.position = joueur.get("position", "")

    def Score(self):
        # Quelqu'un gagne avec 2 points et au moins 1 point d'avance
        if self.Player1.score_Player >= 2 and self.Player1.score_Player > self.Player2.score_Player:
            self.Fight = False
            self.winner = self.Player1.name
            print(f"🏆 {self.winner} GAGNE LA PARTIE! Score: {self.Player1.score_Player}-{self.Player2.score_Player}")
        elif self.Player2.score_Player >= 2 and self.Player2.score_Player > self.Player1.score_Player:
            self.Fight = False
            self.winner = self.Player2.name
            print(f"🏆 {self.winner} GAGNE LA PARTIE! Score: {self.Player1.score_Player}-{self.Player2.score_Player}")
        else:
            self.Fight = True

    def If_Ko(self):
        if self.Player1.perso.health == 0 or self.Player2.perso.health == 0:
            if self.Player1.perso.health == 0 and self.Player2.perso.health == 0:
                # Double KO
                self.Player1.score_Player += 1
                self.Player2.score_Player += 1
                print(f"💥 DOUBLE KO! Score: {self.Player1.score_Player}-{self.Player2.score_Player}")
            elif self.Player1.perso.health == 0:
                # Player2 gagne le round
                self.Player2.score_Player += 1
                print(f"💀 {self.Player1.name} KO! {self.Player2.name} marque! Score: {self.Player1.score_Player}-{self.Player2.score_Player}")
            elif self.Player2.perso.health == 0:
                # Player1 gagne le round
                self.Player1.score_Player += 1
                print(f"💀 {self.Player2.name} KO! {self.Player1.name} marque! Score: {self.Player1.score_Player}-{self.Player2.score_Player}")
            
            # Vérifier si quelqu'un gagne la partie
            self.Score()
            
            # Si le combat continue, réinitialiser les stats
            if self.Fight:
                self.reset_round()
    
    def reset_round(self):
        """Réinitialise la vie et l'énergie pour un nouveau round"""
        self.Player1.perso.health = self.Player1.perso.max_health
        self.Player1.perso.energy = self.Player1.perso.max_energy
        self.Player2.perso.health = self.Player2.perso.max_health
        self.Player2.perso.energy = self.Player2.perso.max_energy
        
        # Repositionner les joueurs aux positions de départ (Y = 20px du bas)
        self.Player1.perso.x = 148
        self.Player2.perso.x = 832
        self.Player1.perso.y = self.Height - 120 - self.Player1.perso.height
        self.Player2.perso.y = self.Height - 120 - self.Player2.perso.height
        
        self.Player1.perso.update_rect_from_values()
        self.Player2.perso.update_rect_from_values()
        self.Player1.rect.topleft = (self.Player1.perso.x, self.Player1.perso.y)
        self.Player2.rect.topleft = (self.Player2.perso.x, self.Player2.perso.y)
        
        print("🔄 Nouveau round!")
    
    def get_game_stats(self):
        """Retourne les statistiques de la partie"""
        return {
            "winner": self.winner if not self.Fight else None,
            "final_score": {
                "player1": self.Player1.score_Player,
                "player2": self.Player2.score_Player
            },
            "players": {
                "player1": {
                    "name": self.Player1.name,
                    "type": self.Player1.perso.type,
                    "final_health": self.Player1.perso.health,
                    "final_energy": self.Player1.perso.energy,
                    "score": self.Player1.score_Player
                },
                "player2": {
                    "name": self.Player2.name,
                    "type": self.Player2.perso.type,
                    "final_health": self.Player2.perso.health,
                    "final_energy": self.Player2.perso.energy,
                    "score": self.Player2.score_Player
                }
            }
        }

    def update_screen(self):
        pygame.display.flip()

    def start(self):
        self.screen = setup_window(self.Width, self.Height, self.title, self.icon_path)

        # ⚡ POST-INIT DES PLAYERS (important pour les images)
        self.Player1.post_init()
        self.Player2.post_init()

        # --- TOUCHES: lettres pour les deux joueurs ---
        player1_controls = [
            pygame.K_q,  # gauche
            pygame.K_d,  # droite
            pygame.K_z,  # saut
            pygame.K_r,  # attaque1
            pygame.K_t,  # attaque2
            pygame.K_y,  # attaque3
            pygame.K_f   # protection
        ]
        
        player2_controls = [
            pygame.K_j,  # gauche (lettre)
            pygame.K_l,  # droite (lettre)
            pygame.K_i,  # saut (lettre)
            pygame.K_u,  # attaque1
            pygame.K_o,  # attaque2
            pygame.K_p,  # attaque3
            pygame.K_m   # protection
        ]

        # ⚡ CRÉATION DES CONTRÔLEURS (avec dimensions écran pour collisions)
        self.controller1 = PlayerController(
            player_instance=self.Player1,
            enemy_instance=self.Player2,
            projectile_group=self.all_projectiles,
            key_list=player1_controls,
            sound_manager=self.sound_manager,
            screen_width=self.Width,
            screen_height=self.Height
        )
        
        self.controller2 = PlayerController(
            player_instance=self.Player2,
            enemy_instance=self.Player1,
            projectile_group=self.all_projectiles,
            key_list=player2_controls,
            sound_manager=self.sound_manager,
            screen_width=self.Width,
            screen_height=self.Height
        )
        
        # Liaison croisée pour la protection
        self.controller1.enemy_controller = self.controller2
        self.controller2.enemy_controller = self.controller1

        # ⚡ CRÉATION DE L'AFFICHAGE
        self.display = GameDisplay(
            screen=self.screen,
            player1=self.Player1,
            player2=self.Player2,
            background_path=self.background_path,
            plan1_path=self.back_plan_1_path,
            icon_vs_path=self.icon_vs_path,
            font_path=self.font_path,
            font_size=self.font_size
        )

        # ⚡ CORRECTION : Afficher les types RÉELS des personnages
        print("🎮 Contrôles:")
        print(f"Joueur 1 ({self.Player1.perso.type.upper()}): Q/D (mouvement), Z (saut), R/T/Y (attaques), F (protection)")
        print(f"Joueur 2 ({self.Player2.perso.type.upper()}): J/L (mouvement), I (saut), U/O/P (attaques), M (protection)")
        print(f"🎯 Joueur 1: {self.Player1.name} ({self.Player1.perso.type}) - Vie: {self.Player1.perso.health} - Énergie: {self.Player1.perso.energy}")
        print(f"🎯 Joueur 2: {self.Player2.name} ({self.Player2.perso.type}) - Vie: {self.Player2.perso.health} - Énergie: {self.Player2.perso.energy}")
        print("\n📋 Règles:")
        print("- Les attaques consomment de l'énergie et infligent des dégâts")
        print("- Premier à 2 points gagne (minimum 1 point d'écart)")
        print("- KO = round gagné, double KO = 1 point chacun")

        self.game_loop()

    def game_loop(self):
        while self.running:
            events = pygame.event.get()
            
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False

            # Si la partie est finie, afficher les stats et quitter
            if not self.Fight:
                stats = self.get_game_stats()
                print("\n" + "="*50)
                print("🏆 PARTIE TERMINÉE 🏆")
                print("="*50)
                print(json.dumps(stats, indent=4, ensure_ascii=False))
                print("="*50 + "\n")
                self.running = False
                self.GamePlay = False
                continue

            # ⚡ GESTION DES ENTREES
            self.controller1.handle_input(events)
            self.controller2.handle_input(events)
            
            # Mettre à jour les projectiles
            self.all_projectiles.update()
            
            # Vérifier collisions projectiles
            for proj in list(self.all_projectiles):
                # Collision avec Player1
                if getattr(proj, "owner", None) != self.Player1 and proj.rect.colliderect(self.Player1.perso.perso_rect):
                    if not self.controller1.protect_active:
                        self.Player1.perso.health = max(self.Player1.perso.health - proj.damage, 0)
                        self.sound_manager.play('hit')
                        print(f"💥 {self.Player1.name} touché par projectile (-{proj.damage} dégâts)")
                    else:
                        self.sound_manager.play('block')
                        print(f"🛡️ {self.Player1.name} bloque le projectile!")
                    proj.kill()
                
                # Collision avec Player2
                if getattr(proj, "owner", None) != self.Player2 and proj.rect.colliderect(self.Player2.perso.perso_rect):
                    if not self.controller2.protect_active:
                        self.Player2.perso.health = max(self.Player2.perso.health - proj.damage, 0)
                        self.sound_manager.play('hit')
                        print(f"💥 {self.Player2.name} touché par projectile (-{proj.damage} dégâts)")
                    else:
                        self.sound_manager.play('block')
                        print(f"🛡️ {self.Player2.name} bloque le projectile!")
                    proj.kill()
            
            self.If_Ko()
            
            # ⚡ MISE À JOUR DE L'AFFICHAGE (avec projectiles)
            self.display.update(self.all_projectiles)
            
            self.clock.tick(60)


class FightGame(Game_Fight):
    def __init__(self):
        super().__init__()
        # Les variables sont déjà initialisées dans Game_Fight.__init__()
        print("🎲 FightGame initialisé!")