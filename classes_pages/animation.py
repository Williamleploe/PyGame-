import json


with open("classes/json/animations.json", "r") as file:
    persos_animation = json.load(file)

# --- Fonction pour récupérer les frames d'une animation ---
def get_animation_frames(personnage_nom, animation_nom):
    for perso in persos_animation:
        if perso["nom"] == personnage_nom:
            animations = perso["animations"]
            if animation_nom in animations:
                return animations[animation_nom]
            else:
                print(f"Animation '{animation_nom}' non trouvée pour {personnage_nom}")
                return []
    print(f"Personnage '{personnage_nom}' non trouvé")
    return []

# # --- MAIN DE TEST ---
# if __name__ == "__main__":
#     BASE_PATH = "assets/perso"
#     perso_name = "Converted_Vampire"
#     anim_name = "attack_1"
#     frames = get_animation_frames(perso_name, anim_name)
#     if frames:
#         print(f"\n Animation '{anim_name}' trouvée pour '{perso_name}' :")
#         for frame in frames:
#             full_path = f"{BASE_PATH}/{perso_name}/{anim_name}/{frame}"
#             print(" →", full_path)
#     else:
#         print(f"Impossible de trouver '{anim_name}' pour '{perso_name}'.")
