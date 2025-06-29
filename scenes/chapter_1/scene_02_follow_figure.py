from player import player
from engine.scene_engine import get_choice, narrate, speak

from player import player
from engine.scene_engine import get_choice, narrate, speak

# Entry point for this atmospheric scene: a pivotal descent following The Figure
def run_scene(player):
    # Initial descent sequence—sets tone and physical/surreal shift
    narrate("You step into the mist, following the silhouette. Each footstep echoes less than the last, until their shape evaporates.")
    narrate("You're left alone. The world shakes as the ground fractures beneath your feet.")
    narrate("Step by step, the cracks grow wider, until you feel yourself falling...")
    narrate("Faster and faster—heart pounding, arms flailing—whispers brush past your ears...")

    # Branch logic based on whether the player discarded their ticket earlier
    if player['flags'].get('discarded_ticket', False):
        # Whispers tie directly to a past choice—haunting, personalized consequence
        speak("Whispers", "'Was your name not good enough?'")
        speak("Whispers", "'Or did you simply forget what it meant?'")

        # Post-fall environment setup—altered familiar space
        narrate("You hit the floor with a thud!")
        narrate("Unharmed, you find yourself in a familiar corridor, but everything's shifted.")
        narrate("The air feels heavier and the space no longer seems endless.")
        narrate("In the distance, a device blinks faintly — a possible way out?")
        
        # Player presented with a contextual choice
        options = [
            "Approach the blinking device",
            "Explore the corridor cautiously"
        ]
        choice = get_choice(options)

        if choice == 0:
            narrate("You move toward the device, your heart pounding with cautious hope.")
            # TODO: Trigger device interaction or next narrative node
        else:
            narrate("You explore the corridor, shadows stretching unnervingly along the walls.")
            # TODO: Lead to optional discovery or alternate path

    else:
        # Variant whisper for players who kept their name—still unsettling
        speak("Whispers", f"'{player['name']}... a name remembered. But is it *yours*?'")
        speak("Whispers", f"'{player['name']}... {player['name']}...' Then silence.")

        # Softer landing sequence for this branch
        narrate("You land softly, the ground solid beneath you.")
        narrate("Around you stretches a misty expanse, endless and silent.")
        narrate("The figure’s voice echoes faintly: 'Not all who follow find their way, but some truths wait in the dark.'")
        
        # Alternate choices reinforcing introspection and direction
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
