import unittest

def is_string_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    return True

#def is_string_rotation(s1, s2):
#    # TODO: find more optimal solution
#    if len(s1) != len(s2):
#        return False
#    for i in range(1, len(s1)):
#        if s1[i:] in s2 and s1[:i] in s2:
#            return True
#    return False # O((m+n)^2)

class TestIsStringRotation(unittest.TestCase):
    # TODO: add more tests
    TEST_DATA = [
        (("waterbottle", "erbottlewat"), True)
    ]

    def test_is_string_rotation(self):
        for (s1, s2), expected in self.TEST_DATA:
            self.assertEqual(is_string_rotation(s1, s2), expected)

if __name__ == "__main__":
    unittest.main()
