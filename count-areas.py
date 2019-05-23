

import sys
from img import *
from cmd_arg_errors import cmd_args_error_check

# Checks for and handles any errors with input command line args (except for IOError with input image file)
cmd_args_error_check(sys.argv)


[height, width] = sys.argv[3].split(',')
height = int(height)
width = int(width)
# All Img properties (including areas) are defined upon creation of this object.
img = Img(sys.argv[1], height, width)

img.print_areas()
