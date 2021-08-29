class Dijkstra:
    def __init__(self, graph: dict):
        self._graph = graph
        self._costs = {}
        self._processed = []
        self._parents = {}

    def __call__(self, root: str, item: str):
        """алгоритм Дейкстры"""
        self.set_start_value(root, item)
        node = self.find_lower_cost_node()
        while node is not None:
            self.set_cost(node)
            cost = self._costs.get(node)
            neighbors = self._graph[node]
            for n in neighbors.keys():
                new_cost = cost + neighbors[n]
                if self._costs[n] > new_cost:
                    self._costs[n] = new_cost
                    self._parents[n] = node
            self._processed.append(node)
            node = self.find_lower_cost_node()

        return self._costs[item], self.return_path(item)

    def find_lower_cost_node(self):
        lowest_cost = float('inf')
        lowest_cost_node = None
        for node in self._costs:
            cost = self._costs[node]
            if cost < lowest_cost and node not in self._processed:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node

    def set_start_value(self, root: str, item: str):
        """задать начальные значения стоимости и родителей для соседей корня"""
        self.set_cost(root)
        self.set_start_parents(root)
        self._costs[item] = float('inf')

    def set_cost(self, node):
        """задать стоимости для соседей узла, если их нету"""
        node = self._graph.get(node)
        for key in node:
            self._costs.setdefault(key, node[key])

    def set_start_parents(self, root):
        """ задать родителей для начального элемента"""
        root_node = self._graph.get(root)
        for key in root_node.keys():
            self._parents[key] = root

    def return_path(self, item):
        """возвращает быстрый путь"""
        result = []
        while item:
            result.append(item)
            item = self._parents.get(item)
        result.reverse()
        return result
