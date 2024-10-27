import os
from cfb_db import *

def menu():
    os.system('cls')
    print("CFB Player Database")
    print("-----------------------")
    print("1. View Players")
    print("2. Pitch Calculator")
    print("3. Ability Database")
    print("4. Export Data")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    return choice
    
def playerMenu():
    print("-"*70)
    print("1. Add Player  |  2. Update Player")
    print("3. Cut Player  |  4. Exit")
    
    choice = input("Enter your choice: ")
    return choice
