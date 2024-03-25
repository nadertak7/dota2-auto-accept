# External libraries
from pyuac import main_requires_admin

# Internal libraries
from utils import scriptmanager

@main_requires_admin
def main() -> None:
    controller = scriptmanager.scriptManager()

    controller.introduce()

    controller.add_hotkeys()

    controller.accept_game_loop()

if __name__ == "__main__":
    main()
