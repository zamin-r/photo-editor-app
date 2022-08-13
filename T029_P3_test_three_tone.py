from T029_P3_filter_three_tone import three_tone
from unit_testing import check_equal
from Cimpl import *


def test_three_tone() -> None:  
    """
    Author: Zamin Rizvi
    
    This test function compares the expected outcome with the three_tone filter 
    function outcome, returning whether or not if the test has successfully
    passed. There are a total of 9 tests.
    
    >>> test_three_tone()
    >>> Checking pixel (0,  0); PASSED
    >>> Checking pixel (1,  0); PASSED
    >>> Checking pixel (2,  0); PASSED
    
    
    """ 
    initial = create_image(3, 1)
    set_color(initial, 0, 0,  create_color(200, 255, 255))
    set_color(initial, 1, 0,  create_color(10, 15, 15))
    set_color(initial, 2, 0,  create_color(255, 0, 110))
 

    expected = create_image(3, 1) 
    set_color(expected, 0, 0,  create_color(0, 0, 255))
    set_color(expected, 1, 0,  create_color(0, 0, 0))
    set_color(expected, 2, 0,  create_color(255, 255, 0))

    
    tone = three_tone(initial, "black", "lemon", "blue")
    print(' ')
    for x, y, ref_color in tone:
        check_equal('Checking pixel ('+str(x)+',  '+str(y)+');', ref_color, get_color(expected, x, y))
        

print("\nTesting three_tone():\n")



test_three_tone()
