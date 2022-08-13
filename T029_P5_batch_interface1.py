#Team: T029
#Zamin Ritvi (101203136)
#Khushi Patel (101195547)

#Imports 
from T029_image_filters import *
from Cimpl import *

#Batch file function


def batch_ui(filename: str) -> None:
 
    """
    Returns an image with the filters applied that are in the batch file. The user
    input file is passed through this function from which the filters are
    applied to manipulate the image within the file. The results are saved 
    within the same folder.
        

    >>> miss_sullivan.jpg test1.jpg 3 X P
    >>> miss_sullivan.jpg test2.jpg V H

    """    
    
    batch_file = open(filename, "r")   # User inputted file is opened
    for line in batch_file:
        new_list = []         
        line_strip = line.strip()
        line_split = line_strip.split()       
        for word in line_split:
            new_list += [word]    
        imagefile = load_image(new_list[0])       # Image is loaded to a list
        for symbol in range(2, len(new_list)): # Allows the function to only select for the filter variables in the file
            imagefile = batch_filters(imagefile, new_list[symbol])  # batch_filters function is applied to the loaded image
        save_as(imagefile, new_list[1])
    batch_file.close()
    new_list = list(line_split)
    

def batch_filters(image: Image, filters: str) -> Image:
    """
    Function executes the functions that the user has called for when the
    batch_ui function calls it to apply the image filters required.
    
    """
    new_image = image
    
    if filters == '3':
        new_image = three_tone((image), 'blood', 'lemon', 'gray') 
    elif filters == 'X':
        new_image = extreme_contrast(image)
    elif filters == 'T':
        new_image = sepia(image)
    elif filters == 'P':
        new_image = posterize(image)
    elif filters == 'H':
        new_image = flip_horizontal(image)
    elif filters == 'V':
        new_image = flip_vertical(image)
    elif filters == 'E':
        new_image = detect_edges(image, 15)
                                 
    return new_image     
    

batch_ui(input("Enter a filename: "))


