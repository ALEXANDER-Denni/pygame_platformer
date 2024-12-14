def platform_collisions(player, platforms):
    x_moves = []
    y_moves = []
    for platform in platforms.sprites():
        colliding = player_platform_collison(player,platform)
        if colliding != False:
            x_moves.append(colliding[0])
            y_moves.append(colliding[1])
    out = [] #X collide, Y collide
    if player.x_velocity >= 0:
        out.append(min(x_moves))
    else:
        out.append(max(x_moves))
    if player.y_velocity >= 0:
        out.append(min(y_moves))
    else:
        out.append(max(y_moves))
    out.append(ground_below(player, platforms))
    return tuple(out)


def moving_platform_push(player, platform):
    if platform.direction == 1:
        if player.rect.x + player.x_velocity < platform.rect.x + platform.rect.w + platform.speed and player.rect.x + player.rect.w + player.x_velocity > platform.rect.x + platform.speed:
            if player.rect.y < platform.rect.y + platform.rect.h and player.rect.y + player.rect.h - 1 > platform.rect.y:
                return True
            if player.rect.y + player.rect.h + 1 > platform.rect.y and player.rect.y < platform.rect.y + platform.rect.h:
                player.push(platform.speed*2) 


def ground_below(player, platforms):
    for obj in platforms:
        if player.rect.y + player.rect.h + player.y_velocity + 1 > obj.rect.y and player.rect.y < obj.rect.y + obj.rect.h and player.rect.x + player.rect.w > obj.rect.x and player.rect.x < obj.rect.x + obj.rect.w:
            return True
    return False


def player_platform_collison(player, obj):
    x_move = 0
    y_move = 0
    if obj.__class__.__name__ == "moving_platform" and (player.x_velocity <= 0) == (obj.direction == 1):
        if moving_platform_push(player, obj):
            player.push(obj.speed + (obj.rect.x + obj.rect.w) - player.rect.x)
            player.x_velocity = 0
    elif (player.rect.x + player.x_velocity< obj.rect.x + obj.rect.w and player.rect.x + player.x_velocity+ player.rect.w > obj.rect.x) and (player.rect.y + player.y_velocity < obj.rect.y + obj.rect.h and player.rect.y + player.y_velocity + player.rect.h > obj.rect.y):
        if player.x_velocity > 0:
            x_move = (obj.rect.x) - (player.rect.x + player.rect.w)
        if player.x_velocity < 0:
            x_move = (obj.rect.x + obj.rect.w) - player.rect.x
        if player.y_velocity < 0:
            y_move = (obj.rect.y + obj.rect.h) - (player.rect.y)
        if player.y_velocity > 0:
            y_move = obj.rect.y - (player.rect.y + player.rect.h)
        return (x_move, y_move)
    return (player.x_velocity, player.y_velocity)
"""x_offset = (player.rect.x+player.rect.w/2)-(obj.rect.x+obj.rect.w/2)
        y_offset = (player.rect.y+player.rect.h/2)-(obj.rect.y+obj.rect.h/2)
        if abs(x_offset)<obj.rect.w/2+player.rect.w/2 and abs(y_offset)*obj.rect.w/2<abs(x_offset)*obj.rect.h/2:
            if x_offset>0:
                player.rect.x = obj.rect.x + obj.rect.w
            else:
                player.rect.x = obj.rect.x - player.rect.w
            return "X"
        elif abs(y_offset)<obj.rect.h/2+player.rect.h/2 and abs(y_offset)*obj.rect.w/2>abs(x_offset)*obj.rect.h/2:
            if y_offset>0:
                player.rect.y = obj.rect.y + obj.rect.h
            else:
                player.rect.y = obj.rect.y - player.rect.h
            return "Y"
    return False"""