from Cimpl import *      #  Imports Cimpl library
from unit_testing import check_equal
from T029_P3_filter_three_tone import three_tone

FILENAME = "p2-original.png"    # name of 1st test file used to apply filter upon
FILENAME2 = "riveter.jpg"   # name of 2nd test file used to apply filter upon

# Author: Zamin Rizvi 
# Student ID: 101203136
# Blue Channel Filter Function and Test Function

def blue_channel(image: Image) -> Image:
    """
    This function is designed to take an Image parameter which is copied and then
    altered to have blue RGB pixel values only. This new image is then returned 
    as an Image type.
    
    >>> original_image = load_image(FILENAME)
    >>> blue = blue_channel(original_image)
    >>> show(blue) 
    
    An image window popup is displayed with the blue filter applied
    
    >>> original_image = load_image(FILENAME2)
    >>> blue = blue_channel(original_image)
    >>> show(blue)
    
    An image window popup is displayed with the blue filter applied

    
    """
    new_image = copy(image)   # A copy is made of the inputted image and bound to new_image
    for pixel in image: 
        x, y, (r, g, b) = pixel   
        blue = create_color(0, 0, b) # creates the RGB color for blue
        set_color(new_image, x, y, blue) # sets the created color into new_image
    return new_image



def test_blue_channel() -> None:
    """
    This test function compares the expected outcome with the blue_channel 
    function outcome, returning whether or not if the test has successfully
    passed.
    
    >>> test_blue_channel()
    >>> Checking pixel (0,0); PASSED
    >>> Checking pixel (1,  0); FAILED: expected Color(red=0, green=128, blue=50), got Color(red=0, green=0, blue=100)
    >>> Checking pixel (2,  0); FAILED: expected Color(red=255, green=185, blue=0), got Color(red=0, green=0, blue=250)
    
    """
    
    reference = create_image(3,1) # A test image is created 
    set_color(reference, 0, 0, create_color(0, 0, 0))  # reference colors are created and set into the test image
    set_color(reference, 1, 0, create_color(20, 100, 100))
    set_color(reference, 2, 0, create_color(250, 155, 250))
    
    expected = create_image(3,1)
    set_color(expected, 0, 0, create_color(0, 0, 0)) # expected colors are created and set into the test image. This is compared with the corresponding reference image.
    set_color(expected, 1, 0, create_color(0, 128, 50))
    set_color(expected, 2, 0, create_color(255, 185, 0))
    
    test_image = blue_channel(reference) # The blue channel function is called and applied to the reference.
    print(' ')
    
    for x, y, ref_color in test_image:
        check_equal('Checking pixel ('+str(x)+',  '+str(y)+');', ref_color, get_color(expected, x, y)) # The pixels within the test image are selected and tested for whether they meet the expected result
        
    
    
print("\nTesting blue_channel():\n")




original_image = load_image(FILENAME)
blue = blue_channel(original_image)
show(blue) 

original_image = load_image(FILENAME2)
blue = blue_channel(original_image)
show(blue)


test_blue_channel()
