def points(win, draw, loss) -> int:
    return win*3 + draw*2 + loss*1


print(points(4, 1, 1))