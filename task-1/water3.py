def initial_state():
    return (8, 0, 0)

def is_goal(s):
    return s[0] == 4, s[1] == 4

def successors(s):
    x, y, z = s

     # Try to empty one bottle
    if x > 0:
        yield ((0, y, z), x)
    if y > 0:
        yield ((x, 0, z), y)
    if z > 0:
        yield ((x, y, 0), z)
    # Try to fill up one bottle
    if x < 8:
        yield ((8, y, z), 8-x)
    if y < 5:
        yield ((x, 5, z), 5-y)
    if z < 3:
        yield ((x, y, 3), 3-z)
    # Try to pour from one to another
    t = 5-y
    if x > 0 and t > 0:
        if x > t:
            yield ((x-t, 5, z), t)
        else:
            yield ((0, y+x, z), x) 
    t = 3-x
    if y > 0 and t > 0:
        if y > t:
            yield ((3, y-t, z), t)
        else:
            yield ((x+y, 0, z), y)  
    t = 8-x
    if z > 0 and t > 0:
        if z > t:
            yield ((8, y, z-t), t)
        else:
            yield ((x+t, y, 0), z)
    t = 3-x
    if z > 0 and t > 0:
        if z > t:
            yield ((8, y, z-t), t)
        else:
            yield ((x+t, y, 0), z)
    t = 8-x
    if y > 0 and t > 0:
        if y > t:
            yield ((8, y-t, z), t)
        else:
            yield ((x+y, 0, z), y) 
    t = 5-y
    if z > 0 and t > 0:
        if z > t:
            yield ((8, y, z-t), t)
        else:
            yield ((x, y+t, 0), z)
