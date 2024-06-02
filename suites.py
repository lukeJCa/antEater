from vision_library import getColours

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

def get_suite(coordinates, img):
	result_suite = None
	suiteTuples = filter_tuples_by_first_element(coordinates)
	for suiteTuple in suiteTuples:
		suiteColours = getColours.get_color_names_at_coordinates(img,suiteTuple[1])
		result_suite = determineSuitsFromColours(suiteColours)
	return result_suite
