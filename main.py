import math

class Point():
    def __init__(self, x, y, z=100):
        self.x = x
        self.y = y
        self.z = z

def calc_dist(x1, x2, y1, y2):
    x_pt = (x2 - x1) ** 2 
    y_pt = (y2 - y1) ** 2
    return math.sqrt(x_pt + y_pt)

def calc_ang(a, b, c):
    ang = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))
    return math.degrees(ang)

northing = input("enter northing coord: ")
easting = input("enter easting coord: ")

occupy = Point(5000, 5000, 100)
backsite = Point(4500, 4500, 90)
foresite = Point(int(northing), int(easting))

c_dist = calc_dist(occupy.x, foresite.x, occupy.y, foresite.y)
b_dist = calc_dist(occupy.x, backsite.x, occupy.y, backsite.y)
a_dist = calc_dist(backsite.x, foresite.x, backsite.y, foresite.y)

print(c_dist)
print(calc_ang(a_dist, b_dist, c_dist))
