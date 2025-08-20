class Enemy:
    def __init__(self, name, description, health):
        self.name = name
        self.description = description
        self.health = health
        self.damage = 5 # Default damage

    def describe(self):
        print(f"A fearsome {self.name} is here!")
        print(self.description)

    def attack(self, player):
        player.health -= self.damage
        print(f"The {self.name} attacks you for {self.damage} damage!")

# A specific enemy that inherits from the base class
class Goblin(Enemy):
    def __init__(self):
        super().__init__(
            name="Goblin",
            description="A small, wiry creature with sharp teeth.",
            health=20
        )