# T029
# Author: Yasmina Younes
# Student number: 101193167

# 0 imports
from Cimpl import*
from unit_testing import check_equal
from T029_P4_filter_horizontal import*

# 1 The test function


def test_flip_horizontal() -> None:
    '''test function for the horizontal flip filter.
    >>> test_flip_horizontal()
    '''
    original = create_image(6, 1)
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 1, 0, create_color(100, 60, 20))
    set_color(original, 2, 0, create_color(104, 104, 104))
    set_color(original, 3, 0, create_color(255, 205, 140))
    set_color(original, 4, 0, create_color(255, 255, 255))
    set_color(original, 5, 0, create_color(1, 1, 1))

    expected = create_image(6, 1)
    set_color(expected, 0, 0, create_color(1, 1, 1))
    set_color(expected, 1, 0, create_color(255, 255, 255))
    set_color(expected, 2, 0, create_color(255, 205, 140))
    set_color(expected, 3, 0, create_color(104, 104, 104))
    set_color(expected, 4, 0, create_color(100, 60, 20))
    set_color(expected, 5, 0, create_color(0, 0, 0))

    image_tested = flip_horizontal(original)
    for x, y, col in image_tested:
        check_equal('Checking pixel @(' + str(x) + ', '
                    + str(y) + ')', col, get_color(expected, x, y))


# 2 Main Script
test_flip_horizontal()
