#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    # Add zeros to ensure at least 2 elements
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)

    # Return a new tuple adding the first two indices
    return (a[0] + b[0], a[1] + b[1])

