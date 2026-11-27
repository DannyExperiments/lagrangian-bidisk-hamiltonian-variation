#!/usr/bin/env python3
"""Check the quartic's gradient at rational corner directions and exact moments."""
from fractions import Fraction as F
from itertools import product
from math import prod


def quartic_monomials():
    """Expand (x₁²+x₂²−y₁²−y₂²)(x₁y₁+x₂y₂)/2."""
    for square in range(4):
        sign = 1 if square < 2 else -1
        for pair in ((0, 2), (1, 3)):
            powers = tuple(2 * (j == square) + (j in pair) for j in range(4))
            yield F(sign, 2), powers


def differentiated_quartic(p, coordinate):
    value = F(0)
    for coeff, powers in quartic_monomials():
        power = powers[coordinate]
        if power:
            value += coeff * power * prod(
                x ** (n - (j == coordinate)) for j, (x, n) in enumerate(zip(p, powers))
            )
    return value


def exact_dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def unit_circle(t):
    return ((1 - t * t) / (1 + t * t), 2 * t / (1 + t * t))


def projected_velocity(x, y, a, b):
    assert exact_dot(x, x) == exact_dot(y, y) == a * a + b * b == 1
    ux = tuple(a * v for v in x)
    uy = tuple(b * v for v in y)
    c = exact_dot(x, y)
    dx1, dx2, dy1, dy2 = (differentiated_quartic(x + y, j) for j in range(4))
    velocity = (dy1, dy2, -dx1, -dx2)
    assert velocity == tuple(-c * v for v in y + x)
    projection = exact_dot(ux + uy, velocity)
    assert projection == -(a + b) * c * c <= 0
    assert c * c + exact_dot(x, (-y[1], y[0])) ** 2 == 1
    return projection


def main():
    circle = [unit_circle(F(t, 3)) for t in range(-9, 10)] + [(F(-1), F(0))]
    lengths = [unit_circle(F(t, 13)) for t in range(1, 13)]
    zero_count = 0
    for x, y, (a, b) in product(circle, circle, lengths):
        assert a > 0 and b > 0
        if projected_velocity(x, y, a, b) == 0:
            zero_count += 1
    assert zero_count > 0
    x, y = unit_circle(F(0)), unit_circle(F(1, 2))
    z = projected_velocity(x, y, F(3, 5), F(4, 5))
    assert z == F(-63, 125)
    assert projected_velocity(tuple(-v for v in x), tuple(-v for v in y), F(3, 5), F(4, 5)) == z
    assert 2 * z == F(-126, 125)

    # With s=t² the product √s ds becomes 2t² dt.
    # The exact primitive is 2t³/3.
    length_mean = F(2, 3) * (1 ** 3 - 0 ** 3)
    angle_mean = F(1, 2)  # quarter-turn pairs have squared dot products summing to one
    assert 2 * (length_mean + length_mean) == F(8, 3)
    assert -2 * (length_mean + length_mean) * angle_mean == F(-4, 3)

    print(f"Exact quartic coefficients at {len(circle) ** 2 * len(lengths)} corner fixtures")
    print(f"Orthogonal pairs with zero derivative: {zero_count}")
    print("Worked support derivative = -63/125; full directional derivative = -126/125")
    print("Normalized initial mean width = 8/3; normalized mean-width derivative = -4/3")


if __name__ == "__main__":
    main()
