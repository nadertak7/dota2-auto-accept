import ctypes
import time
import keyboard
import pyautogui

class Controller:
    def __init__(self) -> None:
        """
        Initialise the Controller class.
        
        Attributes:
            - enable_script_state (bool): Flag to indicate if auto-accepter is toggled on/off.
            - close_script_state (bool): Flag to indicate if the auto-accepter should be running.
        """
        self.enable_script_state: bool = False
        self.close_script_state: bool = False

    def introduce(self):
        """Makes hotkeys visible to user."""
        print("Press F8 to Toggle Auto-Accept and F9 to Close")

    def script_state_prompt(self, enable_script_state: bool):
        """
        Informs user whether script is toggled on or off.

        Args:
            enable_script_state (bool): Current state of the script when the method is called.
        """
        if enable_script_state:
            print("Script Enabled")
        else:
            print("Script Disabled")

    def toggle_script(self) -> None:
        """Toggles the state of the script."""
        self.enable_script_state = not self.enable_script_state
        self.script_state_prompt(self.enable_script_state)

    def close_script(self) -> None:
        """Closes the script."""
        self.close_script_state = not self.close_script_state

    def add_hotkeys(self) -> None:
        """Adds hotkeys for toggling and closing the script."""
        keyboard.add_hotkey('f8', self.toggle_script)
        keyboard.add_hotkey('f9', self.close_script)

    def accept_game_loop(self) -> None:
        """Moves the mouse to the accept button if the script is enabled and not closed."""
        while not self.close_script_state:
            if self.enable_script_state and not self.close_script_state:
                center_res = (
                    ctypes.windll.user32.GetSystemMetrics(0)/2,
                    ctypes.windll.user32.GetSystemMetrics(1)/2
                )
                pyautogui.moveTo(center_res)
                pyautogui.click()
            time.sleep(5)
