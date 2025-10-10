# 🥊 Jeu de Combat - Albertos vs Albertas (Pygame)

Un jeu de combat en **Python** développé avec **Pygame**, inspiré de *Street Fighter* et *Mortal Kombat*.  
Ce projet a été réalisé dans le cadre d’un **projet noté** en deuxième année d’informatique.  

---

## 👥 Groupe de développement

**Groupe :**
- 🧑‍💻 MAUSSANT Mathéo  
- 👨‍💻 AGUER Hugo  
- 👨‍💻 KROMMER William  

---

## 🚀 Fonctionnalités principales

- 🎮 Menu principal avec gestion de sauvegarde (`setup.json`)
- 🗺️ Sélection de la map avec aperçu dynamique
- 👊 Choix de deux personnages jouables :  
  - Converted Vampire (**mêlée**)  
  - Countess Vampire (**distance**)
- ⚔️ Combat en **1v1** sur un maximum de **3 manches**
- 🏆 Écran de victoire affichant le gagnant avec boutons **Restart** et **Menu principal**
- 💾 Sauvegarde automatique de la partie (`setup.json`)
- 🌄 Interface fluide et fond animé

---

## ⚔️ Règles du jeu

- Le jeu oppose **deux joueurs en duel (1v1)**.  
- Chaque victoire rapporte **1 point** à un joueur.  
- Le **premier joueur à atteindre 2 points** remporte la partie.  
- En cas d’égalité (**1 - 1**), une **troisième manche** est automatiquement lancée pour départager les joueurs.

---

## 🎮 Les touches de jeu pour chaque joueur : 

```
JOUEUR 1 (AZERTY)        JOUEUR 2
    Z (Saut)                I (Saut)
Q ← → D (Déplacement)   J ← → L (Déplacement)
    R (Att1)                U (Att1)
    T (Att2)                O (Att2)
    Y (Att3)                P (Att3)
    F (Protection)          M (Protection)
```

---

## 🧠 Structure du projet

```
.
├── assets
│   ├── armes_a_effet
│   ├── background
│   ├── fonts
│   ├── GUI
│   ├── icon.png
│   ├── perso
│   ├── sounds
│   └── vs.png
├── classes_jeu # ---------------------- GESTION DE LA LOGIQUE DE JEU
│   ├── controller.py
│   ├── display.py
│   ├── fight.py
│   ├── perso.py
│   ├── player_file.py
│   ├── projectile.py
│   ├── __pycache__
│   ├── save.py
│   ├── sound.py
│   └── utils.py
├── classes_pages   # ------------------ GESTION DES PAGES
│   ├── a_faire.txt
│   ├── animation.py
│   ├── choose_character.py
│   ├── choose_map.py
│   ├── game.py
│   ├── json
│   ├── main_menu.py
│   ├── __pycache__
│   └── victory.py
├── main.py   # ------------------------ LANCEMENT DU JEU
├── README.md
└── utils
    └── init_paths.py
```

---

## ⚙️ Installation & Lancement

### 1️⃣ Prérequis

- Python **3.10 ou supérieur**
- Module **pygame** installé

### 2️⃣ Installation des dépendances

```bash
pip install pygame
```

### 3️⃣ Lancer le jeu

Depuis la **racine du projet**, exécutez :

```bash
python ./main.py
```

ou

```bash
python3 ./main.py
```

---

🧛‍♂️ *Préparez-vous à combattre... Que le meilleur vampire gagne !*
