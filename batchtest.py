from T029_image_filters import *
from Cimpl import *

def batch_analysis(filename: str) -> None:
    """
    returns a list of strings from filename
    """
    
    infile = open(filename, "r")
    word_list_new = []
    for line in infile:
        word_list = line.split()
        for word in word_list:
            if word != '':
                word_list_new += [word]
        load_img = load_image(word_list_new[0])
        for filter in range(len(word_list)-2):
            load_img = filter_array(load_img, word_list[filter+2])
        save_as(load_img, word_list_new[1])
        word_list_new = [] #reset the line to empty
    infile.close()
    # Now build the list of distinct words.
    word_list_new = list(word_list)
    return word_list_new


def filter_array(image: Image, filter_id: str) -> Image:
    """
    returns an image that has been passed through the filters given by the filter_id
    in the order written in the filename.
    
    >>>Enter a filename: sample.txt
    """
    
    if filter_id == "3":
        image = three_tone(image,"aqua","blood","lemon")
    elif filter_id == "X":
        image = extreme_contrast(image)
    elif filter_id == "T":
        image = sepia_filter(image)
    elif filter_id == "P":
        image = posterize(image)
    elif filter_id == "E":
        image = detect_edges(image,15)
    elif filter_id == "V":
        image = flip_vertical(image)
    elif filter_id == "H":
        image = flip_horizontal(image)
        
    return image

command_sequence = batch_analysis(input("Enter a filename: "))
© 2021 GitHub, Inc.