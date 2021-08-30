import unittest

from algorithms.search.KMP import kmp
from algorithms.search.binary_search import binary_search


class BinarySearchTest(unittest.TestCase):
    def setUp(self) -> None:
        self.list_1 = list(range(100))

    def test_binary_search(self):
        result_1 = self.list_1.index(50)
        result_2 = self.list_1.index(99)
        result_3 = self.list_1.index(0)
        result_4 = self.list_1.index(47)
        self.assertEqual(result_1, binary_search(self.list_1, 50))
        self.assertEqual(result_2, binary_search(self.list_1, 99))
        self.assertEqual(result_3, binary_search(self.list_1, 0))
        self.assertEqual(result_4, binary_search(self.list_1, 47))

    def test_fail_binary_search(self):
        self.assertEqual(None, binary_search(self.list_1, -1))
        self.assertEqual(None, binary_search(self.list_1, 101))


class KMPTest(unittest.TestCase):
    def setUp(self) -> None:
        self.text = 'abacadabadacdababdcadcccabbabcabab'
        self.search_value = 'abab'
        self.fail_search_value = 'abaz'

    def test_kmp(self):
        indices = kmp(self.text, self.search_value)
        self.assertEqual(indices, [13, 30])

    def test_fail_kmp(self):
        indices = kmp(self.text, self.fail_search_value)
        self.assertEqual(indices, [])

if __name__ == '__main__':
    unittest.main()
