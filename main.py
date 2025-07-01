from player import Player
from engine.scene_loader import run_scene

def main():
    player = Player(name="")
    run_scene("scenes.chapter_1.scene_01_intro", player)

if __name__=="__main__":
    main()