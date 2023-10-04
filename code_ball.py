import math

def degree(a: float, t: float, r: float, V: float) -> float:
    """Calculating the angular displacement

    Args:
        a (float): acceleration
        t (float): time
        r (float): radius
        V (float): speed

    Returns:
        float: the angular displacement
    """
    S = V * t + (a * t ** 2) / 2
    C = 2 * math.pi * r
    radians = S / C
    degrees = math.degrees(radians) # degrees = math.degrees(radians).__round__
    return degrees

# a = 10
# t = 100
# r = 2
# V = 1000
# result = degree(a, t, r, V)
# print(result)
