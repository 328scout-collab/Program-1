"""
Test cases for is_convex.  Run with:  python test_convex.py
"""

from convex import is_convex

# (name, points, expected answer)
test_cases = [
    # ---------- Convex shapes ----------
    ("Triangle",                    [(0, 0), (4, 0), (2, 3)],                       True),
    ("Square (counter-clockwise)",  [(0, 0), (2, 0), (2, 2), (0, 2)],               True),
    ("Square (clockwise)",          [(0, 0), (0, 2), (2, 2), (2, 0)],               True),
    ("Rectangle",                   [(0, 0), (5, 0), (5, 1), (0, 1)],               True),
    ("Regular pentagon",            [(0, 2), (-1.9, 0.62), (-1.18, -1.62),
                                     (1.18, -1.62), (1.9, 0.62)],                   True),
    ("Hexagon",                     [(1, 0), (3, 0), (4, 2), (3, 4), (1, 4), (0, 2)], True),
    ("Negative coordinates",        [(-5, -5), (-1, -5), (-1, -1), (-5, -1)],       True),
    ("Very thin triangle",          [(0, 0), (100, 0), (50, 0.01)],                 True),
    ("Square with point mid-edge",  [(0, 0), (1, 0), (2, 0), (2, 2), (0, 2)],       True),

    # ---------- Concave shapes ----------
    ("Arrowhead / dart",            [(0, 0), (2, 1), (4, 0), (2, 4)],               False),
    ("L-shape",                     [(0, 0), (2, 0), (2, 1), (1, 1), (1, 2), (0, 2)], False),
    ("L-shape (clockwise)",         [(0, 2), (1, 2), (1, 1), (2, 1), (2, 0), (0, 0)], False),
    ("Star",                        [(0, 3), (1, 1), (3, 1), (1.5, -0.5), (2, -3),
                                     (0, -1.5), (-2, -3), (-1.5, -0.5), (-3, 1), (-1, 1)], False),
    ("Square with one dent",        [(0, 0), (4, 0), (4, 4), (2, 3), (0, 4)],       False),
    ("U-shape",                     [(0, 0), (3, 0), (3, 3), (2, 3), (2, 1),
                                     (1, 1), (1, 3), (0, 3)],                       False),
    ("Barely concave",              [(0, 0), (4, 0), (4, 4), (2, 3.99), (0, 4)],    False),
]

passed = 0
print(f"{'Shape':<30} {'Expected':<10} {'Got':<10} Result")
print("-" * 60)

for name, points, expected in test_cases:
    result = is_convex(points)
    status = "PASS" if result == expected else "FAIL"
    if result == expected:
        passed += 1
    print(f"{name:<30} {str(expected):<10} {str(result):<10} {status}")

print("-" * 60)
print(f"{passed}/{len(test_cases)} tests passed")
