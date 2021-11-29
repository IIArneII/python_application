from collections import deque
from typing import Union


class Vertex:
    def __init__(self, key):
        self.id = key
        self.connected_to = {}

    def add_neighbor(self, nbr, weight=0):
        self.connected_to[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connected_to])

    def get_connections(self):
        return self.connected_to.keys()

    def get_weight(self, nbr):
        return self.connected_to[nbr]


class Graph:
    def __init__(self):
        self.vert_list = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(key)
        self.vert_list[key] = new_vertex
        return new_vertex

    def __contains__(self, n):
        return n in self.vert_list

    def get_vertex(self, n) -> Union[Vertex, None]:
        if n in self:
            return self.vert_list[n]
        return

    def add_edge(self, f, t, cost: [int, float] = 0.):
        if f not in self:
            self.add_vertex(f)
        if t not in self:
            self.add_vertex(t)
        self.vert_list[f].add_neighbor(self.vert_list[t], cost)

    def get_vertices(self):
        return self.vert_list.keys()

    def __iter__(self):
        return iter(self.vert_list.values())

    def search(self, name, target):
        paths = {}
        search_queue = deque()
        searched = set()
        search_queue.append(self.get_vertex(name))
        while search_queue:
            vertex = search_queue.popleft()
            if vertex not in searched:
                if vertex.id == target:
                    path = [vertex.id]
                    while path[-1] != name:
                        path.append(paths[path[-1]])
                    return path[::-1]
                searched.add(vertex)
                for i in vertex.get_connections():
                    if i.id not in paths:
                        paths[i.id] = vertex.id
                    search_queue.append(i)
        return

    def dijkstra(self, start, end):
        marks = {i: float('inf') for i in self.get_vertices()}
        visited = []
        paths = {}
        marks[start] = 0
        while len(visited) < len(self.get_vertices()):
            current = min(marks, key=lambda x: marks[x] if x not in visited else float('inf'))
            if current in visited:
                return
            if current == end:
                path = [end]
                while path[-1] != start:
                    path.append(paths[path[-1]])
                return marks[current], path[::-1]
            visited.append(current)
            for i in self.get_vertex(current).get_connections():
                if marks[i.id] > self.get_vertex(current).get_weight(i) + marks[current] and i.id not in visited:
                    marks[i.id] = self.get_vertex(current).get_weight(i) + marks[current]
                    paths[i.id] = current


g = Graph()
g.add_vertex('Белово')
g.add_vertex('Ленинск-Кузнецкий')
g.add_vertex('Киселевск')
g.add_vertex('Гурьевск')
g.add_vertex('Мыски')
g.add_vertex('Кемерово')
g.add_vertex('Новосибирск')

g.add_edge('Белово', 'Ленинск-Кузнецкий', 39.2)
g.add_edge('Ленинск-Кузнецкий', 'Киселевск', 93)
g.add_edge('Белово', 'Киселевск', 66.5)
g.add_edge('Белово', 'Гурьевск', 34.3)
g.add_edge('Гурьевск', 'Киселевск', 78.9)
g.add_edge('Ленинск-Кузнецкий', 'Мыски', 194)
g.add_edge('Киселевск', 'Кемерово', 176)
g.add_edge('Кемерово', 'Новосибирск', 265)
g.add_edge('Мыски', 'Новосибирск', 437)


start = input("Введите начало пути: ")
end = input("Введите конец пути: ")
if start in g.get_vertices() and end in g.get_vertices():
    path = g.dijkstra(start, end)
    if path:
        print('Длина пути: ', path[0], '\nПуть: ', path[1])
    else:
        print('Пути не существет')
else:
    print('Указанного города не существует')
