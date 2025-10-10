import pygame
import os

pygame.init()

class SoundManager():
    def __init__(self):
        try:
            pygame.mixer.init()
        except Exception as e:
            print("⚠️ Impossible d'initialiser le mixer:", e)
        self.sounds = {}
        self.load_sounds()
        self.background_music_path = "assets/sounds/fond/track_2.mp3"
        self.play_background_music()

    def load_sounds(self):
        files = {
            'armor': 'assets/sounds/armor.wav',
            'debut_combat': 'assets/sounds/debut_combat.wav',
            'fire_ball': 'assets/sounds/fire_ball.wav',
            'footstep': 'assets/sounds/foot_step.wav',
            'game_over': 'assets/sounds/game_over.wav',
            'jump': 'assets/sounds/jump.wav',
            'melee_hit': 'assets/sounds/sword.wav'
        }

        class DummySound:
            def play(self): pass
            def set_volume(self, v): pass

        for name, path in files.items():
            if os.path.exists(path):
                try:
                    snd = pygame.mixer.Sound(path)
                    snd.set_volume(0.4)
                    self.sounds[name] = snd
                except Exception as e:
                    print(f"⚠️ Erreur chargement son {path}:", e)
                    self.sounds[name] = DummySound()
            else:
                print(f"⚠️ Son non trouvé: {path} -> fallback silencieux")
                self.sounds[name] = DummySound()

        # Harmoniser noms utilisés par le reste du code
        self.sounds['range_shoot'] = self.sounds.get('fire_ball', DummySound())
        self.sounds['hit'] = self.sounds.get('armor', DummySound())
        self.sounds['block'] = self.sounds.get('armor', DummySound())

    def play_background_music(self):
        """Lance la musique de fond en boucle"""
        if os.path.exists(self.background_music_path):
            try:
                pygame.mixer.music.load(self.background_music_path)
                pygame.mixer.music.set_volume(0.3)
                pygame.mixer.music.play(-1)  # -1 = boucle infinie
                print("🎵 Musique de fond lancée!")
            except Exception as e:
                print("⚠️ Impossible de lire la musique de fond:", e)
        else:
            print("⚠️ Fichier musique de fond introuvable:", self.background_music_path)

    def play(self, sound_name):
        """Joue un son générique"""
        snd = self.sounds.get(sound_name)
        if snd:
            try:
                snd.play()
            except Exception:
                pass

    def play_melee(self):
        """Joue le son d'attaque mêlée (sword.wav)"""
        if 'melee_hit' in self.sounds:
            self.sounds['melee_hit'].play()
        if 'hit' in self.sounds:
            self.sounds['hit'].play()
        print("🔊 Son mêlée joué")

    def play_range(self):
        """Joue le son d'attaque à distance (fire_ball.wav)"""
        if 'range_shoot' in self.sounds:
            self.sounds['range_shoot'].play()
        print("🔊 Son range joué")