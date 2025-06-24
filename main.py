from player import player
from scenes.chapter_1 import scene_01_intro, scene_02_follow_figure

def main():
    scene_01_intro.run_scene(player)
    scene_02_follow_figure.run_scene(player)

if __name__=="__main__":
    main()