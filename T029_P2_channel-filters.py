# T029
# Authors: Yasmina Younes (101193167), Khushi Patel (101195547), Juan Sanchez (101202430), Zamin Rizvi (101203136)

# imports
from Cimpl import *

# image filters


def green_channel(image: Image) -> Image:
    """
    returns a green copy of the passed image.
    >>>image=load_image(choose_file())
    >>>green_picture=green_channel(image)
    >>>show(green_picture)
-Yasmina Younes
    """
    green_picture = copy(image)
    for x, y, (r, g, b) in image:
        green_filter = create_color(0, g, 0)
        set_color(green_picture, x, y, green_filter)
    return green_picture


def blue_channel(image: Image) -> Image:
    """
    This function is designed to take an image which is altered to have the blue pixel of the RGB values only. The new image is then returned.
    >>> original_image = load_image(choose_file())
    >>> blue = blue_channel(original_image)
    >>> show(blue) 
    An image window popup is displayed with the blue filter applied
-Zamin Rizvi
    """
    new_image = copy(image)   # A copy is made of the inputted image and bound to new_image
    for pixel in image:
        x, y, (r, g, b) = pixel
        blue = create_color(0, 0, b)  # creates the RGB color for blue
        # sets the created color into new_image
        set_color(new_image, x, y, blue)
    return new_image


def red_channel(image: Image):
    """ This function takes an image and makes a copy of the image and puts a red filter on it. The image is not destroyed but copied and adjusted.
    >>>blank_image = load_image(choose_file())
    >>>red = red_channel(blank_image)
    >>>show(red)
-Juan Sanchez
    """
    red_image = copy(image)
    for pixel in red_image:
        x, y, (r, g, b) = pixel
        red_filter = create_color(r, 0, 0)
        set_color(red_image, x, y, red_filter)
    return red_image


def combine(red_image: Image, blue_image: Image, green_image: Image) -> Image:
    """
    returns the combined red pixels from the passed red image, blue pixels from the blue image and the green pixels from the green image.
    >>> red_image = load_image(choose_file())
    >>> green_image = load_image(choose_file())
    >>> blue_image = load_image(choose_file())
    >>> combined = combine(red_image,green_image,blue_image)
-Khushi Patel 
    """
    new_red = copy(red_image)
    new_green = copy(green_image)
    new_blue = copy(blue_image)
    new_image = copy(red_image)

    for pixel in red_image:
        x, y, (r, b, g) = pixel
        red = get_color(new_red, x, y)
        green = get_color(new_green, x, y)
        blue = get_color(new_blue, x, y)
        combine_image = create_color(red[0], green[1], blue[2])
        set_color(new_image, x, y, combine_image)
    return new_image


# Test functions

# Green Filter
image = load_image(choose_file())
green_picture = green_channel(image)
show(green_picture)

# Blue Filter
original_image = load_image(choose_file())
blue = blue_channel(original_image)
show(blue)

# Red Filter
blank_image = load_image(choose_file())
red = red_channel(blank_image)
show(red)

# Combine Filter
red_image = load_image(choose_file())
green_image = load_image(choose_file())
blue_image = load_image(choose_file())
combined = combine(red_image, blue_image, green_image)
show(combined)
