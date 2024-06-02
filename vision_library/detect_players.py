from vision_library import coordinates, getColours

def read_deck_file(file_path):
    """
    Reads the content of a file and returns it as a string.
    
    Parameters:
    file_path (str): The path to the file to be read.
    
    Returns:
    str: The content of the file as a string.
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "File not found. Please check the path and try again."
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage
# file_path = 'vision_library/deck.txt'
# print(read_deck_file(file_path))


def detectNumberOfPlayers(screenshot, prefix = 'P_', directory = 'pointStorage'):
    

    player_locations = coordinates.preloadCoordinates(prefix, read_deck_file("vision_library\deck.txt"))

    players = 0
    for file in player_locations: # JACK LOOKS LIKE 3 AND 9, THE GLOB ORDERS THEM RIGHT BUT WATCH IT
        points = file[1]
        name = file[0]
        colour = getColours.most_prominent_color(screenshot, points)
        if colour == "yellow":
            players += 1
    return players