from player import player
from main import narrate, speak


def main():
    narrate("The train screeches to a halt. You jolt awake, heart pounding.")
    narrate("Your hand is wrapped tightly around something - a ticket, damp with sweat.")

    player["name"] = input("Your eyes come into focus and you make out a name.\
                           \nIt reads: ")
    
    narrate("You don't remember boarding, but the name feels... familiar, like a whisper in a dream.\
            \n\nYou step off the train into thick, gray mist.")
    narrate("The platform is empty - all but a single figure, still as stone, standing in the fog ahead.")

    input("\n[Press Enter to approach the figure...]")

    speak("The Figure", f"... So you *are* still carrying that name. {player["name"]}. How curious.")
    narrate("They lower their gaze, as if they've seen you before - but not quite like this.")
    speak("The Figure", "Names cling harder than memories, I suppose.")
