def platform_collisions(player, platforms):
    res = []
    for platform in platforms:
        res.append(player_platform_collison(player,platform))
    out = [False, False] #X collide, Y collide
    if "X" in res:
        out[0] = True
    if "Y" in res:
        out[1] = True
    return tuple(out)
def player_platform_collison(player, obj):
    if (player.rect.x < obj.rect.x + obj.rect.w and player.rect.x + player.rect.w > obj.rect.x) and (player.rect.y < obj.rect.y + obj.rect.h and player.rect.y + player.rect.h > obj.rect.y):
        x_offset = (player.rect.x+player.rect.w/2)-(obj.rect.x+obj.rect.w/2)
        y_offset = (player.rect.y+player.rect.h/2)-(obj.rect.y+obj.rect.h/2)
        if abs(x_offset)<obj.rect.w/2+player.rect.w/2 and abs(y_offset)*obj.rect.w<abs(x_offset)*obj.rect.h:
            if x_offset>0:
                player.rect.x = obj.rect.x + obj.rect.w
            else:
                player.rect.x = obj.rect.x - player.rect.w
            return "X"
        elif abs(y_offset)<obj.rect.h/2+player.rect.h/2 and abs(y_offset)*obj.rect.w>abs(x_offset)*obj.rect.h:
            if y_offset>0:
                player.rect.y = obj.rect.y + obj.rect.h
            else:
                player.rect.y = obj.rect.y - player.rect.h
            return "Y"
    return False