# 🥊 Fighting Game Project (Pygame)

Un jeu de combat en **Python** développé avec **Pygame**, inspiré de *Street Fighter* et *Mortal Kombat*.  
Ce projet a été réalisé dans le cadre d’un **projet noté** en deuxième année d’informatique.  

---

## 🚀 Fonctionnalités principales

- 🎮 Menu principal avec gestion de sauvegarde (setup.json)
- 🗺️ Sélection de la map avec aperçu dynamique
- 👊 Choix de deux personnages jouables :  
  - Converted Vampire (melee)  
  - Countess Vampire (range)
- 🏆 Écran de victoire affichant le gagnant avec boutons **Restart** et **Menu principal**
- 💾 Sauvegarde automatique de la partie (setup.json)
- 🌄 Interface fluide et fond animé

---

## 🧠 Structure du projet

PyGame-/
│
├── main.py # Point d’entrée du jeu
├── setup.json # Fichier de sauvegarde de la partie
│
├── classes/ # Dossier contenant toutes les pages
│ ├── game.py # Gestionnaire principal des pages et de la boucle de jeu
│ ├── main_menu.py # Écran titre / menu principal
│ ├── choose_map.py # Sélection de la map
│ ├── choose_player.py # Sélection des personnages
│ └── victory.py # Écran de victoire
│
└── assets/ # Ressources du jeu
├── background/ # Images des cartes et fonds
└── perso/ # Sprites des personnages

yaml
Copier le code

---

## ⚙️ Installation & Lancement

### 1️⃣ Installer Python (3.10+ recommandé)
👉 [Télécharger Python](https://www.python.org/downloads/)

### 2️⃣ Installer les dépendances
```bash
pip install pygame
