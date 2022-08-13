from Cimpl import *       #  Imports Cimpl library
FILENAME = "p2-original.png" # name of 1st test file used to apply filter upon
FILENAME2 = "riveter.jpg"   # name of 2nd test file used to apply filter upon


def extreme_contrast(image: Image) -> Image: 
    """
    Author: Zamin Rizvi
    
    This function is designed to take an image parameter and then copied. The
    copied image has it's RGB values altered in order to return an Image that
    has an extreme contrast. If the RGB component is less than 127, the component
    is changed to 0. If the component is inbetween 128 and 255, it is changed to
    255, returning an image of extreme contrast.
    
    >>> original_image = load_image(FILENAME)
    >>> contrast = extreme_contrast(original_image)
    >>> show(contrast) 
    
    An image window popup is displayed with the contrast filter applied
    
    >>> original_image = load_image(FILENAME2)
    >>> contrast = extreme_contrast(original_image)
    >>> show(contrast) 
    
    An image window popup is displayed with the contrast filter applied
    
    """
    new_image = copy(image)    # The original image is copied and assigned to new_image
    for pixel in image:
        x, y, (r, g, b) = pixel # The RGB values of the image passed into the function
        
        if r <= 127:  
            r = 0
        else:
            r = 255
        if g <= 127:
            g = 0
        else:
            g = 255
        if b <= 127:
            b = 0
        else:
            b = 255 
        set_color(new_image, x, y, create_color(r, g, b)) # After analyzing each pixel, a new color is created and set
    
    return new_image


original_image = load_image(FILENAME)
contrast = extreme_contrast(original_image)
show(contrast) 

