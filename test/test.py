import pygame
import sys

# Initialisation
pygame.init()

# Création de la fenêtre
largeur, hauteur = 640, 480
screen = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Exemple Pygame")

# Couleurs (R, G, B)
BLANC = (255, 255, 255)
ROUGE = (255, 0, 0)

# Position et vitesse du cercle
x, y = largeur // 2, hauteur // 2
vitesse_x, vitesse_y = 3, 2
rayon = 30

# Boucle principale
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Déplacer le cercle
    x += vitesse_x
    y += vitesse_y

    # Rebondir sur les bords
    if x - rayon < 0 or x + rayon > largeur:
        vitesse_x = -vitesse_x
    if y - rayon < 0 or y + rayon > hauteur:
        vitesse_y = -vitesse_y

    # Remplir l'écran
    screen.fill(BLANC)

    # Dessiner le cercle
    pygame.draw.circle(screen, ROUGE, (x, y), rayon)

    # Mettre à jour l'écran
    pygame.display.flip()
    clock.tick(60)  # 60 FPS

pygame.quit()
sys.exit()
