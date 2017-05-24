import sys
from itertools import permutations

if __name__ == '__main__':
    # default color count
    color_count = 5;

    # option to input color count via command-line
    if len(sys.argv) > 1:
        color_count = int(sys.argv[1]) + 1;

    # create as many color names as needed
    color_names = []
    for i in range(color_count):
        elem = "c" + str(i)
        color_names.append(elem)

    # get all permutations (as a generator)
    perm = list(permutations(color_names))

    # create output strings from list of tuples
    # print each output
    for elem in perm:
        output = ""
        for item in list(elem):
            output = output + item + "_"
        output = output[:-1]
        print output
