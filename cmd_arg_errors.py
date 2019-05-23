

import sys


def cmd_args_error_check(argv):
    assert(len(argv) == 4), "\nPlease follow correct usage.\nUsage: 'python count-areas.py <input-filename> --shape <height>,<width>'"
    assert(argv[2] == "--shape"), "\nPlease follow correct usage.\nUsage: 'python count-areas.py <input-filename> --shape <height>,<width>'"
    try:
        [height, width] = argv[3].split(',')
        height = int(height)
        width = int(width)
    except:
        print("Please follow correct usage.")
        print("Usage: 'python count-areas.py <input-filename> --shape <height>,<width>'")
        sys.exit(1)
