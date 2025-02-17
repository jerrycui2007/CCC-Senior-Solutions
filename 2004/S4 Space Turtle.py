# https://dmoj.ca/problem/ccc04s4
import math


def calculate_distance(x1, y1, z1, x2, y2, z2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)


def minimal_segment_distance(ax, ay, az, bx, by, bz, px, py, pz):
    abx = bx - ax
    aby = by - ay
    abz = bz - az

    apx = px - ax
    apy = py - ay
    apz = pz - az

    dot_ab_ap = abx * apx + aby * apy + abz * apz

    if abx == 0 and aby == 0 and abz == 0:
        return calculate_distance(ax, ay, az, px, py, pz)

    len_ab_sq = abx**2 + aby**2 + abz**2
    t = dot_ab_ap / len_ab_sq
    t_clamped = max(0.0, min(t, 1.0))

    closest_x = ax + t_clamped * abx
    closest_y = ay + t_clamped * aby
    closest_z = az + t_clamped * abz

    return calculate_distance(closest_x, closest_y, closest_z, px, py, pz)


x, y, z = map(int, input().split())
planet_x, planet_y, planet_z = map(int, input().split())

forward = [1, 0, 0]
left = [0, 1, 0]
up = [0, 0, 1]

smallest_distance = calculate_distance(x, y, z, planet_x, planet_y, planet_z)

while True:
    distance, turn = input().split()
    distance = int(distance)

    start_x, start_y, start_z = x, y, z
    end_x = start_x + distance * forward[0]
    end_y = start_y + distance * forward[1]
    end_z = start_z + distance * forward[2]

    min_dist = minimal_segment_distance(start_x, start_y, start_z, end_x, end_y, end_z, planet_x, planet_y, planet_z)
    if min_dist < smallest_distance:
        smallest_distance = min_dist

    x, y, z = end_x, end_y, end_z

    if turn == "E":
        break

    if turn == "L":
        forward, left = left, [-forward[0], -forward[1], -forward[2]]
    elif turn == "R":
        forward, left = [-left[0], -left[1], -left[2]], forward
    elif turn == "U":
        forward, up = up, [-forward[0], -forward[1], -forward[2]]
    elif turn == "D":
        forward, up = [-up[0], -up[1], -up[2]], forward

print(f"{smallest_distance:.2f}")