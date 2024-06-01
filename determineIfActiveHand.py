import loadPoints, getColours, compareStrings

def handIsActive(img):
	# Example usage
	directory = 'pointStorage'
	filename = 'activeHand.txt'

	outcome = None

	points = loadPoints.read_coordinates(directory + '/' + filename)
	colours = getColours.get_color_names_at_coordinates(img, points)
	if compareStrings.all_strings_same(colours):
		outcome = False
	else:
		outcome = True

	return outcome
