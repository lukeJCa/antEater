import loadPoints, getColours, determineIfActiveHand
import pyautogui
import os
import glob
import compareStrings

# Example usage
directory = 'pointStorage'
prefix = '6_'

# load all the data files for images beforehand, keep them in memory for speed
def preloadCoordinates():

	coordinateTupleArray = []

	# Construct the search pattern for the glob function
	search_pattern = os.path.join(directory, f"{prefix}*.txt")

	# Use glob to find all files matching the pattern
	for file_path in glob.glob(search_pattern):
		points = loadPoints.read_coordinates(file_path)
		coordinateTupleArray.append((file_path, points))
	return coordinateTupleArray

def load_text_files_with_prefix(coordinates, img):

	# Create a dictionary to store the file contents
	file_contents = {}

	# Construct the search pattern for the glob function
	search_pattern = os.path.join(directory, f"{prefix}*.txt")

	found = False
	# Use glob to find all files matching the pattern
	for file in coordinates: # JACK LOOKS LIKE 3 AND 9, THE GLOB ORDERS THEM RIGHT BUT WATCH IT
		if found == False:
			points = file[1]
			name = file[0]
			colours = getColours.get_color_names_at_coordinates(img, points)
			if compareStrings.all_strings_same(colours):
				print(name)
				found = True
			#print(colors)
	return file_contents

def filter_tuples_by_first_element(tuples_array):
    """
    Create a subset of an array of tuples where the first element of each tuple contains an "S".
    
    :param tuples_array: List of tuples.
    :return: List of tuples where the first element contains an "S".
    """
    return [t for t in tuples_array if '_S' in t[0]]

def determineSuitsFromColours(suiteColours):
	suite = None
	if suiteColours == ["red", "red"]:
		suite = 'd'
	elif suiteColours == ["black", "black"]:
		suite = 's'
	if suiteColours == ["white", "red"]:
		suite = 'h'
	if suiteColours == ["white", "black"]:
		suite = 'c'
	return suite


if __name__ == '__main__':
	

	# Take a screenshot
	screenshot = pyautogui.screenshot()
	# Convert image to RGB (in case it is in another mode like RGBA, L, etc.)
	img = screenshot.convert('RGB')	
	coordinates = preloadCoordinates()
	
	if determineIfActiveHand.handIsActive(img):
		files_contents = load_text_files_with_prefix(coordinates, img)

		suiteTuples = filter_tuples_by_first_element(coordinates)
		for suiteTuple in suiteTuples:
			suiteColours = getColours.get_color_names_at_coordinates(img,suiteTuple[1])
			print(determineSuitsFromColours(suiteColours))
	else:
		print("We are not in the hand")

