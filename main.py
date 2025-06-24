from player import player
from scenes.chapter_1 import intro, follow_figure

def main():
    intro.run_scene(player)
    follow_figure.run_scene(player)

if __name__=="__main__":
    main()