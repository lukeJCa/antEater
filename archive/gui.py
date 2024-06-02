import tkinter as tk
from tkinter import messagebox
import os, pyautogui
import coordinates, getColours, compareStrings, suites, ranking

def char_right_of_first_underscore(s):
    pos = s.find('_')
    if pos != -1 and pos + 1 < len(s):
        return s[pos + 1]
    return None  # or raise an error or return a default value

# Define the functions that will be executed by the buttons
def script1():
    try:
        os.system('python resize.py')
    except Exception as e:
        messagebox.showerror("Error", f"Failed to run script: {e}")
        print(f"Error: {e}")

def script2():
    try:
        os.system('python place.py')
    except Exception as e:
        messagebox.showerror("Error", f"Failed to run script: {e}")
        print(f"Error: {e}")

def run_screen_point_selector():
    # Run the external script "screenPointSelector.py"
    try:
        os.system('python screenPointSelector.py')
    except Exception as e:
        messagebox.showerror("Error", f"Failed to run script: {e}")
        print(f"Error: {e}")

def hole_cards():
    first_hole_card_options = coordinates.preloadCoordinates('6_', 'pointStorage')
    second_hole_card_options = coordinates.preloadCoordinates('7_', 'pointStorage')
    # Take a screenshot
    screenshot = pyautogui.screenshot()
    # Convert image to RGB (in case it is in another mode like RGBA, L, etc.)
    img = screenshot.convert('RGB')

    found = False
    card1 = None
    for file in first_hole_card_options: # JACK LOOKS LIKE 3 AND 9, THE GLOB ORDERS THEM RIGHT BUT WATCH IT
        if found == False:
            points = file[1]
            name = file[0]
            colours = getColours.get_color_names_at_coordinates(img, points)
            if compareStrings.all_strings_same(colours):
                card1 = char_right_of_first_underscore(name)
                found = True

    found = False
    card2 = None
    for file in second_hole_card_options: # JACK LOOKS LIKE 3 AND 9, THE GLOB ORDERS THEM RIGHT BUT WATCH IT
        if found == False:
            points = file[1]
            name = file[0]
            colours = getColours.get_color_names_at_coordinates(img, points)
            if compareStrings.all_strings_same(colours):
                card2 = char_right_of_first_underscore(name)
                found = True

    card1suite = suites.get_suite(first_hole_card_options, img)
    card2suite = suites.get_suite(second_hole_card_options, img)
    hole_card1 = str(card1) + str(card1suite)
    hole_card2 = str(card2) + str(card2suite)
    hole_cards = [hole_card1, hole_card2]
    print(hole_card1)
    print(hole_card2)
    return hole_cards


def detectObject(img,NameAndCoordinateTuple):
    points = NameAndCoordinateTuple[1]
    name = NameAndCoordinateTuple[0]
    colours = getColours.get_color_names_at_coordinates(img, points)
    if compareStrings.all_strings_same(colours):
        player1Present = False

def detectPlayers():
    player_locations = coordinates.preloadCoordinates('P_', 'pointStorage')

    # Take a screenshot
    screenshot = pyautogui.screenshot()
    # Convert image to RGB (in case it is in another mode like RGBA, L, etc.)
    img = screenshot.convert('RGB')

    players = 0
    for file in player_locations: # JACK LOOKS LIKE 3 AND 9, THE GLOB ORDERS THEM RIGHT BUT WATCH IT
        points = file[1]
        name = file[0]
        colour = getColours.most_prominent_color(img, points)
        if colour == "yellow":
            players += 1
    print(players)
    return players

def winningOdds():
    percentage = ranking.simulate_poker(detectPlayers(), hole_cards(), known_community_cards = [], num_simulations = 100)
    print(percentage)

def openWebsite(url):
    import webbrowser
    try:
        webbrowser.open(url)
        print(f"Opening website: {url}")
    except Exception as e:
        print(f"Error opening website: {e}")

# Example usage
#openWebsite("https://www.playwsop.com/play")


# Create the main application window
root = tk.Tk()
root.title("Hold Em GUI")
root.geometry("300x300")  # Set the default window size

# Create buttons and associate them with the respective scripts
button1 = tk.Button(root, text="Resize WSOP Tab", command=script1)
button1.pack(pady=10)

button2 = tk.Button(root, text="Corner WSOP Tab", command=script2)
button2.pack(pady=10)

button4 = tk.Button(root, text="Screen Point Selector", command=run_screen_point_selector)
button4.pack(pady=10)

button5 = tk.Button(root, text="What are my hole cards", command=hole_cards)
button5.pack(pady=10)

button5 = tk.Button(root, text="How Many Players", command=detectPlayers)
button5.pack(pady=10)

button5 = tk.Button(root, text="Odds of Winning", command=winningOdds)
button5.pack(pady=10)

# Run the application
root.mainloop()
