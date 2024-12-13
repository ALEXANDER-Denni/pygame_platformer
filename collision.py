def collision(player, obj):
    if (player.rect.x < obj.rect.x + obj.rect.w and player.rect.x + player.rect.w > obj.rect.x) and (player.rect.y < obj.rect.y + obj.rect.h and player.rect.y + player.rect.h > obj.rect.y):
        x_offset = (player.rect.x+player.rect.w/2)-(obj.rect.x+obj.rect.w/2)
        y_offset = (player.rect.y+player.rect.h/2)-(obj.rect.y+obj.rect.h/2)
        if abs(x_offset)<obj.rect.w/2+player.rect.w/2:
            if x_offset>0:
                player.rect.x += obj.rect.w/2 - x_offset + player.rect.w/2
            else:
                player.rect.x += -obj.rect.w/2 - x_offset - player.rect.w/2
        if abs(y_offset)<obj.rect.h/2:
            if y_offset>0:
                player.rect.y += obj.rect.h/2 - x_offset + player.rect.h/2
            else:
                player.rect.y += -obj.rect.h/2 - x_offset - player.rect.h/2
    return True
    #get distance between center of obj1 and sides of obj2
    #the lowest distance is the amount that needs to be moved