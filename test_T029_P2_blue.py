from T029_P2_blue import blue_channel
from unit_testing import check_equal
from Cimpl import *


def test_blue_channel() -> None:
    
    reference = create_image(4,1)
    set_color(reference, 0, 0, create_color(0, 0, 0))
    set_color(reference, 1, 0, create_color(128, 128, 128))
    set_color(reference, 2, 0, create_color(255, 255, 255))
    
    expected = create_image(4,1)
    set_color(expected, 0, 0, create_color(0, 0, 0))
    set_color(expected, 1, 0, create_color(0, 128, 0))
    set_color(expected, 2, 0, create_color(0, 255, 0))
    
    test_image = blue_channel(reference)
    print(' ')
    
    for x, y, ref_color in test_image:
        check_equal('Checking pixel ('+str(x)+',  '+str(y)+');', ref_color, get_color(expected, x, y))
        
    
    
print("\nTesting blue_channel():\n")

test_blue_channel()
