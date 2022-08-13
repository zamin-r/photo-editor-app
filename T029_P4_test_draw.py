from Cimpl import*
from unit_testing import check_equal
from T029_image_filters import draw_curve

def test_draw_curve():
        
        
    image_color = create_color(100,100,100) 
        
    original = create_image(1,6,image_color)
    
    set_color(original,0,2, create_color(255,50,10))
    set_color(original,0,3, create_color(0,0,0))
    set_color(original,0,4, create_color(200,200,200))
    set_color(original,0,5, create_color(100,150,0))
    
    expected = create_image(1,6,image_color)
        
    set_color(expected,0,2, create_color(255,0,0))
    set_color(expected,0,3, create_color(255,0,0))
    set_color(expected,0,4, create_color(255,0,0))
    set_color(expected,0,5, create_color(255,0,0))
        
                   
    returned_tuple = draw_curve(original,"blood",[(5,0),(4,8)]) 
    curve_image = returned_tuple[0]

    for x,y,col in curve_image:   
        check_equal("Checking pixel @(" + str(x) + "," + str(y) + ")" , col,get_color(expected,x,y))



test_draw_curve()

