# T029
# Milestone 3
# Interactive UI
# Date of submission: June 12 2021
# Author(s): Yasmina Younes (101193167)

# 0 Imports ---------------------------------------------------------------------
from T029_image_filters import*

supported_commands = ["L", "S", "3", "X", "T", "P", "E", "D", "V", "H", "Q"]

# 1 Functions/Script ---------------------------------------------------------------------

command = ''
p = None


def get_command():
    """Displays the photo editor's user interface and prompts the used to enter one of the valid commands.
-Yasmina Younes (101193167)
    >>> L)oad image  S)ave-as
        3)-tone  X)treme contrast  T)int sepia  P)osterize
        E)dge detect  D)raw curve  V)ertical flip  H)oriztonal flip
        Q)uit

        : 
    """
    command = input(
        "L)oad image  S)ave-as\n3)-tone  X)treme contrast  T)int sepia  P)osterize\nE)dge detect  D)raw curve  V)ertical flip   H)oriztonal flip\nQ)uit\n\n: ")
    return (command.upper())


def execute_command(command):
    """Returns the executed commands -- usually (a) filter(s) from the ones provided in the userinterface over a loaded image.
-Yasmina Younes (101193167)
    """
    image = i
    if command not in supported_commands:
        print('No such command')

    if image == None and command in ["S", "3", "X", "T", "P", "E", "D", "V", "H"]:
        print("No image loaded")
    else:
        if command == "L":
            image = load_image(choose_file())

        if command == "S":
            name = input(
                'What is the file name?\nInput full name (example: JohnDoe.jpg), or return to write new save path\n: ')
            save_as(image, name)

        if command == "3":
            image = three_tone(image, 'blood', 'lemon', 'gray')

        if command == "X":
            image = extreme_contrast(image)

        if command == "T":
            image = sepia(image)

        if command == "P":
            image = posterize(image)

        if command == "E":
            threshold = int(input('input the desired threshold\n: '))
            image = detect_edges(image, threshold)

        if command == "D":
            curve = draw_curve(image, 'cyan',)
            image = curve[0]

        if command == "V":
            image = flip_vertical(image)

        if command == "H":
            image = flip_horizontal(image)

    if image != None and command not in ["S", "Q"]:
        show(image)
    return(image)


while command != 'Q':
    command = get_command()
    i = execute_command(command)

