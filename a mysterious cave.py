import sys
import time

def print_slow(text):
    """A function to print with a delay for a retro feel"""
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    print()

def start_game():
    print_slow("welcome to the mysterious cave!")
    print_slow("You are an explorer who stumbled upon a dark cave entrance")
    print_slow("your goal is to find the treasure and come out alive")
    print("-" * 40)
    cave_entrance()

def game_over(reason):
    print("-" * 40)
    print_slow(f"Game Over. {reason}")
    print_slow("thanks for playing!")
    sys.exit()

def cave_entrance():
    print_slow("you are at the cave entrance.it is dark and spooky")
    print_slow("Do you want to [enter] or [leave]?")

    choice = input("> ").strip().lower()

    if choice == "enter":
        dark_room()
    elif choice == "leave":
        game_over("YOu decided not to be adventurous and went home")
    else:
        print_slow("Invalid command. Please enter 'enter' or 'leave'.")
        cave_entrance()

def dark_room():
    print_slow("-" * 40)
    print_slow("you enter the dark room. you see two tunnels ahead: a [left] tunnel and a [right] tunnel.")
    print_slow("There is also a strange [glowing] object in the corner.")

    choice = input("> ").strip().lower()
     
    if choice == "left":
        trap_room()
    elif choice == "right":
        treasure_room()
    elif choice == "glowing":
        print_slow("you investigate the object. It's just a glowing moss, nothing useful")
        dark_room()#stay in the same room after checking
    else:
        print_slow("Invalid command. Please enter 'left', 'right' or 'glowing'")
        dark_room()

def trap_room():
    print_slow("-" * 40)
    print_slow("You walk into the left tunnel and suddenly fall into a hidden pit trap!")
    game_over("You couldn't climb out of the pit.")
    
def treasure_room():
    print_slow("-" * 40)
    print_slow("You enter the right tunnel and see a large chest full of riches and jewels!")
    print_slow("Do you want to [take] it or [leave] it?")

    choice = input("> ").strip().lower()
    
    if choice == "take":
        print_slow("You take the treasure and you become rich and live a happy life")
        print_slow("Congratulations, you win the game!")
    elif choice == "leave":
        game_over("you left the treasure and wandered until you were lost.")
    else:
        print_slow("Invalid command. Please enter 'take' or 'leave'")
        treasure_room()

#start the game
if __name__ == "__main__":
    start_game()