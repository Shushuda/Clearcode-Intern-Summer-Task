from typing import List, Tuple
import numpy


# function for calculating the max possible value of a set of digital items that can fit on a given usb stick
# returns a tuple containing the max possible value and a set of memes' names used to achieve that value
def calculate(usb_size: int, memes: List[Tuple[str, int, int]]) -> Tuple[int, set]:
    # conversion of variable 'usb_size' to int in case of a type mismatch
    # throws an exception if the variable cannot be converted
    try:
        usb_size = int(usb_size) * 1024
    except ValueError:
        raise ValueError(f"Couldn't convert usb_size: '{usb_size}' to int.")

    # checks if the variable 'memes' is the correct type
    if type(memes) is not list:
        raise TypeError("memes is not a list.")

    # checks for the number of values inside a meme
    # allows only exactly 3 elements (name, size, price)
    # also checks if the types are correct
    for meme in memes:
        # accepts lists instead of tuples due to the results being the same with both types
        if not isinstance(meme, (tuple, list)):
            raise TypeError("Values inside a list are not tuples.")
        elif len(meme) != 3:
            raise ValueError("Too many or too few values inside a tuple.")
        elif type(meme[0]) is not str:
            raise TypeError("First value inside a tuple is not a str.")
        elif type(meme[1]) is not int or type(meme[2]) is not int:
            raise TypeError("Values inside a tuple are not an int.")

    item_num = len(memes)

    # matrix of 0 elements to initialize a fixed size, where the nth item is the max value of the memes (hence the "+1")
    matrix = numpy.zeros((item_num + 1, usb_size + 1), dtype=int)

    # uses a Dynamic Programming Algorithm for a Knapsack 0-1 problem
    # loops over the items and compares their sizes to create a matrix with the nth item being
    # the max possible value
    item = 1
    while item <= item_num:
        usb = 0
        while usb <= usb_size:
            if int(memes[item - 1][1]) > usb:
                matrix[item][usb] = matrix[item - 1][usb]
            else:
                matrix[item][usb] = max(matrix[item - 1][usb], matrix[item - 1][usb - int(memes[item - 1][1])]
                                        + int(memes[item - 1][2]))

            usb += 1

        item += 1

    # set-up for finding the items used to acquire the max possible value
    # the items will be added to a set due to task's requirements
    result = matrix[item_num][usb_size]
    capacity = usb_size
    meme = set()

    # retrieving the items' names
    i = item_num
    while i > 0 and result > 0:
        if result != matrix[i - 1][capacity]:
            meme.add(str(memes[i - 1][0]))
            result -= int(memes[i - 1][2])
            capacity -= int(memes[i - 1][1])
        i -= 1

    # solution consisting of a tuple with the total value of the memes used and a set of names of the used memes
    memes_solution = (matrix[item_num][usb_size], meme)

    return memes_solution
