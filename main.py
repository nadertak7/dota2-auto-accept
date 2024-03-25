# External libraries
import keyboard
import mouse
from pyuac import main_requires_admin
import time

# Internal libraries
from utils import userprompt

@main_requires_admin
def main() -> None:

    # Initialise variables
    enable_script_muteable = [False]
    close_script_muteable = [False]
    user_prompt = userprompt.userPrompt()

    def invert_muteable(list_var):
        list_var[0] = not list_var[0]

    def toggle_script() -> None:
        invert_muteable(enable_script_muteable)
        user_prompt.script_state_prompt(enable_script_muteable[0])

    def close_script() -> None:
        invert_muteable(close_script_muteable)

    def accept_game() -> None:
        mouse.move(x="1000", y="520")
        mouse.click()

    user_prompt.introduce()

    keyboard.add_hotkey('f8', toggle_script)
    keyboard.add_hotkey('f9', close_script)

    while not close_script_muteable[0]:
        while enable_script_muteable[0] and not close_script_muteable[0]:
            accept_game()
            time.sleep(5)

if __name__ == "__main__":
    main()
