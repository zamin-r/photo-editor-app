
# Author: Zamin Rizvi 101203136

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