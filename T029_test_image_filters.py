# T029
# Milestone 2
# Date of submission: June 9 2021
# Authors:
# Yasmina Younes (101193167)
# Khushi Patel (101195547)
# Juan Sanchez (101202430)
# Zamin Rizvi (101203136)


# 0 Imports --------------------------------------------------------------------
from T029_image_filters import*
from Cimpl import*
from unit_testing import check_equal


# 1 Testing Functions ----------------------------------------------------------

# Three Tone Filter Testing Function
def test_three_tone() -> None:
    """test function for the three tone filter.
    >>> test_three_tone()
-Zamin Rizvi (101203136)
    """
    initial = create_image(3, 1)
    set_color(initial, 0, 0, create_color(200, 250, 240))
    set_color(initial, 1, 0, create_color(10, 15, 15))
    set_color(initial, 2, 0, create_color(150, 150, 100))

    expected = create_image(3, 1)
    set_color(expected, 0, 0, create_color(255, 255, 255))
    set_color(expected, 1, 0, create_color(0, 0, 0))
    set_color(expected, 2, 0, create_color(128, 128, 128))

    print(' ')
    for x, y, ref_color in initial:
        check_equal('Checking pixel (' + str(x) + ',  '
                    + str(y) + ');', ref_color, get_color(expected, x, y))


# Extreme Contrast Filter Testing Function


def test_extreme_contrast() -> None:
    """test function for the extreme contrast filter.
-Juan Sanchez (101202430)
-Khushi Patel (101195547)
    """
    original = create_image(4, 1)
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 1, 0, create_color(0, 255, 0))
    set_color(original, 2, 0, create_color(0, 1, 255))
    set_color(original, 3, 0, create_color(255, 3, 2))

    expected = create_image(4, 1)
    set_color(expected, 0, 0, create_color(0, 0, 0))
    set_color(expected, 1, 0, create_color(0, 255, 0))
    set_color(expected, 2, 0, create_color(0, 0, 255))
    set_color(expected, 3, 0, create_color(255, 0, 0))

    contrast_image = extreme_contrast(original)

    for x, y, col in contrast_image:
        check_equal('Checking pixel @(' + str(x) + ', ' +
                    str(y) + ')', col, get_color(expected, x, y))

# Sepia Tinting Filter Testing Function


def test_sepia_filter() -> None:
    '''test function for the sepia filter.
    >>> test_sepia_filter()
-Yasmina Younes (101193167)
    '''
    original = create_image(5, 1)
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 1, 0, create_color(100, 60, 20))
    set_color(original, 2, 0, create_color(104, 104, 104))
    set_color(original, 3, 0, create_color(255, 205, 140))
    set_color(original, 4, 0, create_color(255, 255, 255))

    expected = create_image(5, 1)
    set_color(expected, 0, 0, create_color(0, 0, 0))  # black
    set_color(expected, 1, 0, create_color(66, 60, 54))  # dark gray
    set_color(expected, 2, 0, create_color(119, 104, 88))  # medium gray
    set_color(expected, 3, 0, create_color(216, 200, 186))  # light gray
    set_color(expected, 4, 0, create_color(255, 255, 237))  # white

    image_tested = sepia(original)
    for x, y, col in image_tested:
        check_equal('Checking pixel @(' + str(x) + ', ' +
                    str(y) + ')', col, get_color(expected, x, y))

# Posterizing Filter Testing Function


def test_posterizing_filter() -> None:
    """test function for posterizing filter
    >>> test_posterizing_filter()
-Khushi Patel (101195547)
    """
    original = create_image(4, 1)
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 1, 0, create_color(145, 120, 136))
    set_color(original, 2, 0, create_color(113, 157, 134))
    set_color(original, 3, 0, create_color(255, 255, 255))

    expected = create_image(4, 1)
    set_color(expected, 0, 0, create_color(31, 31, 31))
    set_color(expected, 1, 0, create_color(159, 95, 159))
    set_color(expected, 2, 0, create_color(95, 159, 159))
    set_color(expected, 3, 0, create_color(233, 233, 233))

    posterized_image = posterize(original)
    for x, y, col in posterized_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))

# Edge Detection Filter Testing Function


