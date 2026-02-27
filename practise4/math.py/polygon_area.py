import math
def polygon_area(n_sides, side_length):
    return (n_sides * side_length ** 2) / (4 * math.tan(math.pi / n_sides))