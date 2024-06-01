import pyautogui

# Define a dictionary of color names and their corresponding RGB values
COLOR_NAMES = {
    "Black": (0, 0, 0),
    "White": (255, 255, 255),
    "Red": (255, 0, 0),
    "Lime": (0, 255, 0),
    "Blue": (0, 0, 255),
    "Yellow": (255, 255, 0),
    "Cyan": (0, 255, 255),
    "Magenta": (255, 0, 255),
    "Silver": (192, 192, 192),
    "Gray": (128, 128, 128),
    "Maroon": (128, 0, 0),
    "Olive": (128, 128, 0),
    "Green": (0, 128, 0),
    "Purple": (128, 0, 128),
    "Teal": (0, 128, 128),
    "Navy": (0, 0, 128),
    # Add more colors if necessary
}

def get_color_name(rgb_tuple):
    # Find the closest matching color name by calculating the Euclidean distance
    min_distance = float('inf')
    closest_color_name = None
    for color_name, color_rgb in COLOR_NAMES.items():
        distance = sum((rgb_tuple[i] - color_rgb[i]) ** 2 for i in range(3))
        if distance < min_distance:
            min_distance = distance
            closest_color_name = color_name
    return closest_color_name

def get_color_at_point(x, y):
    # Get the RGB values at the specified coordinates
    screenshot = pyautogui.screenshot()
    rgb = screenshot.getpixel((x, y))
    # Determine the color name
    color_name = get_color_name(rgb)
    return rgb, color_name

# Example usage:
if __name__ == "__main__":
    x, y = 474, 584  # Replace with desired coordinates
    rgb, color_name = get_color_at_point(x, y)
    print(f"RGB values at ({x}, {y}): {rgb}")
    print(f"Color name: {color_name}")