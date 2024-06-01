from PIL import Image
import pyautogui

def take_screenshot_and_crop(top_left, top_right, bottom_left, bottom_right):
    """
    Takes a screenshot and returns the cropped content between the specified coordinates.

    Parameters:
    - top_left: tuple of (x, y) coordinates for the top left corner.
    - top_right: tuple of (x, y) coordinates for the top right corner.
    - bottom_left: tuple of (x, y) coordinates for the bottom left corner.
    - bottom_right: tuple of (x, y) coordinates for the bottom right corner.

    Returns:
    - cropped_image: PIL Image object of the cropped region.
    """
    # Take screenshot
    screenshot = pyautogui.screenshot()
    
    # Define the bounding box coordinates
    left = top_left[0]
    upper = top_left[1]
    right = top_right[0]
    lower = bottom_left[1]
    
    # Crop the screenshot
    cropped_image = screenshot.crop((left, upper, right, lower))
    
    return cropped_image


import pytesseract

# Set the Tesseract executable path if it's not in the PATH
# Set the Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\lcarp\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'  # Update this path if necessary


def recognize_poker_card_letter(cropped_image):
    """
    Recognizes and returns the poker card letter from the cropped image.

    Parameters:
    - cropped_image: PIL Image object of the cropped region.

    Returns:
    - card_letter: The recognized poker card letter as a string.
    """
    # Convert the image to grayscale
    gray_image = cropped_image.convert('L')
    
    # Use pytesseract to do OCR on the image
    card_letter = pytesseract.image_to_string(gray_image, config='--psm 8')
    
    # Clean up the output
    card_letter = card_letter.strip().upper()
    
    return card_letter

cropped_image = take_screenshot_and_crop([472, 381], [499, 383], [499, 417], [474, 417])
cropped_image.show()
card_letter = recognize_poker_card_letter(cropped_image)
print("Recognized Card Letter:", card_letter)