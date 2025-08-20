
class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room
        self.inventory = []
        self.health = 50 # NEW: Player has health
        self.damage = 10 # NEW: Player can do damage

    def attack(self, enemy):
        enemy.health -= self.damage
        print(f"You attack the {enemy.name} for {self.damage} damage!")

    def get_inventory_items(self):
        for item in self.inventory:
            print(item)