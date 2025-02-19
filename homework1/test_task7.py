from task7 import array_manip
import numpy as np

def test_array_manip():
    assert np.array_equal(array_manip(), np.array([2, 4, 6, 8, 10])) # checks if the numpy array returned by the function is equal to the expected numpy array