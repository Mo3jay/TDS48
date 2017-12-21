import math

class Point():
    def __init__(self, x, y, z=100):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "X: " + str(self.x) + ", Y: " + str(self.y)

def calc_dist(x1, x2, y1, y2):
    x_pt = (x2 - x1) ** 2 
    y_pt = (y2 - y1) ** 2
    return math.sqrt(x_pt + y_pt)

def calc_ang(a, b, c):
    ang = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))
    return math.degrees(ang)

def stakeout(setup):
    oc_fs = calc_dist(setup["occupy"].x, setup["foresite"].x, setup["occupy"].y, setup["foresite"].y)
    oc_bs = calc_dist(setup["occupy"].x, setup["backsite"].x, setup["occupy"].y, setup["backsite"].y)
    bs_fs = calc_dist(setup["backsite"].x, setup["foresite"].x, setup["backsite"].y, setup["foresite"].y)
    dist = oc_fs
    ang = calc_ang(bs_fs, oc_bs, oc_fs)
    return {"distance": dist, "angle": ang}

points = [
    Point(5000, 5000),
    Point(4678, 3290),
    Point(6234, 3950),
    Point(1337, 5093),
    Point(3209, 1205),
]

def display():
    n = 1
    for point in points:
        print(n, "-", point)
        n = n + 1

def assign():
    choice1 = input("select occupy: ")
    choice2 = input("select backsite: ")
    choice3 = input("select forsite: ")
    setup = {
        "occupy": points[int(choice1) - 1],
        "backsite": points[int(choice2) - 1],
        "foresite": points[int(choice3) - 1]
    }
    return setup

    

display()
setup = assign()
print(stakeout(setup))
