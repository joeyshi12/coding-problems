import unittest

def is_one_edit_away(s1: str, s2: str) -> bool:
    diff = len(s1) - len(s2)
    if diff == 0:
        i = find_mismatch_index(s1, s2)
        return i == -1 or (s1[i+1:] == s2[i+1:])
    elif diff == -1:
        i = find_mismatch_index(s1, s2)
        return s1[i:] == s2[i+1:]
    elif diff == 1:
        i = find_mismatch_index(s1, s2)
        return s1[i+1:] == s2[i:]
    else:
        return False

def find_mismatch_index(s1: str, s2: str) -> int:
    if s1 == s2:
        return -1
    m = min(len(s1), len(s2))
    for i in range(m):
        if s1[i] != s2[i]:
            return i
    return m

class TestIsOneEditAway(unittest.TestCase):
    TEST_DATA = [
        (("", ""), True),
        (("pale", ""), False),
        (("", "pale"), False),
        (("pale", "pale"), True),
        (("pale", "ple"), True),
        (("pales", "pale"), True),
        (("pale", "bale"), True),
        (("pale", "bake"), False)
    ]

    def test_is_one_edit_away(self):
        for (s1, s2), expected in self.TEST_DATA:
            self.assertEqual(is_one_edit_away(s1, s2), expected)
            print(f"\"{s1}\", \"{s2}\" -> {expected}")

if __name__ == "__main__":
    unittest.main()
