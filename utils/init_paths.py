import os , sys 

def setup_imports():
    """
    Ajoute automatiquement les bons chemins pour les imports
    des dossiers classes_jeu et classes_pages.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(current_dir)

    classes_jeu_path = os.path.join(root_dir, "classes_jeu")
    classes_pages_path = os.path.join(root_dir, "classes_pages")

    sys.path.insert(0, classes_jeu_path)
    sys.path.insert(0, classes_pages_path)

    print(f"🔍 Recherche dans classes_jeu: {classes_jeu_path}")
    if os.path.exists(classes_jeu_path):
        print(f"  Contenu: {os.listdir(classes_jeu_path)}")
    else:
        print("  ⚠️  Dossier classes_jeu non trouvé !")

    print(f"🔍 Recherche dans classes_pages: {classes_pages_path}")
    if os.path.exists(classes_pages_path):
        print(f"  Contenu: {os.listdir(classes_pages_path)}")
    else:
        print("  ⚠️  Dossier classes_pages non trouvé !")
