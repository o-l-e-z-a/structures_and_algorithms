import unittest
from algorithms.graph_algorithms.breadth_first_search import bfs


class GraphTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.graph = {'0': ['1', '2'], '1': [], '2': ['3'], '3': ['4', '5', '6'], '4': [], '5': ['7', '8'], '6': ['9'],
                      '7': [], '8': [], '9': []}

    def test_bfs(self):
        self.assertEqual(bfs(self.graph, '0', '0'), ['0'])
        self.assertEqual(bfs(self.graph, '0', '9'), ['0', '2', '3', '6', '9'])
        self.assertEqual(bfs(self.graph, '0', '7'), ['0', '2', '3', '5', '7'])
        self.assertEqual(bfs(self.graph, '0', '5'),  ['0', '2', '3', '5'])
        self.assertIsNone(bfs(self.graph, '0', '66'))
        self.assertIsNone(bfs(self.graph, '0', '11'))


if __name__ == '__main__':
    unittest.main()
