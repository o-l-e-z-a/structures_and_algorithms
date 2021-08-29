import unittest
from algorithms.graph_algorithms.breadth_first_search import bfs
from algorithms.graph_algorithms.dijkstra import Dijkstra


class GraphTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.graph = {'0': ['1', '2'], '1': [], '2': ['3'], '3': ['4', '5', '6'], '4': [], '5': ['7', '8'], '6': ['9'],
                      '7': [], '8': [], '9': []}
        self.graph_2 = {'0': ['1', '2', '3'], '1': ['6'], '2': ['5'], '3': ['4', '5'], '4': [], '5': [], '6': ['7'],
                        '7': [8], '8': [4]}

    def test_bfs(self):
        self.assertEqual(bfs(self.graph, '0', '0'), ['0'])
        self.assertEqual(bfs(self.graph, '0', '9'), ['0', '2', '3', '6', '9'])
        self.assertEqual(bfs(self.graph, '0', '7'), ['0', '2', '3', '5', '7'])
        self.assertEqual(bfs(self.graph_2, '0', '4'), ['0', '3', '4'])
        self.assertIsNone(bfs(self.graph, '0', '66'))
        self.assertIsNone(bfs(self.graph, '0', '11'))

    def test_dijkstra_1(self):
        graph = {'kniga': {
            'plastina': 5,
            'poster': 0
        },
            'poster': {
                'gitara': 30,
                'baraban': 35,
            },
            'plastina': {
                'gitara': 15,
                'baraban': 20,
            },
            'gitara': {
                'piano': 20,
            },
            'baraban': {
                'piano': 10,
            },
            'piano': {}
        }

        d = Dijkstra(graph)
        self.assertEqual(d('kniga', 'piano'), (35, ['kniga', 'plastina', 'baraban', 'piano']))

    def test_dijkstra_2(self):
        graph = {'start': {
            'a': 6,
            'b': 2
        },
            'a': {
                'fin': 1,
            },
            'b': {
                'a': 3,
                'fin': 5,
            },
            'fin': {}
        }

        d = Dijkstra(graph)
        self.assertEqual(d('start', 'fin'), (6, ['start', 'b', 'a', 'fin']))


if __name__ == '__main__':
    unittest.main()
