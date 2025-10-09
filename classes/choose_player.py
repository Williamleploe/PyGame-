import pygame
import json
pygame.init()

class Choose_Player:
    def __init__(self, game):
        self.game = game
        self.WIDTH = game.WIDTH
        self.HEIGHT = game.HEIGHT
        self.players = ["Converted_Vampire", "Countess_Vampire"]
        self.selected = []
        self.font = pygame.font.Font(None, 60)
        self.buttons = []
        self.create_buttons()

    def create_buttons(self):
        x, y = 400, 250
        for p in self.players:
            rect = pygame.Rect(x, y, 400, 100)
            text = self.font.render(p, True, (255, 0, 0))
            text_rect = text.get_rect(center=rect.center)
            self.buttons.append({"rect": rect, "text": text, "text_rect": text_rect, "name": p})
            y += 200

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            for button in self.buttons:
                if button["rect"].collidepoint(pos):
                    print(f"Personnage {button['name']} sélectionné !")
                    self.add_player(button["name"])

    def add_player(self, name):
        # charge setup.json
        with open("setup.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        # créer joueur
        player_id = len(data["players"]) + 1
        player_data = {
            "id": player_id,
            "name": name,
            "path": f"assets/perso/{name}",
            "idle_image": f"assets/perso/{name}/idle/00.png",
            "position": "left" if player_id == 1 else "right",
            "type_personnage": "melee" if player_id == 1 else "range",
            "health": 100,
            "energy": 50,
            "score": 0
        }
        data["players"].append(player_data)

        # sauvegarde
        with open("setup.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

        print(f"💾 Joueur {name} sauvegardé dans setup.json")

        if len(data["players"]) >= 2:
            print("✅ Deux joueurs sélectionnés. Prêt au combat !")
            # ici tu peux lancer la partie réelle
            self.game.change_page("menu")  # retour au menu principal

    def update(self):
        pass

    def draw(self, screen):
        screen.fill((0, 0, 0))
        title = self.font.render("Choisis ton personnage", True, (255, 0, 0))
        screen.blit(title, (self.WIDTH // 2 - title.get_width() // 2, 100))
        for button in self.buttons:
            pygame.draw.rect(screen, (255, 255, 255), button["rect"], 2)
            screen.blit(button["text"], button["text_rect"])
