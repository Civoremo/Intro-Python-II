from humanoid import Humanoid

class Monster(Humanoid):
    def __init__(self, name, weapon, health=5):
        self.weapon = weapon
        super().__init__(name, health)

    def __repr__(self):
        return f'{self.name}-{self.weapon.name} AP:{self.weapon.attack_points}'