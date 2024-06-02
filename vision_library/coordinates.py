import os
import glob
from vision_library import loadPoints

# load all the data files for images beforehand, keep them in memory for speed
def preloadCoordinates(prefix, directory):

	coordinateTupleArray = []

	# Construct the search pattern for the glob function
	search_pattern = os.path.join(directory, f"{prefix}*.txt")

	# Use glob to find all files matching the pattern
	for file_path in glob.glob(search_pattern):
		points = loadPoints.read_coordinates(file_path)
		coordinateTupleArray.append((file_path, points))
	return coordinateTupleArray