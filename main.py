from player import player
from engine.scene_loader import run_scene

def main():
    run_scene("scenes.chapter_1.scene_01_intro", player)
    run_scene("scenes.chapter_1.scene_02_follow_figure", player)
    run_scene("scenes.chapter_1.scene_02_5_explore", player)

if __name__=="__main__":
    main()