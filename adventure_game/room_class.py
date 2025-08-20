from player_class import Player
from item_class import Item
from enemy_class import Enemy, Goblin

class Room:
    def __init__(self, name, description):
        # ... (other attributes are the same)
        self.name = name
        self.description = description
        self.linked_rooms = {}
        self.items = []
        self.character = None # NEW: To hold an Enemy

    def get_details(self):
        # ... (this method is updated)
        print(f"--- {self.name} ---")
        print(self.description)

        if self.character: # NEW: Describe the character if one is present
            self.character.describe()

        if self.items:
            print("You see:")
            for item in self.items:
                print(f"- {item.name}")
        for direction, room in self.linked_rooms.items():
            print(f"To the {direction} is the {room.name}.")

    def link_room(self, room_to_link, direction):
        """Creates a two-way link between this room and another."""
        self.linked_rooms[direction] = room_to_link
        # Automatically create the reverse link
        opposite_direction = {"north": "south", "south": "north", "east": "west", "west": "east"}
        room_to_link.linked_rooms[opposite_direction[direction]] = self

    def move(self, direction):
        """Returns the room object in a given direction, or None."""
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            return None
        





# [All class definitions go here: Item, Enemy, Goblin, Player, Room]

# --- Setup ---
kitchen = Room("Kitchen", "A dimly lit kitchen.")
dining_hall = Room("Dining Hall", "A grand hall.")
garden = Room("Garden", "An overgrown garden.")
sword = Item("sword", "A rusty but sharp sword.")
kitchen.items.append(sword)

dining_hall.link_room(kitchen, "south")
dining_hall.link_room(garden, "east")

# Place an enemy in the garden
garden.character = Goblin()

player = Player("Adventurer", dining_hall)
game_over = False

commands = ["north", "south", "east", "west", "fight", "pick <item_name>", "inventory", "quit"]

# --- Game Loop ---
while not game_over:
    print("\n")
    player.current_room.get_details()

    print("\nAvailable commands:" + ",".join(commands))
    command = input("> ").lower()

    if player.current_room.character and command == "fight":
        enemy = player.current_room.character
        # Combat Loop
        while player.health > 0 and enemy.health > 0:
            player.attack(enemy)
            if enemy.health <= 0:
                print(f"You defeated the {enemy.name}!")
                player.current_room.character = None # Enemy is gone
                break
            enemy.attack(player)
            if player.health <= 0:
                print("You were defeated... Game Over.")
                game_over = True
                break
            print(f"Your health: {player.health} | {enemy.name}'s health: {enemy.health}")

    elif command in ["north", "south", "east", "west"]:
        # (movement logic is the same)
        next_room = player.current_room.move(command)
        if next_room:
            player.current_room = next_room
        else:
            print("You can't go that way.")

    # ... (get, inventory, and quit logic are the same)
    elif command.startswith("pick"):
        item_name = command.split(" ")[1]
        if item_name not in player.inventory:
            player.inventory.append(item_name)
            print(f"\n\n -------You picked up the {item_name}------")
        else:
            print(f"\n\n -------You already have the {item_name}.-------")

    elif command == "inventory":
        print("\n\n -------You are carrying-------")
        player.get_inventory_items()

    elif command == "quit":
        print("Thanks for playing!")
        break
    else:
        print("I don't understand that command.")