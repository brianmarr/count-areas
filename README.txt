

Created by Brian Marr 
18/05/2019

___________

This program takes in a greyscale image file (represented as a string of unsigned bytes) with user-input dimensions and outputs the number of areas for each colour (from 0 to 255)
___________

External modules required:
 - numpy
____________

Please run the program as following:
'python count-areas.py <input-filename> --shape <height>,<width>'

E.g. 'python count-areas.py sample.bin --shape 256,256'

____________

The output will consist of the number of areas in each colour/shade (starting from 0 to 255) present in the image.
E.g. for input file 'sample.bin' (included), the output will be:

3
0
0
...
0
0
2
0
0
...
0
0
2



