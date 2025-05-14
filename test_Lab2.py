import pytest

# Assuming the functions are in Lab2.py
from Lab2 import calc_average, find_min_max, sort_temperature, calc_median_temp

def test_calc_average():
    float_list = [5.0, 67.0, 32.0]
    expected = sum(float_list) / len(float_list)
    assert calc_average(float_list) == expected

def test_find_min_max():
    float_list = [5.0, 67.0, 32.0]
    assert find_min_max(float_list) == (min(float_list), max(float_list))

def test_sort_temperature():
    float_list = [5.0, 67.0, 32.0]
    assert sort_temperature(float_list) == sorted(float_list)

def test_calc_median_temp():
    # Test odd number of elements
    float_list_odd = [5.0, 67.0, 32.0]
    sorted_odd = sorted(float_list_odd)
    median_odd = sorted_odd[len(sorted_odd) // 2]
    assert calc_median_temp(float_list_odd) == median_odd

    # Test even number of elements
    float_list_even = [5.0, 67.0, 32.0, 20.0]
    sorted_even = sorted(float_list_even)
    mid = len(sorted_even) // 2
    median_even = (sorted_even[mid - 1] + sorted_even[mid]) / 2
    assert calc_median_temp(float_list_even) == median_even
