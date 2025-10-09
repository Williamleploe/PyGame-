import pygame

class Choose_Player:
    def __init__(self, game):
        self.game = game
        self.WIDTH = game.WIDTH
        self.HEIGHT = game.HEIGHT

        # --- Configuration des personnages ---
        self.characters = ["Perso A", "Perso B"]

        # --- Couleurs ---
        self.bg_color = (20, 20, 30)
        self.text_color = (255, 255, 255)
        self.selection_color = (255, 50, 50)

        # --- États de sélection ---
        self.player1_choice = None
        self.player2_choice = None

        # --- Police ---
        self.font = pygame.font.SysFont("arial", 36)

    def reset_choices(self):
        """Réinitialise les choix des joueurs"""
        self.player1_choice = None
        self.player2_choice = None

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos

            # --- Zones de clic pour les persos ---
            # Perso A (à gauche)
            if 200 <= x <= 500 and 300 <= y <= 400:
                self.select_character("Perso A")

            # Perso B (à droite)
            elif 780 <= x <= 1080 and 300 <= y <= 400:
                self.select_character("Perso B")

    def select_character(self, name):
        """Assigne un perso au joueur suivant"""
        if self.player1_choice is None:
            self.player1_choice = name
            print(f"🎮 Joueur 1 a choisi : {name}")
        elif self.player2_choice is None:
            self.player2_choice = name
            print(f"🎮 Joueur 2 a choisi : {name}")
            self.end_selection()

    def end_selection(self):
        """Les deux joueurs ont choisi"""
        print("✅ Sélection terminée !")
        print(f"Map : {self.game.selected_map}")
        print(f"Joueur 1 : {self.player1_choice}")
        print(f"Joueur 2 : {self.player2_choice}")

        # Ici ton pote pourra lancer le vrai combat !
        pygame.time.wait(2000)
        self.game.running = False

    def update(self):
        pass  # Pas de logique à mettre à jour pour l’instant

    def draw(self, screen):
        """Affiche le menu de sélection des personnages"""
        screen.fill(self.bg_color)

        title = self.font.render("Choisissez vos personnages", True, self.text_color)
        screen.blit(title, (self.WIDTH // 2 - title.get_width() // 2, 100))

        # --- Affichage des deux persos ---
        for i, name in enumerate(self.characters):
            x = 200 if i == 0 else 780
            rect = pygame.Rect(x, 300, 300, 100)
            color = self.selection_color if (
                name == self.player1_choice or name == self.player2_choice
            ) else (150, 150, 150)
            pygame.draw.rect(screen, color, rect)
            text = self.font.render(name, True, (0, 0, 0))
            screen.blit(text, (rect.centerx - text.get_width() // 2, rect.centery - 20))

        # --- Affiche les choix actuels ---
        p1 = f"Joueur 1 : {self.player1_choice or '...'}"
        p2 = f"Joueur 2 : {self.player2_choice or '...'}"
        t1 = self.font.render(p1, True, self.text_color)
        t2 = self.font.render(p2, True, self.text_color)
        screen.blit(t1, (150, 550))
        screen.blit(t2, (750, 550))
