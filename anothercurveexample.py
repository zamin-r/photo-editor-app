

def test_draw_curve():
    """
    draw_curve function is tested
    
    >>> test_draw_curve()    
    """
        
    color_image = create_color(100, 100, 100) 
        
    original = create_image(6, 1, color_image) 
    
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 1, 0, create_color(100, 60, 20))
    set_color(original, 2, 0, create_color(104, 104, 104))
    set_color(original, 3, 0, create_color(255, 205, 140))
    set_color(original, 4, 0, create_color(20, 205, 140))
    set_color(original, 5, 0, create_color(10, 15, 50))
    
            
    expected = create_image(6, 1, color_image) 
        
    set_color(expected, 0, 0, create_color(10, 15, 20))
    set_color(expected, 1, 0, create_color(80, 210, 21))
    set_color(expected, 2, 0, create_color(100, 90, 40))
    set_color(expected, 3, 0, create_color(252, 255, 250))
    set_color(expected, 4, 0, create_color(0, 0, 0))
    set_color(expected, 5, 0, create_color(10, 15, 50))
    
        
    border = [(5,0),(2,0),(1,5)] 
    border_tuple = draw_curve(original,[(4,0),(2,0)]) 
    image = border_tuple[0]
    border_image = border_tuple[1]
    for x , y, col in image:   
        check_equal("Checking pixel @(" + str(x) + "," + str(y) + ")" , col,get_color(expected,x,y))
    for i in range(len(border)):
        check_equal("Checking border No." +str(i+1)+ " @ x-coordinate:", border[i][0], border_image[i][0])
