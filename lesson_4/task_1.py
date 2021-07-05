def velo(x, y):
    i = 1
    while x < y:
        x *= 1.1
        i += 1
    return i
x1 = int(input ())
y2 = int(input())
print(velo(x1, y2))
