# T029
# Milestone 2
# Date of submission: June 9 2021
# Authors:
# Yasmina Younes (101193167)
# Khushi Patel (101195547)
# Juan Sanchez (101202430)
# Zamin Rizvi (101203136)


# 0 Imports ---------------------------------------------------------------

from Cimpl import *
from unit_testing import check_equal
from simple_Cimpl_filters import *
from point_manipulation import sort_points, get_x_y_lists
import numpy as np
from math import floor


# 1 Filters ---------------------------------------------------------------

# Three Tone Filter
def three_tone(image: Image, color_1: str, color_2: str, color_3: str) -> Image:
    """returns a three toned copy of the passed image based on the three colors passed into the function.
    >>> original_image = load_image(choose_file())
    >>> new_image = three_tone(original_image, "white", "black", "lemon") #random 3 colors
    >>> show(new_image)
-Yasmina Younes (101193167)
    """
    new_image = copy(image)
    color = ["black", "white", "blood", "green",
             "blue", "lemon", "cyan", "magenta", "gray"]
    colors_code = [(0, 0, 0), (255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0),
                   (0, 255, 255), (255, 0, 255), (128, 128, 128)]
    j = 0
    while j in range(len(color)):
        if color_1 == color[j]:
            colors_code_1 = colors_code[j]
            j += 1
        else:
            j += 1
    j = 0
    while j in range(len(color)):
        if color_2 == color[j]:
            colors_code_2 = colors_code[j]
            j += 1
        else:
            j += 1
    j = 0
    while j in range(len(color)):
        if color_3 == color[j]:
            colors_code_3 = colors_code[j]
            j += 1
        else:
            j += 1

    for pixel in image:
        x, y, (r, g, b) = pixel
        if 0 <= ((r + g + b) / 3) <= 84:
            new_color_1 = create_color(
                colors_code_1[0], colors_code_1[1], colors_code_1[2])
            set_color(new_image, x, y, new_color_1)

    for pixel in image:
        x, y, (r, g, b) = pixel
        if 85 <= ((r + g + b) / 3) <= 170:
            new_color_2 = create_color(
                colors_code_2[0], colors_code_2[1], colors_code_2[2])
            set_color(new_image, x, y, new_color_2)

    for pixel in image:
        x, y, (r, g, b) = pixel
        if 171 <= ((r + g + b) / 3) <= 255:
            new_color_3 = create_color(
                colors_code_3[0], colors_code_3[1], colors_code_3[2])
            set_color(new_image, x, y, new_color_3)

    return new_image


# Extreme Contrast Filter
def extreme_contrast(image: Image) -> Image:
    """
    returns an extreme contrasted copy of the passed image.
    >>> original_image = load_image(choose_file())
    >>> contrast = extreme_contrast(original_image)
    >>> show(contrast) 
-Zamin Rizvi (101203136)
-Yasmina Younes (101193167)
    """
    new_image = copy(
        image)    # The original image is copied and assigned to new_image
    for pixel in image:
        # The RGB values of the image passed into the function
        x, y, (r, g, b) = pixel
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
        # After analyzing each pixel, a new color is created and set
        set_color(new_image, x, y, create_color(r, g, b))
    return new_image

# Sepia Tinting Filter


def sepia(image: Image) -> Image:
    """
    returns a copy of the passed image with a sepia filter over it.
    >>> image = load_image(choose_file())
    >>> sepia_filter(image)
-Khushi Patel (101195547)
-Yasmina Younes (101193167)
    """
    new_picture = copy(image)
    sepia_image = grayscale(new_picture)
    for x, y, (r, g, b) in sepia_image:
        if b < 63:
            dark_grey = create_color(r * (1.1), g, b * (0.9))
            set_color(sepia_image, x, y, dark_grey)

        elif 63 <= b < 191:
            gray = create_color(r * (1.15), g, b * (0.85))
            set_color(sepia_image, x, y, gray)

        else:
            light_gray = create_color(r * (1.08), g, b * (0.93))
            set_color(sepia_image, x, y, light_gray)
    return sepia_image

# Posterizing Filter


def _adjust_component(x: int) -> int:  # internal use function
    """
    Returns the midpoint value of the passed component based on the quadrant in which it lies.
-Yasmina Younes (110193167)
    """
    if 0 <= x <= 63:
        x = 31
    elif 64 <= x <= 127:
        x = 95
    elif 128 <= x <= 191:
        x = 159
    else:
        x = 233
    return x


