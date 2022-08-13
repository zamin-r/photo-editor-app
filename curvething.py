#Import relevant libraries
from Cimpl import *
from simple_Cimpl_filters import grayscale
from point_manipulation import sort_points,  get_x_y_lists #import useful libraries for sorting
from math import floor
import numpy as np #for interpolation





def draw_curve(image: Image, color:str, pointList: list) -> (Image, list):
    """
    Author: Adnan Hafeez
    Takes an PNG and a colour name as a string parameter. Requires a list of points as a parameter or user input.
    Returns a copy of the original image with a line draw ontop of the image given the input colour and a polynomial
    fitted to the points provided by the user.
    >>> image = load_image(choose_file())
    >>> output = draw_curve(image, "lemon", pointList=None)
    >>> print(output[1])
    >>> show(output[0])
    Author: Adnan Hafeez
    """
    img_height = get_height(image)
    img_width = get_width(image)

    def _pick_color(colour:str) -> tuple:
        """
        Simple colour picking function, takes in a string name for the colour and returns a tuple of the RGB values of the
        colour.
        >>>_pick_color("blood")
        >>> (255,0,0)
        >>>_pick_color("green")
        >>> (0,255,0)
        >>>_pick_color("blacj")
        >>> (0,0,0)
        Author: Adnan Hafeez
        """
        color_lst = [("black",0,0,0),("white", 255,255,255),
                     ("blood",255,0,0), ("green",0,255,0),
                     ("blue",0,0,255), ("lemon",255, 255,0),
                     ("aqua",0,255,255),("pink",255,0,255),
                     ("gray",128,128,128)]
        for i in color_lst:
            if i[0] == colour:
                return (i[1],i[2],i[3])

    def _request_points(numPoints) -> list:
        """Interactively request points from the user if not inputted in the original function call.
        Return the points sorted in ascending order as a list.
        >>> _request_points(2) #inputs (1,1) and (2,2)
        >>> [(1,1), (2,2)]
        >>> _request_points(3) #inputs (1,1) and (2,2) and (3,4)
        >>> [(1,1), (2,2),(3,4)]
        >>> _request_points(2) #inputs (1,1) and (2,2) and (4,5)
        >>> [(1,1), (2,2),(4,5)]
        Author: Adnan Hafeez
        """
        point_list = []
        for i in range(numPoints):
            user_x_input = input("Please enter the x-coordinates of your point #({0}): ".format(i+1))
            user_y_input = input("Please enter the y-coordinates of your point #({0}): ".format(i+1))
            point_list.append((int(user_x_input),int(user_y_input)))
        return sort_points(point_list) #return point listed sorted in ascending order

    def _interpolation(points: list) -> list:
        """
        Performs a 1 degree polynomial fit if the number of points submitted by the user is 2, and a quadratic fit 
        if points are greater than 2.
        >>> _interpolation([(1,2),(3,4)])
        >>> [1. 1.]
        >>> _interpolation([(12, 102), (14, 123), (160, 210)]
        >>> [ -0.06691966  12.23991114 -35.24250278]
        >>> _interpolation([(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)])
        >>> [2.92038426e-17 1.00000000e+00 1.00000000e+00]
        Author: Adnan Hafeez
        """""

        if len(points) <=2:
            _deg = 1
        else:
            _deg = 2
        get_x, get_y = get_x_y_lists(points)
        return np.polyfit(get_x,get_y,_deg)

    def _exhaustive_search(max_x: int, polycoeff: list, val: int) -> int:
        """Solves f(x)-val = 0 for x between 0 and max_x where polycoeff contains the coefficients of f,
        using EPSILON = 1. Returns None if there is no solution between the bounds.
        >>> _exhaustive_search(640,[2.92038426e-17 1.00000000e+00 1.00000000e+00],0)
        >>> None
        >>> _exhaustive_search(640,[2.92038426e-17 1.00000000e+00 1.00000000e+00],480)
        >>> 477
        >>> _exhaustive_search(640,[0.33444816 99.66555184],480)
        >>> None
        Author: Adnan Hafeez
        """
        EPSILON = 1
        step = 1
        guess = 0
        if len(polycoeff) > 2:
            a,b,c = polycoeff
        else:
            a=0
            b, c = polycoeff
        func_sol = a*guess**2 + b*guess**1 + c - val
        while abs(func_sol) >= EPSILON and guess <= max_x:
            guess += step
            func_sol = a*guess**2 + b*guess**1 + c - val
        if guess > max_x:
            return None
        else:
            return floor(guess) #to round down into the image grid

    def _image_border_finding(image_size: list, polycoeff: list) -> list:
        """
        Takes the size of the image and interpolation coefficients of the polynomial function.
        Returns the pixels where the curve intersects the image borders.
        >>> _image_border_finding([640,480],[2.92038426e-17 1.00000000e+00 1.00000000e+00])
        [(0, 1), (477, 478)]
        >>> _image_border_finding([640,480],[ 0.33444816 99.66555184])
        [(0, 100), (640, 313)]
        >>> _image_border_finding([640,480],[[ 1.00000000e+00 -1.38076004e-14]])
        [(0, 0), (0, 0), (479, 479)]
        Author: Adnan Hafeez
        """
        #image_size[0] = image height
        #image_size[1] = image width
        intersections = []
        #check to see if crossing vertical border
        vert_left = round(np.polyval(polycoeff, 0)) #this is y value at x = 0
        vert_right = round(np.polyval(polycoeff,image_size[1]-1))  #this is y value at x = max

        horz_top = _exhaustive_search(image_size[1],polycoeff,0) #to find x we need to interpolate
        horz_bottom = _exhaustive_search(image_size[1],polycoeff,image_size[0]-1) #to find x we need to interpolate

        #these if statements are testing for the vertical bounds
        if vert_left < image_size[0] and vert_left >= 0:
            intersections += [(0,vert_left)]
        if vert_right < image_size[0] and vert_right >= 0:
            intersections += [(image_size[1],vert_right)]
        if horz_top !=None:
            intersections += [(horz_top,0)]
        if horz_bottom !=None:
            intersections += [(horz_bottom,round(np.polyval(polycoeff,horz_bottom)))]
        return sort_points(intersections)


    img_copy = copy(image)
    print("Image size (height, width)",(get_height(img_copy), get_width(img_copy)))
    if pointList == None:
        numPoints = int(input("How many numbers? (Must be greater than or equal to 2): "))
        point_list = _request_points(numPoints)
        func_coeff = _interpolation(point_list)
        point_list_border = (_image_border_finding([img_height,img_width],func_coeff))
    else:
        point_list = sort_points(pointList)
        func_coeff = _interpolation(point_list)
        point_list_border = (_image_border_finding([img_height,img_width],func_coeff))


    #draw line
    for x in range(img_width-1):
        if np.polyval(func_coeff,x) < img_height:
            y_line = floor(np.polyval(func_coeff,x))
            for y in range(y_line-4, y_line+4):
                if y>=0 and y<img_height:
                    set_color(img_copy, x,y, create_color(_pick_color(color)[0],_pick_color(color)[1],_pick_color(color)[2]))

    return (img_copy, point_list_border)


if __name__ == "__main__":
    image = load_image(choose_file())
    new_image = extreme_contrast(image)
    show(new_image)
    
    posterized_image = posterize(image)
    show(posterized_image)    

    show(sepia_filter(image))

    three_tone_image = three_tone(image,"lemon","blood","black")
    show(three_tone_image)
    
    h_flipped_image = flip_horizontal(image)
    show(h_flipped_image)    

    #file = load_image(choose_file())
    show(flip_vertical(image))
    
    new_image = detect_edges(image,8)
    show(new_image)       
    
    output = draw_curve(image, "lemon", pointList=None)
    print(output[1])
    show(output[0])    
    
    
    
