import json
import csv
import os

def save_player_json(player):
    file_path = "saved_players.json"
    # Load existing data if file exists, else start with an empty list
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            removed_players = json.load(file)
    else:
        removed_players = []
    
    # Add removed player to list    
    removed_players.append(player)
    
    # Write updated list back to file
    with open(file_path, 'w') as file:
        json.dump(removed_players, file, indent=4, default=str)
        
        
def save_player_csv(player):
    file_path = "saved_players.csv"
    file_exists = os.path.exists(file_path)
    
    with open(file_path, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=player.keys())
        
        # Write header omly if file does not exist
        if not file_exists:
            writer.writeheader()
            
        # Write the player data
        writer.writerow(player)
    
