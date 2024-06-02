import pytesseract
from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import pyautogui

# Set the Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\lcarp\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'  # Update this path if necessary

def preprocess_image(image):
    # Convert image to grayscale
    grayscale_image = image.convert("L")
    # Enhance the contrast
    enhancer = ImageEnhance.Contrast(grayscale_image)
    enhanced_image = enhancer.enhance(2)
    # Convert to binary (black and white)
    binary_image = enhanced_image.point(lambda x: 0 if x < 128 else 255, '1')
    return binary_image

def get_card_value_from_box(top_left, bottom_right, top_right, bottom_left):
    # Capture the region defined by the top left and bottom right coordinates
    x1, y1 = top_left
    x2, y2 = bottom_right
    width = x2 - x1
    height = y2 - y1

    if top_right == None and bottom_left == None:
        screenshot = pyautogui.screenshot(region=(x1, y1, width, height))
    else:
        screenshot = pyautogui.screenshot(region=(x1, y1, width, height))
    
    # Preprocess the image to improve OCR accuracy
    processed_image = preprocess_image(screenshot)
    
    # Use Tesseract to do OCR on the captured image
    card_text = pytesseract.image_to_string(processed_image, config='--psm 6')
    print(card_text)
    # Filter out only valid poker card values
    valid_values = {'2', '3', '4', '5', '6', '7', '8', '9', '10', 'A', 'K', 'Q', 'J'}
    
    # Handle potential OCR misrecognition for "10"
    for xx in valid_values:
        if xx in card_text:
            return xx


    card_value = ''.join(filter(lambda x: x in valid_values, card_text.split()))
    
    return card_value
if __name__ == "__main__":

    locations = [((631, 574), (669, 624), (662, 570), (639, 632))
                ]
    for cad_value_location in locations:
        card_value = get_card_value_from_box(cad_value_location[0], cad_value_location[1], cad_value_location[2], cad_value_location[3])
        print(f"Card value in the box: {card_value}")




"""
# Example usage:
if __name__ == "__main__":

    locations = [   
                    ((353, 326), (393, 373))
                    ,((470, 323), (497, 372))
                    ,((586, 326), (614, 373))
                    ,((703, 326), (739, 375))
                    ,((817, 322), (853, 377))
                    ,((345, 514), (385, 567))
                    ,((412, 505), (443, 556)) 
                    ,((760, 508), (794, 556))
                    ,((820, 503), (854, 556))                
                ]
    for cad_value_location in locations:
        card_value = get_card_value_from_box(cad_value_location[0], cad_value_location[1])
        print(f"Card value in the box: {card_value}")


# FIRST CARD BETWEEN 353, 326 AND 393, 373
# SECOND CARD BETWEEN 470, 323 AND 497, 372
# THIRD CARD BETWEEN 586, 326 AND 614, 373
# FOURTH 703, 326 AND 739, 375
# FIFTH 817, 322 AND 853, 377

# SIXTH 345, 514 AND 385, 567
# SEVENTH 412, 505 AND 443, 556

# EIGTH 760, 508 AND 794, 556
# NINTH 820, 503 AND 854, 556
"""