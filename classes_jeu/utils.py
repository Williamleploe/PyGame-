import json, pygame, os
pygame.init()

FILE_SETUP = "classes_pages/json/setup.json"

def open_json(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def insert_data_json(path, new_data):
    data = open_json(path)
    data.update(new_data)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def setup_window(W, H, title, icon_path):
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption(title)
    try:
        icon = pygame.image.load(icon_path)
        pygame.display.set_icon(icon)
    except Exception as e:
        print("⚠️ Icon introuvable:", icon_path, e)
    return screen

class Utils:
    def __init__(self):
        pass
    def font_setup(self , font_path , font_size):
        try:
            my_font = pygame.font.Font(font_path, font_size)
        except Exception:
            my_font = pygame.font.SysFont(None, font_size)
        return my_font

    def build_game_json(self, map_choice=None, players=None, width=1280, height=700):
        """Construit le JSON pour le jeu avec valeurs par défaut si nécessaire"""
        data = {}
        # Map
        if map_choice:
            map_name = map_choice.get("name", "")
            data["map"] = {
                "name": map_name,
                "background": f"assets/background/{map_name}/Preview 1.png",
                "plan": f"assets/background/{map_name}/Plan 1.png"
            }
        else:
            data["map"] = {}
        # Players
        data["players"] = []
        default_positions = [148, 832]
        default_types = ["melee", "range"]
        for idx, player in enumerate(players if players else [{} for _ in range(2)]):
            name = player.get("name", f"Player{idx+1}")
            type_personnage = player.get("type", default_types[idx])
            x_pos = default_positions[idx]
            player_json = {
                "id": idx,
                "name": name,
                "path": f"assets/perso/{name}",
                "idle_image": f"assets/perso/{name}/idle/00.png",
                "position": "left" if idx == 0 else "right",
                "type_personnage": type_personnage,
                "health": 100,
                "energy": 100,
                "score": 0,
                "perso.perso_rect": {
                    "x": x_pos,
                    "y": height - 120 - 128,
                    "width": 128,
                    "height": 128
                },
                "direction": False if idx == 0 else True
            }
            data["players"].append(player_json)
        return data

    def scale(self, coef, image=None, image_path=None, rect=None):
        if image is not None or image_path is not None:
            if image_path is not None:
                image = pygame.image.load(image_path)
            new_width = int(image.get_width() * coef)
            new_height = int(image.get_height() * coef)
            return pygame.transform.scale(image, (new_width, new_height))
        elif rect is not None:
            new_rect = rect.copy()
            new_rect.width = int(rect.width * coef)
            new_rect.height = int(rect.height * coef)
            new_rect.center = rect.center
            return new_rect
        return None
    
    def flip(self, obj, horizontal=True, vertical=False):
        if isinstance(obj, pygame.Surface):
            return pygame.transform.flip(obj, horizontal, vertical)
        elif isinstance(obj, pygame.Rect):
            new_rect = obj.copy()
            if horizontal:
                new_rect.x = -new_rect.right
            if vertical:
                new_rect.y = -new_rect.bottom
            return new_rect
        
    def flip_surface_keep_position(self, surface, rect, horizontal=True, vertical=False, direction=False):
        if direction:
            flipped_surface = pygame.transform.flip(surface, horizontal, vertical)
        else:
            flipped_surface = surface
        new_rect = flipped_surface.get_rect()
        new_rect.center = rect.center
        return flipped_surface, new_rect
