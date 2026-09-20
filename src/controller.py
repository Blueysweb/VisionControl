import pyautogui

def perform_action(gesture):
    if gesture == "OPEN_PALM":
        print("Open Palm detected")
    
    if gesture == "FIST":
        print("Fist detected")
        
    if gesture == "PEACE":
        screenshot = pyautogui.screenshot()
        screenshot.save("screenshot.png")
        print("Screenshot taken!")
        