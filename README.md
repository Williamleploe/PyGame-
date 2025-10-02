# Guide des fonctions principales de Pygame

Ce document présente les fonctions et modules principaux de **Pygame**, ainsi que leur utilité, sans montrer de code d’implémentation.

---

## ⚙️ Initialisation et gestion

- **`pygame.init()`** : Initialise tous les modules nécessaires de Pygame (sons, images, fenêtres, etc.).  
- **`pygame.quit()`** : Ferme proprement Pygame et libère les ressources utilisées.  

---

## 🖼️ Fenêtre et affichage

- **`pygame.display.set_mode()`** : Crée la fenêtre de jeu avec une taille définie.  
- **`pygame.display.set_caption()`** : Change le titre de la fenêtre.  
- **`pygame.display.update()` / `pygame.display.flip()`** : Rafraîchissent l’écran pour montrer les changements graphiques.  

---

## 🎨 Surface et dessin

- **Surface (objet)** : Feuille de dessin où l’on peut placer des images ou dessiner des formes.  
- **`fill()`** : Remplit une surface avec une couleur.  
- **`blit()`** : Copie une image ou une surface sur une autre (placement de sprites).  
- **Fonctions de dessin (`draw`)** : Dessinent des formes simples comme rectangles, cercles, lignes, etc.  

---

## 🎮 Événements et interactions

- **`pygame.event.get()`** : Récupère la liste des événements (clavier, souris, fermeture de fenêtre…).  
- **`pygame.key.get_pressed()`** : Vérifie quelles touches sont actuellement enfoncées.  
- **`pygame.mouse.get_pos()`** : Donne la position de la souris.  

---

## 🎵 Son et musique

- **`pygame.mixer.Sound()`** : Charge et joue un effet sonore.  
- **`pygame.mixer.music`** : Gère la lecture de musiques plus longues (lecture, pause, arrêt, volume…).  

---

## ⏱️ Temps et horloge

- **`pygame.time.Clock()`** : Contrôle la vitesse du jeu (images par seconde).  
- **`pygame.time.get_ticks()`** : Donne le temps écoulé depuis le lancement du programme.  

---

## 🖼️ Images et sprites

- **`pygame.image.load()`** : Charge une image depuis un fichier.  
- **Sprites (`pygame.sprite.Sprite` et `pygame.sprite.Group`)** : Système pour gérer des personnages ou objets, avec leurs collisions et mises à jour automatiques.  

---

## 🔗 Résumé des modules principaux

| Module        | Utilité principale                                         |
|---------------|------------------------------------------------------------|
| Display/Surface | Gérer l’écran et les dessins                               |
| Event          | Gérer les interactions du joueur                           |
| Mixer          | Gérer les sons et musiques                                  |
| Time/Clock     | Contrôler le temps et les FPS                               |
| Sprites        | Faciliter la gestion d’objets et leurs collisions          |

---

Ce guide est une introduction aux fonctions principales de Pygame pour aider à organiser un projet ou à se repérer rapidement.
