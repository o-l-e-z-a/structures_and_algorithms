from collections import deque


def bfs(graph, root, value):
    search_deque = deque()
    search_deque += graph[root]
    visited = set()
    if root == value:
        return True
    while search_deque:
        node = search_deque.popleft()
        visited.add(node)
        if node == value:
            return True
        search_deque += graph[node]
    return False


