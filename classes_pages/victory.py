import pygame
import json

class VictoryScreen:
    def __init__(self, game, game_stats):
        """
        game_stats = {
            "winner": "Countess_Vampire",
            "final_score": {"player1": 2, "player2": 0},
            "players": {
                "player1": {"name": "...", "type": "...", "final_health": ..., "final_energy": ..., "score": ...},
                "player2": {...}
            }
        }
        """
        self.game = game
        self.Width = game.WIDTH
        self.Height = game.HEIGHT
        self.stats = game_stats
        
        # 🔄 Conversion des noms techniques vers noms d'affichage
        NAME_MAPPING = {
            "Converted_Vampire": "Albertos",
            "Countess_Vampire": "Albertas"
        }
        
        # Déterminer qui a gagné (Player 1 ou Player 2)
        winner_name = self.stats.get("winner", "")
        # Convertir le nom technique en nom d'affichage
        winner_display_name = NAME_MAPPING.get(winner_name, winner_name)
        
        self.winner_player = None
        if self.stats["players"]["player1"]["name"] == winner_name:
            self.winner_player = "JOUEUR 1"
            self.winner_color = (255, 255, 0)  # Jaune
            self.winner_character = winner_display_name
        elif self.stats["players"]["player2"]["name"] == winner_name:
            self.winner_player = "JOUEUR 2"
            self.winner_color = (0, 255, 0)  # Vert
            self.winner_character = winner_display_name
        else:
            self.winner_player = "ÉGALITÉ"
            self.winner_color = (255, 255, 255)
            self.winner_character = ""
        
        # Charger le fond
        try:
            bg = pygame.image.load("assets/background/back/2 background/orig.png").convert()
            self.background = pygame.transform.scale(bg, (self.Width, int(self.Width * (bg.get_height() / bg.get_width()))))
            self.background_rect = self.background.get_rect(center=(self.Width // 2, self.Height // 2))
        except Exception:
            self.background = pygame.Surface((self.Width, self.Height))
            self.background.fill((20, 20, 40))
            self.background_rect = self.background.get_rect()
        
        # Polices
        self.title_font = pygame.font.Font(game.font, 80)
        self.subtitle_font = pygame.font.Font(game.font, 50)
        self.text_font = pygame.font.Font(game.font, 35)
        self.button_font = pygame.font.Font(game.font, 40)
        
        # Bouton retour au menu
        self.menu_button_text = self.button_font.render("RETOUR AU MENU", True, (255, 255, 255))
        self.menu_button_rect = self.menu_button_text.get_rect(center=(self.Width // 2, self.Height - 80))
        
        # Animation
        self.alpha = 0
        self.fade_in_speed = 5
        
        # Jouer un son de victoire
        if hasattr(game, 'sound_manager'):
            game.sound_manager.play('game_over')

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.menu_button_rect.collidepoint(event.pos):
                # Jouer son de clic
                if hasattr(self.game, 'sound_manager'):
                    self.game.sound_manager.play('armor')
                
                # Retourner au menu principal
                print("🔙 Retour au menu principal")
                return True  # Signal pour retourner au menu
        return False  # ⚡ IMPORTANT: retourner False si pas de clic

    def update(self):
        # Animation fade-in
        if self.alpha < 255:
            self.alpha = min(255, self.alpha + self.fade_in_speed)

    def draw(self, screen):
        # Fond
        screen.blit(self.background, self.background_rect)
        
        # Overlay semi-transparent
        overlay = pygame.Surface((self.Width, self.Height))
        overlay.set_alpha(200)
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))
        
        # Titre "VICTOIRE" en BLANC
        victory_title = self.title_font.render("VICTOIRE", True, (255, 255, 255))
        victory_rect = victory_title.get_rect(center=(self.Width // 2, 100))
        screen.blit(victory_title, victory_rect)
        
        # "DU" en blanc
        du_text = self.subtitle_font.render("DU", True, (255, 255, 255))
        du_rect = du_text.get_rect(center=(self.Width // 2, 180))
        screen.blit(du_text, du_rect)
        
        # Gagnant "JOUEUR X" en JAUNE (P1) ou VERT (P2)
        winner_text = self.subtitle_font.render(f"{self.winner_player}", True, self.winner_color)
        winner_rect = winner_text.get_rect(center=(self.Width // 2, 240))
        screen.blit(winner_text, winner_rect)
        
        # Nom du personnage (Albertos/Albertas) en dessous
        if self.winner_character:
            char_text = self.text_font.render(f"({self.winner_character})", True, self.winner_color)
            char_rect = char_text.get_rect(center=(self.Width // 2, 290))
            screen.blit(char_text, char_rect)
        
        # Score final
        score = self.stats["final_score"]
        score_text = self.text_font.render(
            f"Score final: {score['player1']} - {score['player2']}", 
            True, (255, 255, 255)
        )
        score_rect = score_text.get_rect(center=(self.Width // 2, 340))
        screen.blit(score_text, score_rect)
        
        # Statistiques des joueurs
        y_offset = 400
        NAME_MAPPING = {
            "Converted_Vampire": "Albertos",
            "Countess_Vampire": "Albertas"
        }
        
        for idx, (key, player) in enumerate(self.stats["players"].items(), start=1):
            color = (255, 255, 0) if idx == 1 else (0, 255, 0)
            
            # Convertir le nom technique en nom d'affichage
            display_name = NAME_MAPPING.get(player['name'], player['name'])
            
            # Nom du joueur
            name_text = self.text_font.render(
                f"Joueur {idx}: {display_name} ({player['type'].upper()})", 
                True, color
            )
            name_rect = name_text.get_rect(center=(self.Width // 2, y_offset))
            screen.blit(name_text, name_rect)
            
            # Stats
            stats_text = self.text_font.render(
                f"Vie: {player['final_health']} | Énergie: {player['final_energy']} | Rounds: {player['score']}", 
                True, (200, 200, 200)
            )
            stats_rect = stats_text.get_rect(center=(self.Width // 2, y_offset + 35))
            screen.blit(stats_text, stats_rect)
            
            y_offset += 90
        
        # Bouton retour au menu (avec effet hover)
        mouse_pos = pygame.mouse.get_pos()
        if self.menu_button_rect.collidepoint(mouse_pos):
            button_text = self.button_font.render("RETOUR AU MENU", True, (255, 255, 0))
        else:
            button_text = self.menu_button_text
        
        # Bordure du bouton
        pygame.draw.rect(screen, (255, 255, 255), self.menu_button_rect.inflate(20, 10), 3)
        screen.blit(button_text, self.menu_button_rect)
        
        pygame.display.flip()