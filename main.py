# External libraries
from pyuac import main_requires_admin

# Internal libraries
from utils import controller

@main_requires_admin
def main() -> None:
    controller_instance = controller.Controller()
    controller_instance.introduce()
    controller_instance.add_hotkeys()
    controller_instance.accept_game_loop()

if __name__ == "__main__":
    main()
