def start_game():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a forest. There are paths to the left and right.")
    
    choice = input("Do you want to go left or right? ").strip().lower()
    
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    else:
        print("Invalid choice. The game ends.")
        
def left_path():
    print("You chose the left path and find a treasure chest.")
    print("Congratulations! You win!")
    
def right_path():
    print("You chose the right path and encounter a wild beast.")
    print("Unfortunately, you have to retreat. Game over.")

start_game()