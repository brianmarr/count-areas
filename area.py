

# A class representing each individual area in an image.
# All Area properties is intialised on declaration of object.
class Area:
    def __init__(self, img_arr, init_coords):
        self.colour = img_arr[init_coords[0], init_coords[1]]
        self.coords = add_coord(img_arr, init_coords)


# This function was initially implemented recursively.
# However, due to the potentially large input data and Python's lack of tail-end recursion optimisation it is now executed iteratively as we can see.
# The iterative version still resembles recursion; next_coords is used as a stack to hold all the parameters 'passed' into the next iteration.
# Returns a complete set of co-ordinates belonging to the area in question.
def add_coord(img_arr, centre, coord_set=None):
    if coord_set == None:
        coord_set = {centre}
    # Initial parameters for a new area
    colour = img_arr[centre[0], centre[1]]
    coord_set = {(centre)}
    next_coords = [(centre)]
    # Each pixel in the area is 'examined' to see if any of the adjacent four pixels are the same colour to determine whether they can be bundled together in the same area.
    # Each bundled pixel is added to the stack to also be 'examined' later on.
    # Over this process the complete set of co-ordinates in the area is built up in coord_set.
    while (next_coords):
        curr_coords = next_coords.pop()
        x = curr_coords[0]
        y = curr_coords[1]
        if in_range(img_arr, x-1, y) and (x-1, y) not in coord_set and img_arr[x-1, y] == colour:
            next_coords.append((x-1, y))
            coord_set.add((x-1, y))
        if in_range(img_arr, x+1, y) and (x+1, y) not in coord_set and img_arr[x+1, y] == colour:
            next_coords.append((x+1, y))
            coord_set.add((x+1, y))
        if in_range(img_arr, x, y-1) and (x, y-1) not in coord_set and img_arr[x, y-1] == colour:
            next_coords.append((x, y-1))
            coord_set.add((x, y-1))
        if in_range(img_arr, x, y+1) and (x, y+1) not in coord_set and img_arr[x, y+1] == colour:
            next_coords.append((x, y+1))
            coord_set.add((x, y+1))
    return coord_set


# Returns boolean based on whether given co-ordinate values are within the image's boundaries
def in_range(img_arr, x, y):
    if x >= 0 and x < img_arr.shape[0] and y >= 0 and y < img_arr.shape[1]:
        return True
    return False
