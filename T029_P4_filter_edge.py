from Cimpl import *       #  Imports Cimpl library
FILENAME = "p2-original.png" # name of 1st test file used to apply filter upon
FILENAME2 = "riveter.jpg"   # name of 2nd test file used to apply filter upon



def detect_edges(image: Image, threshold)-> Image:
    """
    Author: Zamin Rizvi 
    
    This function takes an image input with a variable for threshold. It will 
    return an image that will look like a pencil sketch as the pixels' colors 
    will be changed to black or white.

    
    >>> original_image = load_image(FILENAME)
    >>> edges = detect_edges(original_image, 15)
    >>> show(edges) 

    An image window popup is displayed with the detect_edges filter applied

    
    >>> original_image = load_image(FILENAME2)
    >>> edges = detect_edges(original_image, 2)
    >>> show(edges) 
    
    An image window popup is displayed with the detect_edges filter applied
    
    """  
    
    new_image = copy(image)
    
    for y in range(0, get_height(image) - 1): 
        for x in range(0, get_width(image) - 1):
            
            (Tpixel_r, Tpixel_g, Tpixel_b) = get_color(image, x, y) # Top pixels' color is returned and assigned
            (Bpixel_r, Bpixel_g, Bpixel_b) = get_color(image, x, y - 1) # Bottom pixels' color is returned and assigned
           
            top = (Tpixel_r + Tpixel_g + Bpixel_b)/3 # The top pixels are averaged
            bottom = (Bpixel_r + Bpixel_g + Bpixel_b)/3 # The bottom pixels are averaged
           
            imagecontrast = abs(top - bottom) # The difference of both the top and bottom are calculated with the abs() function applied
           
            if threshold < imagecontrast:
                new_color = create_color(0,0,0)
                set_color(new_image, x, y, new_color) # New color is created with RGB values set to 0, 0, 0
            else:
                new_color = create_color(255,255,255) # New color is set with RGB values set to 0, 0, 0
                set_color(new_image, x, y, new_color)
        
        for y in range((get_height(image) - 1), get_height(image)): 
            white = create_color(255, 255, 255)
            set_color(new_image, x, y, white)
    
    return (new_image)


original_image = load_image(FILENAME)
edges = detect_edges(original_image, 15)
show(edges) 


original_image = load_image(FILENAME2)
edges = detect_edges(original_image, 2)
show(edges) 