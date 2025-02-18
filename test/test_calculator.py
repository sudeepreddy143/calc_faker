'''My Calculator Test'''
from calculator import add, subtract

def test_addition():
    '''Test that addition function works '''    
    assert add(1,7) == 8

def test_subtraction():
    '''Test that addition function works '''    
    assert subtract(7,4) == 3