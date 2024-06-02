from PIL import ImageGrab
import pyautogui
import webcolors

def round_color_to_closest(rgb_tuple):
    """
    Round an RGB tuple to the closest of white, black, or red.
    
    :param rgb_tuple: Tuple containing (r, g, b) values.
    :return: The name of the closest color (white, black, or red).
    """
    # Define the RGB values for white, black, and red
    colors = {
        "white": (255, 255, 255),
        "black": (0, 0, 0),
        "red": (255, 0, 0)
    }
    
    # Calculate the Euclidean distance to each color
    distances = {color: ((rgb_tuple[0] - rgb[0]) ** 2 + (rgb_tuple[1] - rgb[1]) ** 2 + (rgb_tuple[2] - rgb[2]) ** 2) for color, rgb in colors.items()}
    
    # Return the color with the smallest distance
    return min(distances, key=distances.get)


def get_color_names_at_coordinates(img,coordinates):
    """
    Get the color names at specified coordinates in an image.
    
    :param image_path: Path to the image file.
    :param coordinates: List of tuples containing (x, y) coordinates.
    :return: List of color names at the specified coordinates.
    """
    # Take a screenshot
    screenshot = pyautogui.screenshot()
    
    # Convert image to RGB (in case it is in another mode like RGBA, L, etc.)
    img = screenshot.convert('RGB')
    
    rounded_colors = []
    for x, y in coordinates:
        # Get the RGB color at the specified coordinates
        rgb_color = img.getpixel((x, y))
        # Round the color to the closest of white, black, or red
        rounded_color = round_color_to_closest(rgb_color)
        rounded_colors.append(rounded_color)
    
    return rounded_colors


def classify_color(rgb):
    r, g, b = rgb
    if r < 50 and g < 50 and b < 50:
        return "black"
    elif r > 200 and g > 200 and b > 200:
        return "white"
    elif abs(r - g) < 30 and abs(r - b) < 30 and abs(g - b) < 30:
        return "grey"
    elif r > 200 and g > 200 and b < 50:
        return "yellow"
    elif r > 200 and g < 50 and b < 50:
        return "red"
    elif r < 50 and g < 50 and b > 200:
        return "blue"
    elif r < 50 and g > 200 and b < 50:
        return "green"
    else:
        return None



def most_prominent_color(img, coordinates):
    rgb_list = []
    for x, y in coordinates:
        # Get the RGB color at the specified coordinates
        rgb_color = img.getpixel((x, y))
        rgb_list.append(rgb_color)

    color_counts = {
        "black": 0,
        "grey": 0,
        "white": 0,
        "yellow": 0,
        "red": 0,
        "blue": 0,
        "green": 0
    }
    
    for rgb in rgb_list:
        color = classify_color(rgb)
        if color:
            color_counts[color] += 1
    
    most_prominent = max(color_counts, key=color_counts.get)
    return most_prominent

# Example usage
#rgb_list = [(255, 0, 0), (0, 0, 255), (200, 200, 200), (50, 50, 50), (255, 255, 0)]
#print(most_prominent_color(rgb_list))  # Output: red