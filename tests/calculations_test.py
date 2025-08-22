# System Modules
import sys
import os
import math  # <-- Add this import

# Installed Modules
import pytest

# Project Modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from calculations import area_of_circle, get_nth_fibonacci   # noqa: E402


def test_area_of_circle_positive_radius():
    """Test with a positive radius."""
    # Arrange
    radius = 1

    # Act
    result = area_of_circle(radius)

    # Assert
    assert abs(result - 3.14159) < 1e-5


def test_area_of_circle_zero_radius():
    """Test with a radius of zero."""
    # Arrange
    radius = 0

    # Act
    result = area_of_circle(radius)

    # Assert
    assert result == 0


def test_area_of_circle_large_radius():
    """Test with a large radius."""
    radius = 1000
    result = area_of_circle(radius)
    assert abs(result - (math.pi * 1000 ** 2)) < 1e-5

def test_area_of_circle_float_radius():
    """Test with a float radius."""
    radius = 2.5
    result = area_of_circle(radius)
    assert abs(result - (math.pi * 2.5 ** 2)) < 1e-5

def test_area_of_circle_negative_radius():
    """Test with a negative radius (should raise ValueError)."""
    with pytest.raises(ValueError):
        area_of_circle(-1)

def test_get_nth_fibonacci_three():
    """Test with n=3."""
    n = 3
    result = get_nth_fibonacci(n)
    assert result == 2

def test_get_nth_fibonacci_four():
    """Test with n=4."""
    n = 4
    result = get_nth_fibonacci(n)
    assert result == 3

def test_get_nth_fibonacci_large():
    """Test with a large n."""
    n = 20
    result = get_nth_fibonacci(n)
    assert result == 6765

def test_get_nth_fibonacci_ten_correct():
    """Test with n=10, correct expected value."""
    n = 10
    result = get_nth_fibonacci(n)
    assert result == 55
    # Arrange
    n = 0

    # Act
    result = get_nth_fibonacci(n)

    # Assert
    assert result == 0


def test_get_nth_fibonacci_one():
    """Test with n=1."""
    # Arrange
    n = 1

    # Act
    result = get_nth_fibonacci(n)

    # Assert
    assert result == 1


def test_get_nth_fibonacci_ten():
    """Test with n=10."""
    # Arrange
    n = 10

    # Act
    result = get_nth_fibonacci(n)

    # Assert
    assert result == 55


def test_get_nth_fibonacci_negative():
    """Test with negative n (should raise ValueError)."""
    with pytest.raises(ValueError):
        get_nth_fibonacci(-5)
