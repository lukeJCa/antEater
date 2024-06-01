import pyautogui

def take_screenshot_and_save():
    # Define the region starting from the top left of the screen
    x, y = 0, 0
    width, height = 1280, 960

    # Take a screenshot of the specified region
    screenshot = pyautogui.screenshot(region=(x, y, width, height))

    # Save the screenshot
    screenshot.save('screenshot_1280x960.png')
    print("Screenshot saved as 'screenshot_1280x960.png'")

# Example usage:
if __name__ == "__main__":
    take_screenshot_and_save()