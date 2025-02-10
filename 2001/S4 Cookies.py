# https://dmoj.ca/problem/ccc01s4
import random
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius


def midpoint(p1, p2):
    return Point((p1.x + p2.x) / 2, (p1.y + p2.y) / 2)


def distance(p1, p2):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


def is_inside_circle(circle, point):
    return distance(circle.center, point) <= circle.radius


def circle_from_2(a, b):
    return Circle(midpoint(a, b), distance(a, b) / 2)


def get_circle_center(a, b, c):
    bx = b.x - a.x
    by = b.y - a.y
    cx = c.x - a.x
    cy = c.y - a.y

    denominator = bx * cy - by * cx
    if denominator == 0:
        return None  # Colinear points

    numerator_hx = (bx ** 2 + by ** 2) * cy - by * (cx ** 2 + cy ** 2)
    numerator_hy = bx * (cx ** 2 + cy ** 2) - (bx ** 2 + by ** 2) * cx

    Hx = numerator_hx / (2 * denominator)
    Hy = numerator_hy / (2 * denominator)

    return Point(Hx, Hy)


def circle_from_3(a, b, c):
    center = get_circle_center(a, b, c)
    if not center:
        # Handle colinear points by finding the two farthest apart
        max_dist = 0
        farthest_pair = (a, b)
        for pair in [(a, b), (a, c), (b, c)]:
            d = distance(*pair)
            if d > max_dist:
                max_dist = d
                farthest_pair = pair
        return circle_from_2(*farthest_pair)
    center.x += a.x
    center.y += a.y
    return Circle(center, distance(center, a))


def is_valid_circle(circle, points):
    for point in points:
        if not is_inside_circle(circle, point):
            return False
    return True


def trivial_enclosing_circle(points):
    if len(points) == 0:
        return Circle(Point(0, 0), 0)
    if len(points) == 1:
        return Circle(points[0], 0)
    if len(points) == 2:
        return circle_from_2(points[0], points[1])

    # Check all combinations of two points
    for i in range(3):
        for j in range(i + 1, 3):
            circle = circle_from_2(points[i], points[j])
            if is_valid_circle(circle, points):
                return circle

    return circle_from_3(points[0], points[1], points[2])


def minimum_enclosing_circle(enclosed_points, boundary_points):
    if len(enclosed_points) == 0 or len(boundary_points) == 3:
        return trivial_enclosing_circle(boundary_points)

    index = random.randint(0, len(enclosed_points) - 1)
    random_point = enclosed_points[index]
    new_enclosed = [p for i, p in enumerate(enclosed_points) if i != index]

    mec = minimum_enclosing_circle(new_enclosed, boundary_points.copy())

    if is_inside_circle(mec, random_point):
        return mec
    else:
        new_boundary = boundary_points.copy()
        new_boundary.append(random_point)
        return minimum_enclosing_circle(new_enclosed, new_boundary)


number_of_chips = int(input())
chips = []
for _ in range(number_of_chips):
    x, y = map(int, input().split())
    chips.append(Point(x, y))


smallest_circle = minimum_enclosing_circle(chips.copy(), [])
print(smallest_circle.radius * 2)