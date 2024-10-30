import os
from cfb_db import *

# Main Menu for Program Startup
def menu():
    os.system('cls')
    print("CFB Player Database")
    print("-----------------------")
    print("1. View Players")
    print("2. Update Player (Stats)")
    print("3. Pitch Calculator (N/I)")
    print("4. Ability Database (N/I)")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    return choice
    
# Menu for View Player
def playerMenu():
    print("-"*70)
    print("1. Add Player   |   2. Cut Player")
    print("3. Change VIew  |   4. Exit")
    
    choice = input("Enter your choice: ")
    return choice

# TODO: Menu for Updating players
def updateMenu():
    
    choice = input("Enter a Menu Option: ")
    return choice

# TODO: Menu for different Views
def viewMenu():
    
    choice = input("Enter a Menu Option: ")
    return choice
