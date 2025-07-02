from player import Player
from engine.scene_engine import get_choice, narrate, speak

def run_scene(player):
    if choice == 0:
        narrate("You move toward the device, your heart pounding with cautious hope.")
        # TODO: Trigger device interaction or next narrative node
        narrate("The screen comes alive, flickering words across the screen")
        speak("Blinking Device", "What is your name?")

        options = [
            "Try and enter your name",
            "Try random combinations",
            "Walk away from the device" 
            ]

        choice = get_choice(options)
        # TODO: Flesh out choice by adding stats, flags, and moving the story on
        if choice == 0:
            speak("The Device", "Name not recognised, did you really think throwing it away was a good idea?")
        elif choice == 1:
            speak("The Device", "Failed to follow simple instructions... Powering Down")
        else:
            narrate("You walk away from the device, feeling a strange sense of relief running over you")
