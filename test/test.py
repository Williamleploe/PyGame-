# import pygame  # On importe la bibliothèque pygame

# pygame.init()  # On initialise tous les modules nécessaires de pygame (fenêtre, sons, etc.)

# # On crée une fenêtre de 600 pixels de large sur 400 pixels de haut
# pygame.display.set_mode((600, 400))

# # On définit une variable de contrôle pour maintenir la boucle du jeu en marche
# running = True  

# # Boucle principale du jeu (tant que 'running' est True, la fenêtre reste ouverte)
# while running:
#     # On récupère tous les événements générés (clavier, souris, fermeture de fenêtre, etc.)
#     for event in pygame.event.get():
#         # Si l’événement est de type "QUIT" (clic sur la croix rouge de la fenêtre)
#         if event.type == pygame.QUIT:
#             # On change la variable pour sortir de la boucle
#             running = False

# # Quand on sort de la boucle, on ferme proprement pygame
# pygame.quit()