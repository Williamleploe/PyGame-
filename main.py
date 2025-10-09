import sys
import pygame
sys.path.append("./classes")
from game import Game
from main_menu import MainMenu
pygame.init()

if __name__ == "__main__":
    game = Game()
    game.run()