from player import Player
from engine.scene_engine import get_choice, narrate, speak
from scenes.chapter_1 import scene_03_2_shout_figure, scene_03_device, scene_03_1_corridor, scene_04_exit_station

def run_scene(player):
    narrate("You step into the mist, following the silhouette. Each footstep echoes less than the last, until their shape evaporates.")
    narrate("You're left alone. The world shakes as the ground fractures beneath your feet.")
    narrate("Step by step, the cracks grow wider, until you feel yourself falling...")
    narrate("Faster and faster—heart pounding, arms flailing—whispers brush past your ears...")

    if player.flags.get('discarded_ticket', False):
        speak("Whispers", "'Was your name not good enough?'")
        speak("Whispers", "'Or did you simply forget what it meant?'")

        narrate("You hit the floor with a thud!")
        narrate("Unharmed, you find yourself in a familiar corridor, but everything's shifted.")
        narrate("The air feels heavier and the space no longer seems endless.")
        narrate("In the distance, a device blinks faintly — a possible way out?")
        
        options = [
            "Approach the blinking device",
            "Explore the corridor cautiously"
        ]
        choice = get_choice(options)

        if choice == 0:
            player.update_stat("curiosity", 1)
            player.update_stat("insight", 1)
            player.flags["approach_blinking_device"] = True
            scene_03_device.run_scene(player)

        else:
            player.update_stat("curiosity", 1)
            player.flags["explore_corridor_s2"] = True
            scene_03_1_corridor.run_scene(player)

    else:
        speak("Whispers", f"'{player.name}... a name remembered. But is it *yours*?'")
        speak("Whispers", f"'{player.name}... {player.name}...'") 
        narrate("Then silence.")

        narrate("You land softly, the ground solid beneath you.")
        narrate("Around you stretches a misty expanse, endless and silent.")
        narrate("The figure's voice echoes faintly: 'Not all who follow find their way, but some truths wait in the dark.'")
        
        options = [
            "Call out to the figure",
            "Move forward into the mist"
        ]
        choice = get_choice(options)
        
        if choice == 0:
            player.update_stat("willpower", 1)
            player.flags["called_figure"] = True
            scene_03_2_shout_figure.run_scene(player)

        else:
            player.update_stat("corruption", 1)
            player.flags["stepped_into_mist"] = True
            scene_04_exit_station.run_scene(player)




'''
IDEAS

- 
'''
