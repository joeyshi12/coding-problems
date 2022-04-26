import unittest

def compress_string(s):
    cs = ""
    char_idx = 0
    for i in range(1, len(s) + 1):
        if i == len(s) or s[char_idx] != s[i]:
            cs = cs + s[char_idx] + str(i - char_idx)
            char_idx = i
    return cs if len(cs) < len(s) else s

class TestCompressString(unittest.TestCase):
    TEST_DATA = [
        ("", ""),
        ("a", "a"),
        ("aa", "aa"),
        ("aaa", "a3"),
        ("aabcccccaaa", "a2b1c5a3")
    ]

    def test_compress_string(self):
        for s, expected in self.TEST_DATA:
            self.assertEqual(compress_string(s), expected)
            print(f"\"{s}\" -> \"{expected}\"")

if __name__ == "__main__":
    unittest.main()
