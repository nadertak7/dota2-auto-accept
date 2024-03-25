class userPrompt: 
    def __init__(self):
        pass
  
    def introduce(self):
        print("Press F8 to Toggle Auto-Accept and F9 to Close")

    def script_state_prompt(self, enable_script_state):
        if enable_script_state:
            print("Script Enabled")
        else:
            print("Script Disabled")
