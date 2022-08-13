from Cimpl import *
FILENAME = "p2-original.png"
from point_manipulation import sort_points,  get_x_y_lists 
from math import floor
import numpy as np 

def draw_curve(FILENAME: Image, color: str , points_lst: list):


    """Author: Juan Sanchez
    
    This function creates a curve on an image, this is done after asking the user how many 
    points he or she desires on the curve and creating a line based off of those 
    given points. 
    """
    curve_image = copy(FILENAME)
    r1, g1, b1 = color_picked(color)
    pixel_color = create_color(r1, g1, b1)                
      

image = PIL.Image.open(FILENAME)
width, height = image.size
print("pixel_x:",width, "pixel_y:",height)

n = int(input("How many points would you like to provide? must be greater or equal to 2 "))

point_lst =[]   
for i in range(0, n):
                x = int(input())
                y= int(input()) 
                point_lst += [(x,y)]
print("point_list =",point_lst)


def _take_first(elem: tuple) -> int:
                return elem[0]
                
           
                
def sort_points(point_lst:list) -> list:
                return sorted(point_lst,key=_take_first)

print("The sorted points are:", sorted(point_lst,key=_take_first))

def _interpolation (point_lst: list) :
                if len(point_lst) <=2:
                                _deg = 1 
                else:
                                _deg = 2 
                get_x, get_y = get_x_y_lists(point_lst)
                return np.polyfit(get_x,get_y,_deg)
print( _interpolation (point_lst))
       
                                
"""def _exhaustive_search(max_x: int, polycoeff: list, val: int) -> int:
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
                                                                return floor(guess) 


def _image_border_finding(image_size: list, polycoeff: list) -> list:
                intersections = []
                vert_left = round(np.polyval(polycoeff, 0))
                vert_right = round(np.polyval(polycoeff,image_size[1]-1))  

                horz_top = _exhaustive_search(image_size[1],polycoeff,0) 
                horz_bottom = _exhaustive_search(image_size[1],polycoeff,image_size[0]-1) 

       
                if vert_left < image_size[0] and vert_left >= 0:
                                
                                intersections += [(0,vert_left)]
                if vert_right < image_size[0] and vert_right >= 0:
                                intersections += [(image_size[1],vert_right)]
                if horz_top !=None:
                                
                                intersections += [(horz_top,0)]
                                
                if horz_bottom !=None:
                                intersections += [(horz_bottom,round(np.polyval(polycoeff,horz_bottom)))]
                return sort_points(intersections)


                

                """