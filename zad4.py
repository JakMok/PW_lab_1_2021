def midpoint(point1, point2):
    x = (point1[0] + point2[0]) / 2
    y = (point1[1] + point2[1]) / 2
    return x, y


print(midpoint((1, 1), (3, 3)))
print(midpoint((1, 0), (0, 3)))
