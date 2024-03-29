import time
import keyboard
import ctypes
import pyautogui

class Controller:
    def __init__(self) -> None:
        self.enable_script_state = False
        self.close_script_state = False

    def introduce(self):
        print("Press F8 to Toggle Auto-Accept and F9 to Close")

    def script_state_prompt(self, enable_script_state):
        if enable_script_state:
            print("Script Enabled")
        else:
            print("Script Disabled")

    def toggle_script(self) -> None:
        self.enable_script_state = not self.enable_script_state
        self.script_state_prompt(self.enable_script_state)

    def close_script(self) -> None:
        self.close_script_state = not self.close_script_state

    def add_hotkeys(self) -> None:
        keyboard.add_hotkey('f8', self.toggle_script)
        keyboard.add_hotkey('f9', self.close_script)

    def accept_game_loop(self) -> None:
        while not self.close_script_state:
            if self.enable_script_state and not self.close_script_state:
                center_res = (
                    ctypes.windll.user32.GetSystemMetrics(0)/2,
                    ctypes.windll.user32.GetSystemMetrics(1)/2
                )
                pyautogui.moveTo(center_res)
                pyautogui.click()
                time.sleep(5)
