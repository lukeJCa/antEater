from PIL import ImageGrab, ImageDraw
import pyautogui
import loadPoints

def draw_points_on_screenshot(coords, output_path='screenshot_with_points.png'):
    """
    Takes a screenshot and draws points at the given coordinates.

    Args:
    coords (list of tuples): List of (x, y) tuples representing the coordinates to draw.
    output_path (str): Path to save the modified screenshot.

    Returns:
    None
    """
    # Take a screenshot
    screenshot = pyautogui.screenshot()
    
    # Convert the screenshot to a format that allows drawing
    screenshot = screenshot.convert('RGB')
    
    # Create a drawing object
    draw = ImageDraw.Draw(screenshot)
    
    # Draw points at each coordinate
    for coord in coords:
        draw.ellipse((coord[0] - 5, coord[1] - 5, coord[0] + 5, coord[1] + 5), fill='red', outline='red')

    # Save the modified screenshot
    screenshot.save(output_path)
