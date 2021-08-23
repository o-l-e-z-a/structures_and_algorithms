import unittest
from algorithms.search.binary_search import binary_search


class SearchTest(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()
