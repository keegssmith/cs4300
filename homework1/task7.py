import numpy as np # using numpy package

# creates an array of even numbers from 0-9, then adds two to each array value
def array_manip():
    # create array (rank 1)
    array = np.array([0,2,4,6,8])

    # add two to every element in the array
    new_array = (array + 2)

    return new_array

print(array_manip())