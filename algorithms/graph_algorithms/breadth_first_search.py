from collections import deque


# def bfs(graph, root, value):
#     """ возвращает True, если элемент существует, иначе - None"""
#     search_deque = deque()
#     search_deque += graph[root]
#     visited = []
#     if root == value:
#         return True
#     while search_deque:
#         node = search_deque.popleft()
#         if node not in visited:
#             visited.append(node)
#             if node == value:
#                 return True
#             search_deque += graph[node]
#     return False


def bfs(graph, start, value):
    """ возвращает наикратчайший путь, если элемента не сущестует - None"""
    search_deque = deque()
    search_deque += start
    visited = [start]
    previous = {}
    while search_deque:
        node = search_deque.popleft()
        neighbours = graph[node]
        if node == value:
            result = []
            item = node
            while item:
                result.append(item)
                item = previous.get(item)
            result.reverse()
            return result
        for neighbour in neighbours:
            if neighbour not in visited:
                previous[neighbour] = node
                search_deque += neighbour
                visited.append(neighbour)
    return None
