import importlib

def run_scene(scene_path, player):
    try:
        module = importlib.import_module(scene_path)
        module.run_scene(player)
    except ModuleNotFoundError:
        print(f"[ERROR] Scene '{scene_path}' could not be found.")
    except AttributeError:
        print(f"[ERROR] Scene '{scene_path}' does not contain a 'run_scene(player)' function")
    