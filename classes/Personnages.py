# ===============================
# CLASSES
# ===============================

class Personnage:
    def __init__(self, nom, vie, attaque, defense, mana_max):
        self.nom = nom
        self.vie = vie
        self.vie_max = vie
        self.attaque = attaque
        self.defense = defense
        self.defense_max = 50
        self.mana_max = mana_max
        self.mana = mana_max

    def attaquer_base(self, cible):
        cout = 7
        if self.mana >= cout:
            degats_effectifs = max(1, self.attaque - cible.defense // 2)
            cible.vie -= degats_effectifs
            self.mana -= cout
            print(f"⚔️  {self.nom} utilise Attaque de base sur {cible.nom} ({degats_effectifs} dégâts, -{cout} mana)")
        else:
            print(f"❌ {self.nom} n'a pas assez de mana pour l'attaque de base !")

    def attaquer_special(self, cible):
        cout = 15
        if self.mana >= cout:
            degats_effectifs = max(1, self.attaque + 10 - cible.defense // 3)
            cible.vie -= degats_effectifs
            self.mana -= cout
            print(f"🔥 {self.nom} utilise Attaque spéciale sur {cible.nom} ({degats_effectifs} dégâts, -{cout} mana)")
        else:
            print(f"❌ {self.nom} n'a pas assez de mana pour l'attaque spéciale !")

    def bouclier(self):
        cout = 13
        if self.mana >= cout:
            self.defense = min(self.defense + 10, self.defense_max)
            self.mana -= cout
            print(f"🛡️  {self.nom} utilise Bouclier (+10 défense, -{cout} mana)")
        else:
            print(f"❌ {self.nom} n'a pas assez de mana pour le bouclier !")

    def regen_mana(self):
        self.mana = min(self.mana + 10, self.mana_max)

    def statut(self):
        vie_emoji = "❤️" * (self.vie * 10 // self.vie_max) or "💀"
        mana_emoji = "🔵" * (self.mana * 10 // self.mana_max) or "⚪"
        print(f"{self.nom} | Vie: {self.vie}/{self.vie_max} {vie_emoji} | Mana: {self.mana}/{self.mana_max} {mana_emoji} | Atk: {self.attaque} | Def: {self.defense}")


# ===============================
# CLASSES ENFANTS
# ===============================

class Guerrier(Personnage):
    def __init__(self, nom):
        super().__init__(nom, vie=100, attaque=15, defense=5, mana_max=50)

class Mage(Personnage):
    def __init__(self, nom):
        super().__init__(nom, vie=80, attaque=20, defense=3, mana_max=60)
