from player import player
from main import narrate, speak


def main():
    narrate("You wake as the train pulls to a heavy stop." \
    "\nYou step off the train, mist rolling over a desolate platform." \
    "\nYou step outside and all you can see is a figure holding a sign in the distance.")

    player["name"] = input("It reads: What is your name? ")

    speak("The Figure", f"The mysterious figure looks you up and down. Ahhh yes, {player["name"]}, that sounds about right.")
    narrate("They lower the sign and step back, eyes painting a blank picture")
    speak("The Figure", "You returned for a reason. Though I wonder if it's the same one that sent you away...")
    narrate("They turn away and walk into the fog")

    input("\n[Press Enter to follow them into the fog...]")
