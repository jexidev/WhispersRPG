from player import Player
from engine.scene_engine import get_choice, narrate, speak
from scenes.chapter_1 import scene_02_follow_figure, scene_02_5_explore


def run_scene(player):
    narrate("The train screeches to a halt. You jolt awake, heart pounding.")
    narrate("Your hand is wrapped tightly around something - a ticket, damp with sweat.")

    # Discard the ticket or not
    options = ["Throw the ticket away - the journey is over anyway",
               "Examine the ticket"]
    
    choice = get_choice(options)

    if choice == 0:
        narrate("You drop the ticket onto the carriage floor and stand. Whatever it once meant, it's behind you now.")
        player.flags['discarded_ticket'] = True
        player.name = "..."  # Placeholder or symbolic nothingness
        player.update_stat("identity_stability", -1)
    else:
        player.name = input("Your eyes come into focus and you make out a name.\nIt reads: ")
        player.flags['discarded_ticket'] = False
        player.update_stat("insight", 1)

    narrate("You don't remember boarding, but the name feels... familiar, like a whisper in a dream.\nYou step off the train into thick, gray mist.")
    narrate("The platform is empty - all but a single figure, still as stone, standing in the fog ahead.")

    input("\n[Press Enter to approach the figure...]")

    if player.name == "...":
        speak("The Figure", "... Interesting. I see you decided to leave your name behind. How curious.")
    else:
        speak("The Figure", f"... So you *are* still carrying that name. {player.name}. How curious.")

    narrate("They lower their gaze, as if they've seen you before - but not quite like this.")
    speak("The Figure", "Names cling harder than memories, I suppose.")
    narrate("The figure turns away from you and glides into the fog.")
    
    options = [
        "Follow the figure into the fog",
        "Stay and look around the platform"
    ]
    choice = get_choice(options)

    if choice == 0:
        player.update_stat("identity_stability", -1)
        scene_02_follow_figure.run_scene(player)
    else:
        player.update_stat("curiosity", 1)
        scene_02_5_explore.run_scene(player)
