from vision_library import coordinates, getColours, determineColour, compareStrings, suites
import pyautogui

# generic function given an input prefix and directory to look for reference files
# screenshot -> pretaken screenshot to check the reference files against
# prefix -> from 1_ to 7_ indicating which card we are looking for
# directory -> where the options for all the cards are, should these already be loaded in memory?
def identify_card(screenshot, prefix, directory):
    
    card_options_with_suites = coordinates.preloadCoordinates(prefix, directory) # shouldnt include the S
    suite_options = [t for t in card_options_with_suites if t[0].find('_S') != -1]
    card_options = [t for t in card_options_with_suites if t[0].find('_S') == -1]

    found = False # used to stop searching once we have it, also breaks draws if it would find J + 3
    card_number = None # or letter
    for file in card_options: #contains tuples where the first one is the file name, second are the coordinates
        if found == False:
            points = file[1]
            name = file[0]
            colours = getColours.get_color_names_at_coordinates(screenshot, points)
            if compareStrings.all_strings_same(colours):
                card_number = compareStrings.char_right_of_first_underscore(name)
                found = True

    print(card_number)
    card_suite = suites.get_suite(suite_options, screenshot) # only the S is considered
    print(card_suite)
    output_card_string = None
    if found == True and card_number is not None and card_suite is not None: # only if we know there have been no issues
        output_card_string = card_number + card_suite
    return output_card_string

def flop_cards():
    # Take a screenshot
    screenshot = pyautogui.screenshot()
    # Convert image to RGB (in case it is in another mode like RGBA, L, etc.)
    img = screenshot.convert('RGB')

    flop_card1 = identify_card(img, '1_', 'pointStorage')
    flop_card2 = identify_card(img, '2_', 'pointStorage')
    flop_card3 = identify_card(img, '3_', 'pointStorage')

    flop_cards = [flop_card1, flop_card2, flop_card3]
    return flop_cards

def turn_card():
    # Take a screenshot
    screenshot = pyautogui.screenshot()
    # Convert image to RGB (in case it is in another mode like RGBA, L, etc.)
    img = screenshot.convert('RGB')

    turn_card = identify_card(img, '4_', 'pointStorage')

    return [turn_card]

def river_card():
    # Take a screenshot
    screenshot = pyautogui.screenshot()
    # Convert image to RGB (in case it is in another mode like RGBA, L, etc.)
    img = screenshot.convert('RGB')

    turn_card = identify_card(img, '5_', 'pointStorage')

    return [turn_card]


def hole_cards():

    # Take a screenshot
    screenshot = pyautogui.screenshot()
    # Convert image to RGB (in case it is in another mode like RGBA, L, etc.)
    img = screenshot.convert('RGB')

    hole_card1 = identify_card(img, '6_', 'pointStorage')
    hole_card2 = identify_card(img, '7_', 'pointStorage')

    hole_cards = [hole_card1, hole_card2]
    return hole_cards