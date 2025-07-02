from engine.scene_engine import get_choice, narrate, speak

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

        else:
            narrate("You explore the corridor, shadows stretching unnervingly along the walls.")
            # TODO: Lead to optional discovery or alternate path

    else:
        speak("Whispers", f"'{player.name}... a name remembered. But is it *yours*?'")
        speak("Whispers", f"'{player.name}... {player.name}...' Then silence.")

        narrate("You land softly, the ground solid beneath you.")
        narrate("Around you stretches a misty expanse, endless and silent.")
        narrate("The figure’s voice echoes faintly: 'Not all who follow find their way, but some truths wait in the dark.'")
        
        options = [
            "Call out to the figure",
            "Move forward into the mist"
        ]
        choice = get_choice(options)
        
        if choice == 0:
            narrate("Your voice cuts through the silence, but no answer comes.")
            # TODO: Seed callback opportunity in later scene?
        else:
            narrate("You step forward, letting the unknown pull you deeper.")
            # TODO: Continue player journey into next major beat



'''
IDEAS

- 
'''
