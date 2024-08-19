from circle import Circle
import pytest

def test_create_circle():
    """Test that ensures a circle with a positive radius is created"""
    circle = Circle(10)
    assert isinstance(circle,Circle)


def test_create_circle_from_string():
    """Test that ensures a circle with a string as a radius is raising a TypeError"""
    with pytest.raises(TypeError):
        circle = Circle("20")
        


def test_create_circle_zero_radius():
    """Test than ensures a circle with zero radius is raising a ValueError"""
    with pytest.raises(ValueError):
        circle = Circle(0)
        

def test_create_circle_negative_radius():
    """Test than ensures a circle with negative radius is raising a ValueError"""
    with pytest.raises(ValueError):
        circle = Circle(-10)

#https://stackoverflow.com/questions/23337471/how-do-i-properly-assert-that-an-exception-gets-raised-in-pytest
