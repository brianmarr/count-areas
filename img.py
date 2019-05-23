
import sys
import numpy as np
from area import *

MAX_SHADE = 256


# All Img properties are initialised on declaration of object.
class Img:
    def __init__(self, name, height, width, test=None):
        self.name = name
        self.height = height
        self.width = width
        # The image is converted from string of bytes to a 2D numpy array.
        self.array = bytes2arr(self.name, height, width)
        # List of each individual area with each one's colour and co-ordinate set.
        self.areas = get_areas(self.array)

    def print_areas(self):
        colours = []
        for area in self.areas:
            colours.append(area.colour)
        for shade in range(MAX_SHADE):
            print(colours.count(shade))


# Converts the input byte string into a numpy 2D array with input dimensions. Returns the array.
def bytes2arr(file_name, height, width):
    try:
        with open(file_name, 'rb') as f:
            arr = np.array([list(f.read())])
    except IOError:
        print("Could not read file:", file_name)
        sys.exit(1)

    try:
        arr.shape = (height, width)
    except ValueError:
        print("ValueError: Your image does not fit to your given height and weight dimensions.")
        sys.exit(1)

    return arr


# Every pixel in the image belongs to a particular area, and no pixel belongs to multiple areas.
# Therefore we can iterate over every single pixel given that it has not already been found to belong to another area.
# Returns a list containing all areas in the image, including their colours and set of all co-ordinates.
def get_areas(img_arr):
    areas = []
    checked_coords = set()
    for x in range(img_arr.shape[0]):
        for y in range(img_arr.shape[1]):
            if (x, y) not in checked_coords:
                # We only need to input (x,y) - any single set of co-ordinates lying within the area.
                new_area = Area(img_arr, (x, y))
                areas.append(new_area)
                # The total set of all co-ordinates in the area is added to the list of already checked co-ordinates.
                checked_coords = checked_coords | new_area.coords
    return areas
