def distance_between(point1, point2):
    return (abs(((point2[0]-point1[0])**2)+((point2[1]-point1[1])**2))**(1/2),abs(point2[0]-point1[0]),abs(point2[1]-point1[1])) 
def collision(obj1, obj2):
    obj_1_top_left = (obj1.rect.x, obj1.rect.y)
    obj_1_top_right = (obj1.rect.x+obj1.rect.w, obj1.rect.y)
    obj_1_bottom_left = (obj1.rect.x, obj1.rect.y+obj1.rect.h)
    obj_1_bottom_right = (obj1.rect.x+obj1.rect.w, obj1.rect.y+obj1.rect.h)
    obj_2_top_left = (obj2.rect.x, obj2.rect.y)
    obj_2_top_right = (obj2.rect.x+obj2.rect.w, obj2.rect.y)
    obj_2_bottom_left = (obj2.rect.x, obj2.rect.y+obj2.rect.h)
    obj_2_bottom_right = (obj2.rect.x+obj2.rect.w, obj2.rect.y+obj2.rect.h)
    if (obj1.rect.x < obj2.rect.x + obj2.rect.w or obj1.rect.x + obj1.rect.w > obj2.rect.x) and (obj1.rect.y < obj2.rect.y + obj2.rect.h or obj1.rect.y + obj1.rect.h > obj2.rect.y):
        distance_right_top = distance_between(obj_1_top_right,obj_1_bottom_left)
        distance_left_top = distance_between(obj_1_top_left,obj_1_bottom_right)
        distance_right_bottom = distance_between(obj_1_bottom_right,obj_1_top_left)
        distance_right_bottom = distance_between(obj_1_bottom_right,obj_1_top_left)
    #find shortest distance between two corners
    #get longest side of overlapping area
    #move in opposite direction of overlapping side