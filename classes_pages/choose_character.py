import pygame
from classes_jeu.utils import insert_data_json, FILE_SETUP

ALIAS_TO_REALNAME = {"Albertos":"Converted_Vampire","Albertas":"Countess_Vampire"}
DEFAULT_PLAYER_STATS = {
    "Albertos":{"type_personnage":"melee","health":100,"energy":100,"idle_image":"assets/perso/Converted_Vampire/idle/00.png","path":"assets/perso/Converted_Vampire","width":128,"height":128},
    "Albertas":{"type_personnage":"range","health":100,"energy":100,"idle_image":"assets/perso/Countess_Vampire/idle/00.png","path":"assets/perso/Countess_Vampire","width":128,"height":128}
}

class ChooseCharacter:
    def __init__(self, game):
        self.game, self.Width, self.Height = game, game.WIDTH, game.HEIGHT
        bg = pygame.image.load("assets/background/back/2 background/orig.png").convert()
        self.BACKGROUND = pygame.transform.scale(bg,(self.Width,int(self.Width*(bg.get_height()/bg.get_width()))))
        self.background_rect = self.BACKGROUND.get_rect(center=(self.Width//2,self.Height//2))
        self.title_font, self.button_font, self.small_font = pygame.font.Font(self.game.font,60), pygame.font.Font(self.game.font,40), pygame.font.Font(self.game.font,35)
        self.characters, self.player1_choice, self.player2_choice, self.play_enabled = list(DEFAULT_PLAYER_STATS.keys()), None, None, False
        self.buttons=[]
        self.setup_buttons()

    def setup_buttons(self):
        self.buttons=[]
        p1x, p2x, start_y, spacing_y = self.Width//4, self.Width*3//4, 200, 80
        self.title = self.title_font.render("CHOISISSEZ VOS PERSONNAGES", True,(255,255,255))
        self.title_rect = self.title.get_rect(center=(self.Width//2,80))
        self.title1 = self.button_font.render("Joueur 1", True,(255,255,0))
        self.title1_rect = self.title1.get_rect(center=(p1x,start_y))
        self.title2 = self.button_font.render("Joueur 2", True,(0,255,0))
        self.title2_rect = self.title2.get_rect(center=(p2x,start_y))
        for i,char in enumerate(self.characters):
            y = start_y + (i+1)*spacing_y
            self.buttons.append({"surface":self.button_font.render(char,True,(255,255,0)),"rect":self.button_font.render(char,True,(255,255,0)).get_rect(center=(p1x,y)),"name":char,"player":1})
            self.buttons.append({"surface":self.button_font.render(char,True,(0,255,0)),"rect":self.button_font.render(char,True,(0,255,0)).get_rect(center=(p2x,y)),"name":char,"player":2})
        self.play_text = self.button_font.render("PLAY", True,(255,255,255))
        self.play_rect = self.play_text.get_rect(center=(self.Width//2,self.Height-100))

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # 🔊 Vérifier clic sur les boutons de personnages
            for b in self.buttons:
                if b["rect"].collidepoint(event.pos):
                    # Jouer le son de clic
                    if hasattr(self.game, 'sound_manager'):
                        self.game.sound_manager.play('armor')  # Utilise armor.wav comme clic
                    
                    if b["player"] == 1:
                        self.player1_choice = b["name"]
                    else:
                        self.player2_choice = b["name"]
            
            self.play_enabled = self.player1_choice and self.player2_choice
            
            # 🔊 Vérifier clic sur le bouton PLAY
            if self.play_enabled and self.play_rect.collidepoint(event.pos):
                # Jouer le son de clic
                if hasattr(self.game, 'sound_manager'):
                    self.game.sound_manager.play('debut_combat')  # Son spécial pour PLAY
                self.launch_game()

    def launch_game(self):
        players=[]
        for idx,alias in enumerate([self.player1_choice,self.player2_choice]):
            s = DEFAULT_PLAYER_STATS[alias]
            players.append({"id":idx+1,"name":ALIAS_TO_REALNAME[alias],"path":s["path"],"idle_image":s["idle_image"],
                            "position":"left" if idx==0 else "right","type_personnage":s["type_personnage"],
                            "health":s["health"],"energy":s["energy"],"score":0,
                            "perso_rect":{"x":148 if idx==0 else 832,"y":450,"width":s["width"],"height":s["height"]},
                            "direction":False if idx==0 else True})
        insert_data_json(FILE_SETUP, {"map":self.game.game_setup["map"],"players":players})
        self.game.GamePlay=True

    def update(self): pass

    def draw(self,screen):
        screen.blit(self.BACKGROUND,self.background_rect)
        screen.blit(self.title,self.title_rect)
        screen.blit(self.title1,self.title1_rect)
        screen.blit(self.title2,self.title2_rect)
        for b in self.buttons: screen.blit(b["surface"],b["rect"])
        if self.player1_choice:
            txt=self.small_font.render(f"Choix: {self.player1_choice}", True,(255,255,0))
            screen.blit(txt,txt.get_rect(center=(self.Width//4,self.Height//2-20)))
        if self.player2_choice:
            txt=self.small_font.render(f"Choix: {self.player2_choice}", True,(0,255,0))
            screen.blit(txt,txt.get_rect(center=(self.Width*3//4,self.Height//2-20)))
        screen.blit(self.play_text,self.play_rect)