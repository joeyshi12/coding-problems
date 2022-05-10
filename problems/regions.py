"""
cpsc110 - lecture 12

Problem 4: Design a function that consumes a region and a string
and looks for a region with the given label.  If there is one
the function should produce the first one it finds.  If there is
not one it should produce false. The signature for the function
is given below
"""

from typing import List, Optional
from dataclasses import dataclass
import unittest


@dataclass
class Region:
    label: str
    weight: int


class NestedRegion:
    color: List[int]

    def __init__(self, color: str, single: Region = None, group: List['NestedRegion'] = None):
        if (single is None and group is None) or (single is not None and group is not None):
            raise Exception
        self.single = single
        self.group = group
        self.color = color

    def is_region(self) -> bool:
        return self.single is not None

    def get_region(self) -> Region:
        if not self.is_region():
            raise Exception
        return self.single

    def get_group(self) -> List['NestedRegion']:
        return self.group


def find_region(label: str, nest: NestedRegion) -> Optional[Region]:
    if nest.is_region():
        region = nest.get_region()
        return region if region.label == label else None
    for child in nest.get_group():
        region = find_region(label, child)
        if region:
            return region
    return None


class TestFindRegion(unittest.TestCase):
    def test_empty(self):
        nest = NestedRegion("black", group=[])
        result = find_region("sss-one", nest)
        self.assertIsNone(result)

    def test_single_found(self):
        nest = NestedRegion("red", single=Region("sss-one", 20))
        result = find_region("sss-one", nest)
        self.assertEqual(result, nest.single)

    def test_single_not_found(self):
        nest = NestedRegion("blue", single=Region("sss-two", 40))
        result = find_region("sss-one", nest)
        self.assertIsNone(result)

    def test_group(self):
        single1 = NestedRegion("red", single=Region("sss-one", 20))
        single2 = NestedRegion("blue", single=Region("sss-two", 40))
        single3 = NestedRegion("orange", single=Region("sss-three", 60))
        single4 = NestedRegion("yellow", single=Region("sss-four", 80))
        single5 = NestedRegion("blue", single=Region("sss-five", 100))
        nest1 = NestedRegion("black", group=[single1, single2, single3])
        nest2 = NestedRegion("white", group=[nest1])
        nest3 = NestedRegion("brown", group=[single4, single5])
        nest4 = NestedRegion("purple", group=[nest2, nest3])
        result = find_region("sss-two", nest4)
        self.assertEqual(result, single2.single)


if __name__ == "__main__":
    unittest.main()
