# Used inside scenes to hihglight narration
def narrate(text):
    print(f"\n{text}")

# Used inside scenes to separate speach lines.
def speak(name, text):
    print(f'\n{name}: "{text}"')

# Presents a list of options to the player  
def get_choice(options):
    print("\nWhat will you do?\n")
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    while True:
        choice = input("\nChoose an option: ")
        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(options):
                return index
        print("Invalid choice. Please enter the number of your selection.")