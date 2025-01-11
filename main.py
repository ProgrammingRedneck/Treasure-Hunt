import random
import os
import sys

# Game constants
GRID_SIZE = 5
TREASURE_COUNT = 1
TRAP_COUNT = 3

# Generate the game map
def generate_map():
    game_map = [["." for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    
    # Place treasure
    for _ in range(TREASURE_COUNT):
        x, y = random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1)
        game_map[x][y] = "T"

    # Place traps
    for _ in range(TRAP_COUNT):
        while True:
            x, y = random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1)
            if game_map[x][y] == ".":
                game_map[x][y] = "X"
                break

    # TODO Add loot and equipment.

    return game_map

# Display the game grid
def display_map(player_pos):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Treasure Hunt!")
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            if (x, y) == player_pos:
                sys.stdout.write("P ")
            else:
                sys.stdout.write(". ")
        sys.stdout.write("\n")

# Simulate user input for restricted environments
def get_move():
    predefined_moves = ["d", "d", "s", "s", "a", "w", "d"]  # Example sequence of moves
    if not hasattr(get_move, "index"):
        get_move.index = 0
    if get_move.index < len(predefined_moves):
        move = predefined_moves[get_move.index]
        get_move.index += 1
        print(f"Move (w/a/s/d): {move}")  # Simulate user seeing the move prompt
        return move
    return ""

# Main game logic
def main():
    game_map = generate_map()
    player_pos = (0, 0)
    
    while True:
        display_map(player_pos)

        # Player input
        move = get_move().lower()
        if move == "":
            print("No more moves available. Exiting game.")
            break

        x, y = player_pos

        if move == 'w' and x > 0:
            x -= 1
        elif move == 's' and x < GRID_SIZE - 1:
            x += 1
        elif move == 'a' and y > 0:
            y -= 1
        elif move == 'd' and y < GRID_SIZE - 1:
            y += 1
        else:
            print("Invalid move!")
            continue

        player_pos = (x, y)

        # Check game map at new position
        tile = game_map[x][y]
        if tile == "T":
            display_map(player_pos)
            print("Congratulations! You found the treasure!")
            break
        elif tile == "X":
            display_map(player_pos)
            print("Oh no! You fell into a trap. Game over!")
            break

if __name__ == "__main__":
    main()
