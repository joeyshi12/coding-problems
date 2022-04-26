import unittest

def URLify(s, size):
    if size > len(s):
        raise Exception
    url = ""
    for i in range(size):
        url = url + (s[i] if s[i] != " " else "%20")
    return url

class TestURLify(unittest.TestCase):
    TEST_DATA = [
        (("", 0), ""),
        (("   ", 1), "%20"),
        (("a a  ", 3), "a%20a"),
        (("Mr John Smith    ", 13), "Mr%20John%20Smith"),
    ]

    def test_URLify(self):
        for (s, size), expected in self.TEST_DATA:
            self.assertEqual(URLify(s, size), expected)
            print(f"(\"{s}\", {size}) -> \"{expected}\"")

if __name__ == "__main__":
    unittest.main()
