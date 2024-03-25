import time
import keyboard
import ctypes #For get resolution of the screen
import pyautogui #To move your cursor in the middle of the screen 

class Controller:
    def __init__(self) -> None:
        self.enable_script_muteable = [False]
        self.close_script_muteable = [False]

    def introduce(self):
        print("Press F8 to Toggle Auto-Accept and F9 to Close")

    def script_state_prompt(self, enable_script_state):
        if enable_script_state:
            print("Script Enabled")
        else:
            print("Script Disabled")

    def invert_muteable(self, list_var) -> None:
        list_var[0] = not list_var[0]

    def toggle_script(self) -> None:
        self.invert_muteable(self.enable_script_muteable)
        self.script_state_prompt(self.enable_script_muteable[0])

    def close_script(self) -> None:
        self.invert_muteable(self.close_script_muteable)

    def add_hotkeys(self) -> None:
        keyboard.add_hotkey('f8', self.toggle_script)
        keyboard.add_hotkey('f9', self.close_script)

    def accept_game_loop(self) -> None:
        while not self.close_script_muteable[0]:
            while self.enable_script_muteable[0] and not self.close_script_muteable[0]:
                center_res = (
                    ctypes.windll.user32.GetSystemMetrics(0)/2,
                    ctypes.windll.user32.GetSystemMetrics(1)/2
                )
                pyautogui.moveTo(center_res)
                pyautogui.click()
                time.sleep(5)
