def turtle(coord, direction):
    bias = yield coord
    while bias:
        if bias == "l":
            if direction == 3:
                direction = 0
            else:
                direction += 1
        elif bias == "r":
            if direction == 0:
                direction = 3
            else:
                direction -= 1
        else:
            buf = list(coord)
            if direction == 0:
                buf[0] += 1
            elif direction == 1:
                buf[1] += 1
            elif direction == 2:
                buf[0] -= 1
            else:
                buf[1] -= 1
            coord = tuple(buf)
        bias = yield coord