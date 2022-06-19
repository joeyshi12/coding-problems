# https://leetcode.com/problems/search-suggestions-system/

import unittest
from typing import List


def suggested_products(products: List[str], search_word: str) -> List[List[str]]:
    products.sort()
    suggestions, prefix, i = [], "", 0
    for c in search_word:
        prefix = prefix + c
        i = max(i, binary_search(products, prefix, i))
        suggestions.append([product for product in products[i:i + 3] if product.startswith(prefix)])
    return suggestions


def binary_search(products: List[str], val: str, i: int) -> int:
    j = len(products) - 1
    while i <= j:
        p = (i + j) // 2
        if p == 0 and products[p] > val:
            return 0
        if products[p - 1] < val <= products[p]:
            return p
        if products[p] < val:
            i = p + 1
        else:
            j = p - 1
    return -1


class TestSuggestedProducts(unittest.TestCase):
    def test_empty(self):
        result = suggested_products([], "")
        self.assertListEqual(result, [])

    def test_single_product(self):
        result = suggested_products(["mobile"], "mouse")
        expected = [["mobile"], ["mobile"], [], [], []]
        self.assertListEqual(result, expected)

    def test_perfect_match(self):
        result = suggested_products(["havana"], "havana")
        self.assertListEqual(result, [["havana"] for _ in range(6)])

    def test_products_1(self):
        products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
        result = suggested_products(products, "mouse")
        expected = [
            ["mobile", "moneypot", "monitor"],
            ["mobile", "moneypot", "monitor"],
            ["mouse", "mousepad"],
            ["mouse", "mousepad"],
            ["mouse", "mousepad"]
        ]
        self.assertListEqual(result, expected)

    def test_products_2(self):
        products = ["bags", "baggage", "banner", "box", "cloths"]
        result = suggested_products(products, "bags")
        expected = [
            ["baggage", "bags" ,"banner"],
            ["baggage", "bags" ,"banner"],
            ["baggage", "bags"],
            ["bags"]
        ]
        self.assertListEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