def posterize(image: Image) -> Image:
    """
    returns a posterized copy of the passed image.
    >>> image = load_image(choose_file())
    >>> new_image = posterize(image)
    >>> show(new_image)
-Yasmina Younes (101193167)
    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:
        new_r = _adjust_component(r)
        new_g = _adjust_component(g)
        new_b = _adjust_component(b)
        posterized_colour = create_color(new_r, new_g, new_b)
        set_color(new_image, x, y, posterized_colour)
    return new_image

# Edge Detection Filter


def detect_edges(image: Image, threshold) -> Image:
    """returns a black and white edge detected copy of the passed image depending on the passed threshold.
    >>> original_image = load_image(choose_file())
    >>> edges = detect_edges(original_image, 5) #5 is a random example of a threshold
    >>> show(edges)
-Zamin Rizvi (101203136)
-Yasmina Younes (101193167)
    """
    new_image = copy(image)
    for y in range(0, get_height(image) - 1):
        for x in range(0, get_width(image) - 1):
            # Top pixels' color is returned and assigned
            (Tpixel_r, Tpixel_g, Tpixel_b) = get_color(image, x, y)
            # Bottom pixels' color is returned and assigned
            (Bpixel_r, Bpixel_g, Bpixel_b) = get_color(image, x, y - 1)

            top = (Tpixel_r + Tpixel_g + Bpixel_b) / \
                3  # The top pixels are averaged
            bottom = (Bpixel_r + Bpixel_g + Bpixel_b) / \
                3  # The bottom pixels are averaged

            # The difference of both the top and bottom are calculated with the abs() function applied
            imagecontrast = abs(top - bottom)

            if threshold < imagecontrast:
                new_color = create_color(0, 0, 0)
                # New color is created with RGB values set to 0, 0, 0
                set_color(new_image, x, y, new_color)
            else:
                # New color is set with RGB values set to 0, 0, 0
                new_color = create_color(255, 255, 255)
                set_color(new_image, x, y, new_color)

        for y in range((get_height(image) - 1), get_height(image)):
            white = create_color(255, 255, 255)
            set_color(new_image, x, y, white)
    return (new_image)


# Curve drawing Filter



# Vertical Flipping Filter


def flip_vertical(image: Image) -> None:
    """
    returns a vertical flip copy of the passed image.
    >>> image = load_image(choose_file())
    >>> copy_image = flip_vertical(image)
    >>> show(copy_image)
-Yasmina Younes (101193167)
    """
    image_height = get_height(image)
    image_width = get_width(image)
    copy_image = copy(image)
    half_height = image_height // 2
    for x in range(0, image_width):
        for y in range(0, half_height):
            bottom_color = get_color(copy_image, x, (image_height - y - 1))
            top_color = get_color(copy_image, x, y)
            set_color(copy_image, x, (image_height - y - 1), top_color)
            set_color(copy_image, x, y, bottom_color)
    return copy_image

# Horizontal Flipping Filter


def flip_horizontal(image: Image):
    """
    returns a horizontal flip copy of the passed image.
    >>> image = load_image(choose_file())
    >>> copy_image = flip_horizontal(image)
    >>> show(copy_image)
-Khushi Patel (101195547)
-Yasmina Younes (101193167)
    """
    new_picture = copy(image)
    w = get_width(image)
    for pixel in image:
        x, y, (r, g, b) = pixel
        new_col = create_color(r, g, b)
        set_color(new_picture, (w - x - 1), y, new_col)
    return new_picture


# 2 Main Script ---------------------------------------------------------------
'''
# Three Tone
original_image = load_image(choose_file())
new_image = three_tone(original_image, "white",
                       "black", "lemon")  # random 3 colors
show(new_image)

# Extreme Contrast
original_image = load_image(choose_file())
contrast = extreme_contrast(original_image)
show(contrast)

# Sepia Tinting
original_image = load_image(choose_file())
image = load_image(choose_file())
show(sepia(image))

# Posterizing
image = load_image(choose_file())
new_image = posterize(image)
show(new_image)

# Edge Detection
original_image = load_image(choose_file())
edges = detect_edges(original_image, 15)
show(edges)

# Curve drawing
image = load_image(choose_file())
x = draw_curve(image, "blood",)
show(x[0])

# Vertical Flipping
image = load_image(choose_file())
copy_image = flip_vertical(image)
show(copy_image)

# Horizontal Flipping
image = load_image(choose_file())
copy_image = flip_horizontal(image)
show(copy_image)
'''
