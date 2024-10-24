from pymongo import MongoClient
import os
#from dbmenu import *

uri = "mongodb+srv://joshmcd:Lilmac11@osu-dynasty.x7hhy.mongodb.net/?retryWrites=true&w=majority&appName=OSU-Dynasty"
client = MongoClient(uri)
# coll name needs to be updated for each team
# CFB25 and OSU_Players(test)
db = client.CFB25
# KentSt or OSU and CFB25(test)
coll = db.OSU

# add_player() - Function to add new player
def add_player():
    while True:
        os.system('cls')
        name = input("Enter player name: ")
        pos = input("Enter player position: ")
        tend = input("Enter player archetype: ")
        home = input("Enter player's Hometown (city, st): ")
        height = input("Enter player's height (ft'in): ")
        weight = input("Enter player's weight: ")
        dev = input("Enter player Development type: ")
        cla = input("Enter player's Classification: ")
    
        player = {
            'Name': name,
            'Position': pos,
            'Tendency': tend,
            'Hometown': home,
            'Height': height,
            'Weight': weight,
            'Development': dev,
            'Class': cla,
            'Ratings': {},
            'Stats': {},
            'Accolades': {},
            'Abilites': {}
        }
    
        coll.insert_one(player)
        print(f"Player {name} added successfully.")
        
        another = input("Would you like to add another player to this team? (y/n): ").strip().lower()
        if another != 'y':
            break
    
# Function to view all players
def view_players():
    # Get all players: Name, Postiion, Tendency, Development, and Current Class
    players = coll.find({}, {'Name': 1, 'Position': 1, 'Tendency': 1, 'Development': 1, 'Class': 1})
    
    # Minimum column widths
    min_name = 15
    min_pos = 10
    min_tend = 12
    min_dev = 12
    min_class = 10
    
    # initialize column widths
    name_width = max(len('Name'), min_name)
    pos_width = max(len('Position'), min_pos)
    tend_width = max(len('Tendency'), min_tend)
    dev_width = max(len('Development'), min_dev)
    cla_width = max(len('Class'), min_class)
    
    # Determin max width of each field by the data
    for player in players:
        name_width = max(name_width, len(player.get('Name', 'N/A')))
        pos_width = max(pos_width, len(player.get('Position', 'N/A')))
        tend_width = max(tend_width, len(player.get('Tendency', 'N/A')))
        dev_width = max(dev_width, len(player.get('Development', 'N/A')))
        cla_width = max(cla_width, len(player.get('Class', 'N/A')))
    
    # Print header column names
    print(f"{'Name'.ljust(name_width)} {'Position'.ljust(pos_width)} {'Tendency'.ljust(tend_width)} {'Development'.ljust(dev_width)} {'Class'.ljust(cla_width)}")
    print('-' * (name_width + pos_width + tend_width + dev_width + cla_width))
    
    # Get all players: Name, Postiion, Tendency, Development, and Current Class
    players = coll.find({}, {'Name': 1, 'Position': 1, 'Tendency': 1, 'Development': 1, 'Class': 1})
    
    # Print each player's details, aligned
    for player in players:
        name = player.get('Name', 'N/A').ljust(name_width)
        pos = player.get('Position', 'N/A').ljust(pos_width)
        tend = player.get('Tendency', 'N/A').ljust(tend_width)
        dev = player.get('Development', 'N/A').ljust(dev_width)
        cla = player.get('Class', 'N/A').ljust(cla_width)
        
        print(f"{name} {pos} {tend} {dev} {cla}")
        
    choice = input("\nDo you want to enter a player? (yes/no): ").lower()
    
    if choice == 'yes':
        add_player()

# Function to add/update stats to a player
def update_stats():
    name = input("Enter the player who's stats you want to update: ")
    year = input("Enter the year (e.g., 2024): ")
    
    while True:
        category = input("Enter the stat category: ")
        stat = input(f"Enter the stat value for {category}: ")
        
        coll.update_one(
            {'Name': name},
            {'$set': {f'Stats.{year}.{category}': int(stat)}}
        )
        print(f"Updated {category} for {name} in {year} to {stat}.")
        
        repeat = input("Do you want to add another stat for this player and year?: ").strip().lower()
        if repeat != 'y':
            break

# TODO: Function to add/update abilities for player
def update_abilites():
    name = input("Enter the player who's abilites you want to update: ")
    year = input("Enter the year (e.g., 2024): ")
    
    while True:
        ability = input("Enter the ability to upgrade: ")
        
        # update database with new ability
        
        repeat = input("Would you like to update another ability?: ").strip().lower()
        if repeat != 'y':
            break

# TODO: Function to add/update ratings for player

# TODO: Function to add/update accolades for player

# Function to delete a player from the database
def remove_player():
    # Get all players
    players = list(coll.find({}, {'Name': 1, 'Position': 1, 'Tendency': 1, 'Development': 1, 'Class': 1}))
    
    # Display players
    if players:
        for idx, player in enumerate(players, start=1):
            print(f"{idx}. {player.get('Name', 'N/A')} | {player.get('Position', 'N/A')} | {player.get('Development', 'N/A')}")
            
        try:
            # Prompt User to select a player to remove by index
            player_index = int(input(f"\nSelect a player to remove by number (1-{len(players)}): ")) - 1
            if 0 <= player_index < len(players):
                selected_player = players[player_index]
                player_name = selected_player.get('Name', 'N/A')
                
                # Get confirmation for deletetion
                confirm = input(f"Are you sure you want to remove {player_name}? (yes/no): ").lower()
                if confirm == 'yes':
                    # Code to remove entry from MongoDB
                    coll.delete_one({'_id': selected_player['_id']})
                    print(f"{player_name} has been cut from the team.")
                else:
                    print("Cut operation cancelled. (enter 'yes' to cut a player)")
            else:
                print("Invalid player index. (Enter the number next to the player you want to cut)")
        except ValueError:
            print("Invalid input. Please enter a number")
    else:
        print("No players found in the database.")
                
# TODO: Function to update all players class

# TODO: Function to view stats for a specific player
# TODO: Function to view abilites for a specific player
# TODO: Function to view accolades for a specifc player
# TODO: Function to view ratings for a specific player

def menu():
    print("CFB Recruiting Database")
    print("-----------------------")
    print("1. Add Player")
    print("2. Update Stats")
    print("3. View Players")
    print("4. Delete Player")
    print("5. Exit")
    
    choice = input("Enter your Choice: ")
    return choice

def main():
    while True:
        choice = menu()
                
        if choice == '1':
            add_player()
        elif choice == '2':
            update_stats()
        elif choice == '3':
            view_players()          
        elif choice == '4':
            remove_player()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
    
client.close()
