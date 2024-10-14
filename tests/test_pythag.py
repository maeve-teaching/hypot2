import numpy as np
import hypot2.pythag

def test_add_nums():
    '''Tests the function that adds two numbers'''

    # Arrange
    test_variable_a = 3.5
    test_variable_b = 4
    expected_output = 7.5

    # Act
    output = hypot2.pythag.add_nums(test_variable_a, test_variable_b)

    # Assert
    assert output == expected_output


def test_add_nums_arrays():
    '''Tests the function that adds two arrays'''

    # Arrange
    test_array_a = np.array([2, 5.7, 8])
    test_array_b = np.array([1.0, 1.0, 1.0])
    expected_output = np.array([3, 6.7, 9])

    # Act
    output = hypot2.pythag.add_nums(test_array_a, test_array_b)

    # Assert
    assert np.allclose(expected_output, output)

def test_square_number():
    '''Test for the example function'''

    # Arrange
    test_variable_1 = 7
    expected_output = 49

    # Act
    output = hypot2.pythag.square_number(test_variable_1)

    # Assert
    assert output == expected_output

    # No cleanup needed

def test_square_array():
    '''Test for the example function'''

    # Arrange
    test_array_1 = np.array([7, 4, 5])
    expected_output = np.array([49, 16, 25])

    # Act
    output = hypot2.pythag.square_number(test_array_1)

    # Assert
    assert np.allclose(expected_output, output)

def test_square_root():
    '''Test for the square root function'''

    # Arrange
    test_variable_1 = 16
    expected_output = 4

    # Act
    output = hypot2.pythag.square_root(test_variable_1)

    # Assert
    assert output == expected_output

def test_square_root_array():
    '''Test for the square root function for an array'''

    # Arrange
    test_array_1 = np.array([16, 49, 64])
    expected_output = np.array([4, 7, 8])

    # Act
    output = hypot2.pythag.square_root(test_array_1)

    # Assert
    assert np.allclose(expected_output, output)
    
def test_square_root_2():
    '''Test for the square root function'''

    # Arrange
    test_variable_1 = 16
    expected_output = np.sqrt(16)

    # Act
    output = hypot2.pythag.square_root(test_variable_1)

    # Assert
    assert output == expected_output

def test_calc_hypot():
    '''Integration test for calc_hypot'''

    # Arrange
    test_variable_1 = 5.6
    test_variable_2 = 7.8
    expected_output = 9.6

    # Act
    output = hypot2.pythag.calc_hypot(test_variable_1, test_variable_2)

    # Assert
    assert np.allclose(expected_output, output, atol=1e-3)

def test_calc_hypot():
    '''Integration test for calc_hypot'''

    # Arrange
    test_variable_1 = np.array([10, 30045, 6.9, 0.04])
    test_variable_2 = np.array([23, 2400, 8.9, 0.34])
    expected_output = np.array([25.08, 30140.7, 11.26, 0.34])

    # Act
    output = hypot2.pythag.calc_hypot(test_variable_1, test_variable_2)

    # Assert
    assert np.allclose(expected_output, output, rtol=1e-1)