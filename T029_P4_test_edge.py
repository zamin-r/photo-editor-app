from Cimpl import*
from unit_testing import check_equal
from T029_P4_filter_edge import*



def test_detect_edges() -> None:
    """
    Author: Juan Sanchez, Zamin Rizvi

    Test function for detect_edges filter

    >>> test_detect_edges()
    >>> Checking pixel (0, 0); PASSED
    >>> Checking pixel (1, 0); PASSED
    >>> Checking pixel (2, 0); PASSED
    >>> Checking pixel (3, 0); PASSED
    >>> Checking pixel (4, 0); PASSED
    
    """
    
    original = create_image(5,1)
    set_color(original, 0, 0, create_color(10, 15, 20))
    set_color(original, 1, 0, create_color(80, 210, 21))
    set_color(original, 2, 0, create_color(100, 90, 40))
    set_color(original, 3, 0, create_color(252, 255, 250))
    set_color(original, 4, 0, create_color(0, 0, 0))

    expected = create_image(5,1)
    set_color(expected, 0, 0, create_color(10, 15, 20))
    set_color(expected, 1, 0, create_color(80, 210, 21))
    set_color(expected, 2, 0, create_color(100, 90, 40))
    set_color(expected, 3, 0, create_color(252, 255, 250))
    set_color(expected, 4, 0, create_color(0, 0, 0))


    edge = detect_edges(original, 2)    
    for x, y, ref_color in edge:
        check_equal('Checking pixel ('+str(x)+', '
                    +str(y)+');', ref_color, get_color(expected, x, y)) 
        
test_detect_edges()