def test_detect_edges() -> None:
    """test function for edge detect filter.
    >>> test_detect_edges()
-Juan Sanchez (101202430)
    """
    original = create_image(5, 1)
    set_color(original, 0, 0, create_color(10, 15, 20))
    set_color(original, 1, 0, create_color(80, 210, 21))
    set_color(original, 2, 0, create_color(100, 90, 40))
    set_color(original, 3, 0, create_color(252, 255, 250))
    set_color(original, 4, 0, create_color(0, 0, 0))

    expected = create_image(5, 1)
    set_color(expected, 0, 0, create_color(10, 15, 20))
    set_color(expected, 1, 0, create_color(80, 210, 21))
    set_color(expected, 2, 0, create_color(100, 90, 40))
    set_color(expected, 3, 0, create_color(252, 255, 250))
    set_color(expected, 4, 0, create_color(0, 0, 0))
    edge = detect_edges(original, 2)
    for x, y, ref_color in edge:
        check_equal('Checking pixel (' + str(x) + ', '
                    + str(y)+');', ref_color, get_color(expected, x, y))

# Curve drawing Filter Testing Function


def test_draw_curve():
        
        
    image_color = create_color(100,100,100) 
        
    original = create_image(1,6,image_color)
    
    set_color(original,0,2, create_color(255,50,10))
    set_color(original,0,3, create_color(0,0,0))
    set_color(original,0,4, create_color(200,200,200))
    set_color(original,0,5, create_color(100,150,0))
    
    expected = create_image(1,6,image_color)
        
    set_color(expected,0,2, create_color(255,0,0))
    set_color(expected,0,3, create_color(255,0,0))
    set_color(expected,0,4, create_color(255,0,0))
    set_color(expected,0,5, create_color(255,0,0))
        
        
    border_list = [(5,0),(4,8),(1,0)] #Expected borders that draw_curve function will return
           
    returned_tuple = draw_curve(original,"blood",[(5,0),(4,8)]) #Draw curve returns a tuple index 1 is the image, and index 2 are the borders
    curve_image = returned_tuple[0]

    for x,y,col in curve_image:   # col is the Color object for the pixel @ (x,y)
        check_equal("Checking pixel @(" + str(x) + "," + str(y) + ")" , col,get_color(expected,x,y))

# Vertical Flipping Filter Testing Function


def test_flip_vertical() -> None:
    '''test function for the horizontal flip filter.
    >>> test_flip_vertical()
-Khushi Patel (101195547)
-Yasmina Younes (101193167)
    '''
    original = create_image(1, 6)
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 0, 1, create_color(111, 111, 1))
    set_color(original, 0, 2, create_color(2, 2, 2))
    set_color(original, 0, 3, create_color(3, 33, 3))
    set_color(original, 0, 4, create_color(4, 4, 114))
    set_color(original, 0, 5, create_color(5, 5, 5))

    expected = create_image(1, 6)
    set_color(expected, 0, 0, create_color(5, 5, 5))
    set_color(expected, 0, 1, create_color(4, 4, 114))
    set_color(expected, 0, 2, create_color(3, 33, 3))
    set_color(expected, 0, 3, create_color(2, 2, 2))
    set_color(expected, 0, 4, create_color(111, 111, 1))
    set_color(expected, 0, 5, create_color(0, 0, 0))

    image_tested = flip_vertical(original)
    for x, y, col in image_tested:
        check_equal('Checking pixel @(' + str(x) + ', '
                    + str(y) + ')', col, get_color(expected, x, y))

# Horizontal Flipping Filter Testing Function


def test_flip_horizontal() -> None:
    '''test function for the horizontal flip filter.
    >>> test_flip_horizontal()
-Yasmina Younes (101193167)
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
        check_equal('Checking pixel @(' + str(x) + ', ' +
                    str(y) + ')', col, get_color(expected, x, y))

# 2 Main Script ---------------------------------------------------------------


# Three Tone
print("test_three_tone")
test_three_tone()

# Extreme Contrast
print("test_extreme_contrast")
test_extreme_contrast()

# Sepia Tinting
print("test_sepia_filter")
test_sepia_filter()

# Posterizing
print("test_posterizing_filter")
test_posterizing_filter()

# Edge Detection
print("test_detect_edges")
test_detect_edges()

# Curve drawing
print("test_draw_curve")
test_draw_curve()

# Vertical Flipping
print("test_flip_vertical")
test_flip_vertical()

# Horizontal Flipping
print("test_flip_horizontal")
test_flip_horizontal()

