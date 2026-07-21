import json

def save_game_data(game_data, output_path):
    with open(output_path, "w") as file:
        json.dump(game_data, file, indent=4)

    print(f"Saved game data to: {output_path}")