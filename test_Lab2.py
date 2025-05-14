import pytest
from unittest.mock import patch

# Assuming the functions are in Lab2.py
from Lab2 import calc_average, find_min_max, sort_temperature, calc_median_temp

def test_calc_average():
    # Mock the user input for the list of numbers
    with patch('builtins.input', return_value="5, 67, 32"):
        float_list = [5, 67, 32]
        expected = sum(float_list) / len(float_list)
        assert calc_average(float_list) == expected

def test_find_min_max():
    # Mock the user input for the list of numbers
    with patch('builtins.input', return_value="5, 67, 32"):
        float_list = [5, 67, 32]
        minimum = min(float_list)
        maximum = max(float_list)
        assert find_min_max(float_list) == (minimum, maximum)

def test_sort_temperature():
    # Mock the user input for the list of numbers
    with patch('builtins.input', return_value="5, 67, 32"):
        float_list = [5, 67, 32]
        sorted_list = sorted(float_list)
        assert sort_temperature(float_list) == sorted_list

def test_calc_median_temp():
    # Mock the user input for the list of numbers
    with patch('builtins.input', return_value="5, 67, 32"):
        float_list_odd = [5, 67, 32]
        sorted_list_odd = sorted(float_list_odd)
        median_odd = sorted_list_odd[len(sorted_list_odd) // 2]
        assert calc_median_temp(float_list_odd) == median_odd

        # Test case with an even number of elements
        float_list_even = [5, 67, 32, 20]
        sorted_list_even = sorted(float_list_even)
        median_even = (sorted_list_even[1] + sorted_list_even[2]) / 2
        assert calc_median_temp(float_list_even) == median_even
