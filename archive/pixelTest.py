import pyautogui
import time

def get_pixel_rgb(x, y):
    # Capture the screen at the specified coordinates
    screenshot = pyautogui.screenshot(region=(x, y, 1, 1))

    # Get the RGB values of the pixel
    pixel_rgb = screenshot.getpixel((0, 0))

    return pixel_rgb

if __name__ == "__main__":
    # Test coordinates
    x, y = 1, 1

    try:
        while True:
            # Get the RGB values of the pixel at (100, 100)
            rgb = get_pixel_rgb(x, y)
            print(f"RGB values at ({x}, {y}): {rgb}")

            # Sleep for a short duration to avoid excessive CPU usage
            time.sleep(0.1)  # Adjust the sleep time as needed

    except KeyboardInterrupt:
        print("Stopped by user")