import unittest
import random

from algorithms.sorts.selection_sort import selection_sort
from algorithms.sorts.bubble_sort import bubble_sort
from algorithms.sorts.quick_sort import quick_sort
from algorithms.sorts.merge_sort import merge_sort
from algorithms.sorts.insertion_sort import insertion_sort
from algorithms.sorts.shell_sort import shell_sort
from algorithms.sorts.heap_sort import heap_sort
from algorithms.sorts.counting_sort import counting_sort


def get_functions():
    """ Находим все импортиванные ф-ии со словом sort"""
    sorts = [globals()[name] for name in globals() if name.endswith('sort') and name != 'counting_sort']
    return sorts


class SortsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.list_1 = list(range(100, 0, -1))
        self.list_2 = list(range(0, -100, -1))
        self.list_3 = [random.randint(0, 130) for i in range(1000)]
        self.sort_list_1 = sorted(self.list_1)
        self.sort_list_2 = sorted(self.list_2)
        self.sort_list_3 = sorted(self.list_3)

    def test_all_sorts(self):
        """ Тестирование всех импориванных функций(кроме осообых случаев) """
        for func in get_functions():
            self.assertEqual(self.sort_list_1, func(self.list_1))
            self.assertEqual(self.sort_list_2, func(self.list_2))
            self.assertEqual(self.sort_list_3, func(self.list_3))

    def test_counting_sort(self):  # не поддерживает сортировку с отрицательными числами
        self.assertEqual(self.sort_list_1, counting_sort(self.list_1))
        self.assertEqual(self.sort_list_3, counting_sort(self.list_3))


if __name__ == '__main__':
    unittest.main()
