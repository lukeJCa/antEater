from vision_library import coordinates, getColours

def detectNumberOfPlayers(screenshot, prefix = 'P_', directory = 'pointStorage'):
    
    player_locations = coordinates.preloadCoordinates(prefix, directory)

    players = 0
    for file in player_locations: # JACK LOOKS LIKE 3 AND 9, THE GLOB ORDERS THEM RIGHT BUT WATCH IT
        points = file[1]
        name = file[0]
        colour = getColours.most_prominent_color(screenshot, points)
        if colour == "yellow":
            players += 1
    return players