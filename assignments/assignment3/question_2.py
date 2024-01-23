"""
2. Numpy
    Using NumPy create random vector of size 20 having only float in the range 1-20.
    Then reshape the array to 4 by 5
    Then replace the max in each row by 0 (axis=1)
    (you can NOT implement it via for loop)
"""

import numpy as np


def problem_2():
    # Create random vector of size 20 having only float in the range 1-20.
    low = 1
    high = 20
    size = 20
    numpy_random_vector = np.random.uniform(low, high, size)
    print('Random Vector: \n{}\n'.format(numpy_random_vector))

    # Reshape array to 4 by 5
    rows = 4
    columns = 5
    reshape_array = numpy_random_vector.reshape(rows, columns)
    print('After reshape (4 by 5): \n{}\n'.format(reshape_array))

    # Replace the max in each row by 0 (axis=1)
    reshape_array[np.arange(rows), reshape_array.argmax(axis=1)] = 0
    print('After replacing max in each row by 0: \n{}\n'.format(reshape_array))


# call method
problem_2()
