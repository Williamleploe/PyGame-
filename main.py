import pygame
import sys
from classes_jeu.fight import FightGame
from classes_pages.game import Game
from classes_jeu.utils import open_json

pygame.init()

def run_game():
    """Démarre directement un combat si une sauvegarde existe"""
    setup_data = open_json("classes_pages/json/setup.json")

    if setup_data:
        print("💾 Sauvegarde trouvée, chargement...")
    else:
        print("🆕 Nouvelle partie !")

    game = FightGame()
    game.start()

def main():
    """Démarre le menu principal du jeu"""
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
