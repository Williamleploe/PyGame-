# classes_jeu/save.py
import json
import threading
import os
from classes_jeu.utils import FILE_SETUP

class Save:
    def __init__(self, fight, file_path=FILE_SETUP, interval=5):
        self.fight = fight
        self.file = file_path
        self.auto_save_interval = interval
        self.auto_save_active = False
        self.lock = threading.Lock()

    def _player_to_dict(self, idx, player):
        # assure que les valeurs du perso sont à jour
        if hasattr(player.perso, "update_values_from_rect"):
            player.perso.update_values_from_rect()
        return {
            "id": idx,
            "name": getattr(player.perso, "name", None),
            "path": getattr(player.perso, "path", f"assets/perso/{getattr(player.perso, 'name', '')}"),
            "idle_image": getattr(player.perso, "idle_path", ""),
            "position": getattr(player, "position", ""),
            "type_personnage": getattr(player.perso, "type", ""),
            "health": getattr(player.perso, "health", 100),
            "energy": getattr(player.perso, "energy", 100),
            "score": getattr(player, "score_Player", 0),
            "perso.perso_rect": {
                "x": getattr(player.perso, "x", 0),
                "y": getattr(player.perso, "y", 0),
                "width": getattr(player.perso, "width", 128),
                "height": getattr(player.perso, "height", 128)
            },
            "direction": getattr(player, "direction", False)
        }

    def create_save_json(self):
        save_data = {}

        # Map : on essaie d'extraire un "name" depuis le chemin si possible
        bg = getattr(self.fight, "background_path", "")
        plan = getattr(self.fight, "back_plan_1_path", "")
        map_name = None
        if bg:
            try:
                parts = os.path.normpath(bg).split(os.sep)
                # si chemin = assets/background/<map_name>/...
                if "background" in parts:
                    i = parts.index("background")
                    if len(parts) > i+1:
                        map_name = parts[i+1]
            except Exception:
                map_name = None

        save_data["map"] = {
            "name": map_name,
            "background": bg,
            "plan": plan
        }

        save_data["players"] = []
        players = [getattr(self.fight, "Player1", None), getattr(self.fight, "Player2", None)]
        for idx, player in enumerate(players, start=1):
            if player is None:
                continue
            save_data["players"].append(self._player_to_dict(idx, player))

        os.makedirs(os.path.dirname(self.file), exist_ok=True)
        with open(self.file, 'w', encoding='utf-8') as f:
            json.dump(save_data, f, ensure_ascii=False, indent=4)
        print(f"💾 Sauvegarde effectuée -> {self.file}")

    def auto_save(self):
        if self.auto_save_active:
            with self.lock:
                self.create_save_json()
            threading.Timer(self.auto_save_interval, self.auto_save).start()

    def start_auto_save(self):
        self.auto_save_active = True
        self.auto_save()

    def stop_auto_save(self):
        self.auto_save_active = False
