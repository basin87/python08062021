def velo():
    x = int(input())
    y = int(input())
    i = 1
    while x < y:
        x *= 1.1
        i += 1
    return i
print(velo())