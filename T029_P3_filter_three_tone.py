from Cimpl import *
FILENAME = "p2-original.png"

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

