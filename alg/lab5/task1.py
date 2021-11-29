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

    def add_edge(self, f, t, cost=0):
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


g = Graph()
g.add_vertex('1')
g.add_vertex('2')
g.add_vertex('3')
g.add_vertex('4')
g.add_vertex('5')

g.add_edge('5', '1')
g.add_edge('5', '2')
g.add_edge('1', '4')
g.add_edge('2', '3')
g.add_edge('3', '5')
g.add_edge('2', '1')

print(g.search('3', '4'))
