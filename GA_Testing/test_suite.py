# File for testing the behavior of our genetic_helpers.py script

import genetic_helpers as gh
import unittest

def _bitstring_to_binary(bitstring):
    value = 0
    place_counter = 0
    for bit in reversed(bitstring):
        value = 2**value * int(bit)
        place_counter = place_counter + 1
    return value


class TestGenHelpers(unittest.TestCase):
    pass
