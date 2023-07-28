"""
Graph() creates a new empty graph.

add_vertex(vert) adds an instance of Vertex to the graph.

add_edge(from_vert, to_vert) adds a new directed edge to the graph that
connects two vertices.

add_edge(from_vert, to_vert, weight) adds a new weighted directed edge to the
graph that connects two vertices.

get_vertex(vert_key) finds the vertex in the graph named vert_key.

get_vertices() returns the list of all vertices in the graph.

in returns True for a statement of the form vertex in graph if the given vertex
is in the graph, False otherwise.
"""


class Vertex:
    def __init__(self, key):
        self.key = key
        self.neighbors = {}

    def get_neighbor(self, other):
        return self.neighbors.get(other, None)

    def set_neighbor(self, other, weight=0):
        self.neighbors[other] = weight

    def __repr__(self):
        return f"Vertex({self.key})"

    def __str__(self):
        return str(self.key) + " connected to: " + str([x.key for x in self.neighbors])

    def get_neighbors(self):
        return self.neighbors.keys()

    def get_key(self):
        return self.key


class Graph:
    def __init__(self):
        self.vertices = {}

    def set_vertex(self, key):
        self.vertices[key] = Vertex(key)

    def get_vertex(self, key):
        return self.vertices.get(key, None)

    def __contains__(self, key):
        return key in self.vertices

    def add_edge(self, from_vert, to_vert, weight=0):
        if from_vert not in self.vertices:
            self.set_vertex(from_vert)
        if to_vert not in self.vertices:
            self.set_vertex(to_vert)
        self.vertices[from_vert].set_neighbor(self.vertices[to_vert], weight)

    def get_vertices(self):
        return self.vertices.keys()

    def __iter__(self):
        return iter(self.vertices.values())


def main():
    g = Graph()
    for i in range(6):
        g.set_vertex(i)
    g.vertices
    g.add_edge(0, 1, 5)
    g.add_edge(0, 5, 2)
    g.add_edge(1, 2, 4)
    g.add_edge(2, 3, 9)
    g.add_edge(3, 4, 7)
    g.add_edge(3, 5, 3)
    g.add_edge(4, 0, 1)
    g.add_edge(5, 4, 8)
    g.add_edge(5, 2, 1)
    for v in g:
        for w in v.get_neighbors():
            print(f"({v.get_key()}, {w.get_key()}, {v.neighbors[w]})")


if __name__ == "__main__":
    main()
