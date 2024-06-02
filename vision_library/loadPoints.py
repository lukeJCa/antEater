def read_coordinates(file_name):
    """
    Reads a list of x and y coordinates from a text file.

    Args:
    file_name (str): The name of the file containing the coordinates.

    Returns:
    list of tuple: A list of tuples where each tuple represents an (x, y) coordinate.
    """
    coordinates = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                x, y = map(int, line.strip().split(','))
                coordinates.append((x, y))
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")
    except ValueError:
        print("Error parsing the file. Ensure it contains only coordinates in the format 'x,y'.")

    return coordinates

