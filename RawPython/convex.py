"""
Problem 2: Determine whether a polygon is convex.

Decision rule (exterior angles):
    Walk around the polygon. At each vertex we "turn" by some exterior angle.
    If we add up the SIZE of every turn (ignoring left/right), a convex
    polygon turns exactly 360 degrees in total. A concave polygon has at
    least one turn in the opposite direction, so it must over-turn to get
    back to where it started, and the total ends up greater than 360.
"""

import math


def exterior_angle(a, b, c):
    """
    Return the exterior (turning) angle in degrees at point b,
    when walking from a -> b -> c.

    """
    in_x = b[0] - a[0]
    in_y = b[1] - a[1]

    out_x = c[0] - b[0]
    out_y = c[1] - b[1]

    cross = in_x * out_y - in_y * out_x
    dot = in_x * out_x + in_y * out_y

    return math.degrees(math.atan2(cross, dot))


def is_convex(points):
    """
    Return True if the polygon described by points is convex, otherwise False.

    points is a list of (x, y) coordinates, in order around the polygon.
    """
    n = len(points)
    total_turn = 0

    for i in range(n):
        a = points[i - 1]          # previous point (wraps to the last point)
        b = points[i]              # current point
        c = points[(i + 1) % n]    # next point (wraps to the first point)

        total_turn += abs(exterior_angle(a, b, c))

    return abs(total_turn - 360) < 1e-6
