import pyautogui
import random
import time
import keyboard

def random_clicks():
    """
    Clicks randomly every 0.05 to 0.25 seconds until the space bar is pressed.
    """
    print("Press the space bar to stop...")

    while True:
        # Check if the space bar is pressed
        if keyboard.is_pressed('space'):
            print("Space bar pressed. Stopping...")
            break

        # Perform a click
        pyautogui.click()

        # Sleep for a random time between 0.05 and 0.25 seconds
        sleep_time = random.uniform(0.05, 0.25)
        time.sleep(sleep_time)

# Example usage:
if __name__ == "__main__":
    random_clicks()