import unittest
from algorithms.graph_algorithms.breadth_first_search import bfs


class GraphTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.graph = {'0': ['1', '2'], '1': [], '2': ['3'], '3': ['4', '5', '6'], '4': [], '5': ['7', '8'], '6': ['9'],
                      '7': [], '8': [], '9': []}

    def test_something(self):
        self.assertEqual(bfs(self.graph, '0', '0'), True)
        self.assertEqual(bfs(self.graph, '0', '9'), True)
        self.assertEqual(bfs(self.graph, '0', '7'), True)
        self.assertEqual(bfs(self.graph, '0', '5'), True)
        self.assertEqual(bfs(self.graph, '0', '66'), False)
        self.assertEqual(bfs(self.graph, '0', '11'), False)


if __name__ == '__main__':
    unittest.main()
