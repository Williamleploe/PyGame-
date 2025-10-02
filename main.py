import sys
sys.path.append("./classes")

import Personnages as personnage

# ===============================
# FONCTION DE JEU CLI
# ===============================

def tour_joueur(joueur, adversaire):
    joueur.regen_mana()
    print("\n" + "="*50)
    print(f"➡️  C'est le tour de {joueur.nom} !")
    joueur.statut()
    adversaire.statut()
    print("-"*50)
    
    while True:
        action = input(
            "Choisissez votre action :\n"
            "- 'a' = ⚔️ Attaque de base (7 mana)\n"
            "- 's' = 🔥 Attaque spéciale (15 mana)\n"
            "- 'e' = 🛡️ Bouclier (13 mana)\n"
            "Action: "
        ).lower()
        if action == 'a':
            joueur.attaquer_base(adversaire)
            break
        elif action == 's':
            joueur.attaquer_special(adversaire)
            break
        elif action == 'e':
            joueur.bouclier()
            break
        else:
            print("❌ Action invalide, veuillez réessayer !")


# ===============================
# BOUCLE DE JEU PRINCIPALE
# ===============================

def jeu_1v1():
    joueur1 = personnage.Guerrier("Guerrier")
    joueur2 = personnage.Mage("Mage")
    
    while joueur1.vie > 0 and joueur2.vie > 0:
        tour_joueur(joueur1, joueur2)
        if joueur2.vie <= 0:
            break
        tour_joueur(joueur2, joueur1)

    print("\n" + "="*50)
    if joueur1.vie <= 0 and joueur2.vie <= 0:
        print("🤝 Égalité ! Les deux personnages sont tombés.")
    elif joueur1.vie <= 0:
        print(f"🏆 {joueur2.nom} a gagné !")
    else:
        print(f"🏆 {joueur1.nom} a gagné !")
    print("="*50)


# ===============================
# LANCEMENT DU JEU
# ===============================

if __name__ == "__main__":
    jeu_1v1()
